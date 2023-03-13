import schemas 
from database import get_session
from database.core import AsyncSession
from crud import user
from crud.utils.errors import PasswordsMismatchError
from crud.utils.user import CreateUserConstructor
from ..responses.user import (
    NoSuchUserResponse, 
    UserWasntCreatedResponse, 
    UserCreatedSuccessfullyResponse,
    UserEmailUpdatedSuccessfully,
    UserLoginUpdatedSuccessfully,
    UserDeletedSuccessfully,
    UserPasswordUpdatedSuccessfully,
    UserPasswordMismatchResponse,
)

from fastapi import (
    HTTPException,
    APIRouter, 
    Depends,
    status,
)
from fastapi.responses import JSONResponse

from typing import Union



router = APIRouter(prefix='/user')

@router.post('/create', status_code=status.HTTP_201_CREATED, tags=['POST'])
async def create_user_endpoint(data: CreateUserConstructor, database_session: AsyncSession = Depends(get_session)) -> dict:
    is_created = await user.create(data, database_session)
    if is_created:
        return JSONResponse(
            status_code=status.HTTP_201_CREATED, 
            content=UserCreatedSuccessfullyResponse(
                status=status.HTTP_201_CREATED,
                message='User successfully created'
            ).to_dict(),
        )
    
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content=UserWasntCreatedResponse(
            status=status.HTTP_400_BAD_REQUEST,
            message='User was not created'
        ).to_dict(),
    )

@router.get('/get/{user_data}', status_code=status.HTTP_200_OK, response_model=schemas.User, tags=['GET'])
async def get_user_endpoint(user_data: str, database_session: AsyncSession = Depends(get_session)) -> Union[NoSuchUserResponse, schemas.User]:
    
    if '@' in user_data:
        result = await user.get_by_email(user_data, database_session)
    elif isinstance(user_data, str):
        result = await user.get_by_login(user_data, database_session)
    
    if not result:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST, 
            content=NoSuchUserResponse(
                status=status.HTTP_400_BAD_REQUEST,
                message='No such user'
            ).to_dict(),
        )
    return result

@router.put('/update/login', status_code=status.HTTP_200_OK, response_model=UserLoginUpdatedSuccessfully, tags=['PUT'])
async def update_login_user_endpoint(user_data: schemas.UpdateUserLogin, database_session: AsyncSession = Depends(get_session))-> Union[NoSuchUserResponse, UserLoginUpdatedSuccessfully]:
    
    result = await user.update_login(**user_data.to_dict(), _session=database_session)
    if not result:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST, 
            content=NoSuchUserResponse(
                status=status.HTTP_400_BAD_REQUEST,
                message='No such user to update login'
            ).to_dict(),
        )
    
    return UserLoginUpdatedSuccessfully(
        status=status.HTTP_200_OK,
        message='User login updated successfully'
    ).to_dict()

@router.put('/update/email', status_code=status.HTTP_200_OK, response_model=UserLoginUpdatedSuccessfully, tags=['PUT'])
async def update_email_user_endpoint(user_data: schemas.UpdateUserEmail, database_session: AsyncSession = Depends(get_session)) -> Union[NoSuchUserResponse, UserEmailUpdatedSuccessfully]:
    
    result = await user.update_email(
        old_email=str(user_data.old_email),
        new_email=str(user_data.new_email),
        _session=database_session),
    if not result:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST, 
            content=NoSuchUserResponse(
                status=status.HTTP_400_BAD_REQUEST,
                message='No such user to update email'
            ).to_dict(),
        )
    
    return UserEmailUpdatedSuccessfully(
        status=status.HTTP_200_OK,
        message='User email updated successfully'
    ).to_dict()


@router.put('/update/password', status_code=status.HTTP_200_OK, response_model=UserPasswordUpdatedSuccessfully, tags=['PUT'])
async def update_password_endpoint(user_data: Union[schemas.UpdateUserPasswordWithLogin,schemas.UpdateUserPasswordWithEmail] , database_session: AsyncSession = Depends(get_session))-> Union[NoSuchUserResponse, UserPasswordUpdatedSuccessfully]:

    try:
        if isinstance(user_data, schemas.UpdateUserPasswordWithLogin):
            result = await user.update_password_by_login(**user_data.to_dict(), _session=database_session)
        elif isinstance(user_data, schemas.UpdateUserPasswordWithEmail):
            result = await user.update_password_by_email(**user_data.to_dict(), _session=database_session)
    except PasswordsMismatchError:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content=UserPasswordMismatchResponse(
                status=status.HTTP_400_BAD_REQUEST,
                message='Password is incorrect'
            )
        )
    if not result:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST, 
            content=NoSuchUserResponse(
                status=status.HTTP_400_BAD_REQUEST,
                message='No such user to update password'
            ).to_dict(),
        )
    
    return UserPasswordUpdatedSuccessfully(
        status=status.HTTP_200_OK,
        message='User password updated successfully'
    ).to_dict()

# @router.put('/update/password_by_email', status_code=status.HTTP_200_OK, response_model=UserPasswordUpdatedSuccessfully, tags=['PUT'])
# async def update_password_by_email_endpoint(user_data: schemas.UpdateUserPasswordWithEmail, database_session: AsyncSession = Depends(get_session))-> Union[NoSuchUserResponse, UserPasswordUpdatedSuccessfully]:
#     try:
#         result = await user.update_password_by_email(**user_data.to_dict(), _session=database_session)
#     except PasswordsMismatchError:
#         return JSONResponse(
#             status_code=status.HTTP_400_BAD_REQUEST,
#             content=UserPasswordMismatchResponse(
#                 status=status.HTTP_400_BAD_REQUEST,
#                 message='Password is incorrect'
#             ).to_dict(),
#         )
#     if not result:
#         return JSONResponse(
#             status_code=status.HTTP_400_BAD_REQUEST, 
#             content=NoSuchUserResponse(
#                 status=status.HTTP_400_BAD_REQUEST,
#                 message='No such user to update password'
#             ).to_dict(),
#         )
    
#     return UserPasswordUpdatedSuccessfully(
#         status=status.HTTP_200_OK,
#         message='User password updated successfully'
#     ).to_dict()

@router.delete('/delete', status_code=status.HTTP_200_OK, response_model=UserDeletedSuccessfully, tags=['DELETE'])
async def delete_user_endpoint(user_data: str ,database_session: AsyncSession = Depends(get_session)) -> Union[NoSuchUserResponse, UserDeletedSuccessfully]:
    
    if '@' in user_data:
        result = await user.delete_by_email(user_data, database_session)
    elif isinstance(user_data, str):
        result = await user.delete_by_login(user_data, database_session)
    
    if not result:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST, 
            content=NoSuchUserResponse(
                status=status.HTTP_400_BAD_REQUEST,
                message='No such user to delete'
            ).to_dict(),
        )
    
    return UserDeletedSuccessfully(
        status=status.HTTP_200_OK,
        message='User successfully deleted'
    ).to_dict()