import uuid
from datetime import timedelta
from typing import Union

import schemas
from settings import settings
from services.auth.oauth2 import AuthJWT, MissingTokenError, require_user
from services.auth.cookie import Cookie
from services.auth.password import verify_password
from services.auth.encryption import get_decrypted_value, get_encrypted_key
from services.auth.confirmation import send_email
from crud import user as usr
from routers.responses.user import (
    UserCreatedSuccessfullyResponse,
    UserWasntCreatedResponse,
    UserPasswordMismatchResponse,
    UserLoginSuccessfullyResponse,
    UserDoesNotExistsResponse,
    UserDoesNotActivatedResponse,
    MissingTokenResponse,
)
from database import get_session
from database.core import AsyncSession

from fastapi import (
    APIRouter, 
    Depends,
    status,
    Response,
)
from fastapi.responses import JSONResponse
from pydantic import EmailStr


router = APIRouter(prefix='/auth', tags=['AUTH'])



@router.post('/register', status_code=status.HTTP_201_CREATED, response_model=schemas.UserWithID)
async def create_user_endpoint(data: schemas.CreateUser, database_session: AsyncSession = Depends(get_session)) -> schemas.UserWithID:
    
    if data.password != data.confirm_password:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content=UserPasswordMismatchResponse(
                status=status.HTTP_400_BAD_REQUEST,
                message='Passwords mismatch'
            ).dict()
        )
    data = data.dict()
    data['email'] = data['email'].lower()
    data['role'] = 'user'
    user = await usr.create(data, database_session)
    if user:
        user_key = get_encrypted_key(user.id)
        await send_email(to=data['email'], endpoint_key=f'/api/v1/auth/verify/{user_key}', user=user)
        return JSONResponse(
            status_code=status.HTTP_201_CREATED, 
            content=UserCreatedSuccessfullyResponse(
                status=status.HTTP_201_CREATED,
                message='User successfully created. We send a message on your email address to confirm registration',
                user=user.dict(),
            ).dict(),
        )
    
    return JSONResponse(
        status_code=status.HTTP_409_CONFLICT,
        content=UserWasntCreatedResponse(
            status=status.HTTP_409_CONFLICT,
            message='User already exists'
        ).dict(),
    )

@router.post('/login', status_code=status.HTTP_200_OK, response_model=UserLoginSuccessfullyResponse)
async def login_endpoint(
    data: Union[schemas.AuthenticateWithLogin, schemas.AuthenticateWithEmail], 
    response: Response,
    auth: AuthJWT = Depends(),
    database_session: AsyncSession = Depends(get_session),
    ) -> UserLoginSuccessfullyResponse:

    if isinstance(data, schemas.AuthenticateWithLogin):
        user = await usr.get(data.login, database_session, True)
    elif isinstance(data, schemas.AuthenticateWithEmail):
        user = await usr.get(EmailStr(data.email.lower()), database_session, True)
    
    if not user:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content=UserDoesNotExistsResponse(
                status=status.HTTP_400_BAD_REQUEST,
                message='Incorrect Email or Password',
            ).dict()
        )
    if not user.is_active:
        return JSONResponse(
            status_code=status.HTTP_401_UNAUTHORIZED,
            content=UserDoesNotActivatedResponse(
                status=status.HTTP_401_UNAUTHORIZED,
                message='Please verify your email address',
            ).dict()
        )
    if not verify_password(data.password, user.password):
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content=UserDoesNotExistsResponse(
                status=status.HTTP_400_BAD_REQUEST,
                message='Incorrect Email or Password',
            ).dict()
        )
    access_token = auth.create_access_token(
        subject=str(user.id),
        expires_time=timedelta(minutes=settings.access_token_expires_in)
    )
    refresh_token = auth.create_refresh_token(
        subject=str(user.id),
        expires_time=timedelta(minutes=settings.refresh_token_expires_in)
    )

    response.set_cookie(
        **Cookie(
            key='access_token',
            value=access_token,
            max_age=settings.access_token_expires_in * 60,
            expires=settings.access_token_expires_in * 60,
            httponly=True,
        ).dict()
    )
    response.set_cookie(
        **Cookie(
            key='refresh_token',
            value=refresh_token,
            max_age=settings.refresh_token_expires_in * 60,
            expires=settings.refresh_token_expires_in * 60,
            httponly=True,
        ).dict()
    )
    response.set_cookie(
        **Cookie(
            key='logged_in',
            value='True',
            max_age=settings.access_token_expires_in * 60,
            expires=settings.access_token_expires_in * 60,
            httponly=False,
        ).dict()
    )
    return UserLoginSuccessfullyResponse(
        status='success',
        message='Succeesfully logged in',
        token=access_token,
    )


@router.get('/verify/{key}', status_code=status.HTTP_200_OK)
async def verify_user_enpoint(key: str,  database_session: AsyncSession = Depends(get_session)) -> JSONResponse:
    
    cipher_key, encrypted_value = key.split(':')
    user_id = get_decrypted_value(encrypted_value=encrypted_value, cipher_key=cipher_key.encode())
    user = await usr.get(uuid.UUID(user_id), database_session)
    if not user:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={'status': 'failed', 'message': 'No such user to confirm registration'}
        )
    if user.is_active:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={'status': 'failed', 'message': 'This user is already activated'}
        )
    await usr.update(schemas.UpdateUser(entity=uuid.UUID(user.id), update={'is_active': True}), database_session)

    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={'status': 'success', 'message': 'Your account was activated'}
    )

@router.get('/refresh', status_code=status.HTTP_200_OK, response_model=UserLoginSuccessfullyResponse)
async def refresh_token_endpoint(
    response: Response,
    auth: AuthJWT = Depends(),
    database_session: AsyncSession = Depends(get_session),
) -> UserLoginSuccessfullyResponse:
    
    try:
        auth.jwt_refresh_token_required()
        user_id = auth.get_jwt_subject()

        if not user_id:
            return JSONResponse(
                status_code=status.HTTP_400_BAD_REQUEST,
                content=UserDoesNotExistsResponse(
                    status=status.HTTP_400_BAD_REQUEST,
                    message='Cannot refresh token',
                ).dict()
            )
        user = await usr.get(uuid.UUID(user_id), database_session)
        if not user:
            return JSONResponse(
                status_code=status.HTTP_400_BAD_REQUEST,
                content=UserDoesNotExistsResponse(
                    status=status.HTTP_400_BAD_REQUEST,
                    message='The user belonging to this token no longer exist',
                ).dict()
            )
        access_token = auth.create_access_token(
            subject=str(user.id),
            expires_time=timedelta(minutes=settings.access_token_expires_in)
        )

    except MissingTokenError:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content=MissingTokenResponse(
                status=status.HTTP_400_BAD_REQUEST,
                message='Please provide refresh token',
            ).dict()
        )
    except Exception as ex:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={'error': ex.__class__.__name__.lower()}
        )
    response.set_cookie(
        **Cookie(
            key='access_token',
            value=access_token,
            max_age=settings.access_token_expires_in * 60,
            expires=settings.access_token_expires_in * 60,
            httponly=True,
        ).dict()
    )
    response.set_cookie(
        **Cookie(
            key='logged_in',
            value='True',
            max_age=settings.access_token_expires_in * 60,
            expires=settings.access_token_expires_in * 60,
            httponly=False,
        ).dict()
    )
    return UserLoginSuccessfullyResponse(
        status='success',
        message='Succeesfully refreshed',
        token=access_token,
    )

@router.get('/logout', status_code=status.HTTP_200_OK)
async def logout_endpoint(
    response: Response,
    auth: AuthJWT = Depends(),
    user_id: str | JSONResponse = Depends(require_user)
) -> JSONResponse:
    
    if isinstance(user_id, JSONResponse):
        return user_id
    
    auth.unset_jwt_cookies()
    response.set_cookie('logged_in', '', -1)

    return {'status': 'success'}