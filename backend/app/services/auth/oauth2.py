import base64, uuid

from fastapi import Depends, status
from fastapi.responses import JSONResponse
from fastapi_jwt_auth import AuthJWT
from fastapi_jwt_auth.exceptions import MissingTokenError
from pydantic import BaseModel
from crud import user as usr

from settings import settings
from database.core import AsyncSession, get_session
from routers.responses.user import (
    NoSuchUserResponse, 
    UserNotActivetedResponse,
    MissingTokenResponse,
    InvalidTokenResponse,
)


class Settings(BaseModel):
    authjwt_algorithm: str = settings.jwt_algorithm
    authjwt_decode_algorithms: list[str] = [settings.jwt_algorithm]
    authjwt_token_location: set = {'cookies', 'headers'}
    authjwt_access_cookie_key: str = 'access_token'
    authjwt_refresh_cookie_key: str = 'refresh_token'
    authjwt_cookie_csrf_protect: bool = False
    authjwt_public_key: str = base64.b64decode(settings.jwt_public_key).decode('utf-8')
    authjwt_private_key: str = base64.b64decode(settings.jwt_private_key).decode('utf-8')


@AuthJWT.load_config
def get_config():
    return Settings()

async def require_user(
    database_session: AsyncSession = Depends(get_session),
    auth: AuthJWT = Depends()
    ) -> str | JSONResponse:

    try:
        auth.jwt_required()
        user_id = auth.get_jwt_subject()
        user = await usr.get(uuid.UUID(user_id), database_session)
        
        if not user:
            return JSONResponse(
                status_code=status.HTTP_401_UNAUTHORIZED,
                content=NoSuchUserResponse(
                    status=status.HTTP_401_UNAUTHORIZED,
                    message='User no longer exist'
                ).dict()
            )
        if not user.is_active:
            return JSONResponse(
                status_code=status.HTTP_401_UNAUTHORIZED,
                content=UserNotActivetedResponse(
                    status=status.HTTP_401_UNAUTHORIZED,
                    message='You are not verified'
                ).dict()
            )
    except MissingTokenError:
        return JSONResponse(
            status_code=status.HTTP_401_UNAUTHORIZED,
            content=MissingTokenResponse(
                status=status.HTTP_401_UNAUTHORIZED,
                message='You are not logged in'
            ).dict()
        )
    except Exception:
        return JSONResponse(
            status_code=status.HTTP_401_UNAUTHORIZED,
            content=InvalidTokenResponse(
                status=status.HTTP_401_UNAUTHORIZED,
                message='Token is invalid or has expired'
            ).dict()
        )
    return user_id