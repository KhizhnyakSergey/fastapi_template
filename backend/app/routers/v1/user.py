import re, uuid

import schemas, models
from database import get_session
from database.core import AsyncSession
from services.auth.oauth2 import require_user
from crud import user as usr
from crud.utils.errors import PasswordsMismatchError
from ..responses.user import (
    NoSuchUserResponse, 
    UserEmailUpdatedSuccessfully,
    UserLoginUpdatedSuccessfully,
    UserDeletedSuccessfully,
    UserPasswordUpdatedSuccessfully,
    UserPasswordMismatchResponse,
)

from fastapi import (
    APIRouter, 
    Depends,
    status,
)
from fastapi.responses import JSONResponse
from pydantic import EmailStr

from typing import Union


router = APIRouter(prefix='/users', tags=['USERS'])


@router.get('/me', response_model=schemas.UserPrivate)
async def get_me_endpoint(
    user_id: str | JSONResponse = Depends(require_user), 
    database_session: AsyncSession = Depends(get_session)
    ) -> schemas.UserPrivate:
    
    if isinstance(user_id, JSONResponse):
        return user_id
    return await usr.get(uuid.UUID(user_id), database_session, True)


@router.get('/get', status_code=status.HTTP_200_OK, response_model=schemas.UserWithID)
async def get_user_endpoint(
    user: str | EmailStr | uuid.UUID, 
    database_session: AsyncSession = Depends(get_session)
    ) -> Union[NoSuchUserResponse, schemas.UserWithID]:
    
    if re.search(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', user):
        result = await usr.get(EmailStr(user.lower()), database_session)
    else:
        try:
            user = uuid.UUID(user)
        except ValueError:
            ...
        result = await usr.get(user, database_session)
    
    if not result:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST, 
            content=NoSuchUserResponse(
                status=status.HTTP_400_BAD_REQUEST,
                message='No such user'
            ).dict(),
        )
    return result

@router.put('/update/login', status_code=status.HTTP_200_OK, response_model=UserLoginUpdatedSuccessfully)
async def update_login_user_endpoint(
    user_data: schemas.UpdateUserLogin, 
    database_session: AsyncSession = Depends(get_session),
    user_id: str | JSONResponse = Depends(require_user)
    ) -> Union[NoSuchUserResponse, UserLoginUpdatedSuccessfully]:
    
    if isinstance(user_id, JSONResponse):
        return user_id
    
    result = await usr.update(schemas.UpdateUser(entity=user_data.old_login, update={'login': user_data.new_login}), database_session)
    
    if not result:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST, 
            content=NoSuchUserResponse(
                status=status.HTTP_400_BAD_REQUEST,
                message='No such user to update login'
            ).dict(),
        )
    
    return UserLoginUpdatedSuccessfully(
        status=status.HTTP_200_OK,
        message='User login updated successfully'
    )

@router.put('/update/email', status_code=status.HTTP_200_OK, response_model=UserEmailUpdatedSuccessfully)
async def update_email_user_endpoint(
    user_data: schemas.UpdateUserEmail, 
    database_session: AsyncSession = Depends(get_session),
    user_id: str | JSONResponse = Depends(require_user)
    ) -> Union[NoSuchUserResponse, UserEmailUpdatedSuccessfully]:
    
    if isinstance(user_id, JSONResponse):
        return user_id
    
    result = await usr.update(schemas.UpdateUser(entity=EmailStr(user_data.old_email), update={'email': EmailStr(user_data.new_email)}), database_session)

    if not result:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST, 
            content=NoSuchUserResponse(
                status=status.HTTP_400_BAD_REQUEST,
                message='No such user to update email'
            ).dict(),
        )
    
    return UserEmailUpdatedSuccessfully(
        status=status.HTTP_200_OK,
        message='User email updated successfully'
    )

@router.put('/update/password', status_code=status.HTTP_200_OK, response_model=UserPasswordUpdatedSuccessfully)
async def update_password_endpoint(
    user_data: schemas.UpdateUserPassword, 
    database_session: AsyncSession = Depends(get_session),
    user_id: str | JSONResponse = Depends(require_user)
    ) -> Union[NoSuchUserResponse, UserPasswordUpdatedSuccessfully]:

    try:
        if isinstance(user_id, JSONResponse):
            return user_id
        
        result = await usr.update(
            schemas.UpdateUser(
                entity=uuid.UUID(user_id),
                update={
                    'old_password': user_data.old_password,
                    'password': user_data.new_password,
                }
            ),
            database_session
            )
    except PasswordsMismatchError:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content=UserPasswordMismatchResponse(
                status=status.HTTP_400_BAD_REQUEST,
                message='Password is incorrect'
            ).dict(),
        )
    if not result:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST, 
            content=NoSuchUserResponse(
                status=status.HTTP_400_BAD_REQUEST,
                message='No such user to update password'
            ).dict(),
        )
    
    return UserPasswordUpdatedSuccessfully(
        status=status.HTTP_200_OK,
        message='User password updated successfully'
    )

@router.delete('/delete', status_code=status.HTTP_200_OK, response_model=UserDeletedSuccessfully)
async def delete_user_endpoint(
    database_session: AsyncSession = Depends(get_session),
    user_id: str | JSONResponse = Depends(require_user)
    ) -> Union[NoSuchUserResponse, UserDeletedSuccessfully]:
    
    if isinstance(user_id, JSONResponse):
        return user_id

    result = await usr.delete(uuid.UUID(user_id), database_session)

    if not result:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST, 
            content=NoSuchUserResponse(
                status=status.HTTP_400_BAD_REQUEST,
                message='No such user to delete'
            ).dict(),
        )
    
    return UserDeletedSuccessfully(
        status=status.HTTP_200_OK,
        message='User successfully deleted'
    )