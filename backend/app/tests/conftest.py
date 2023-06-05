import pytest, httpx

from typing import AsyncGenerator, TypeVar, Callable, Any

from settings import Setting
from settings.test import Setting as AdditionalSetting
from database.core import init_db
from main import app

settings = Setting(_env_file=AdditionalSetting.Config.env_file, module=AdditionalSetting)

Fixture = TypeVar('Fixture', bound=Callable[..., Any])

pytestmark = pytest.mark.anyio


@pytest.fixture(scope='session')
def anyio_backend():
    return 'asyncio'

@pytest.fixture(scope='function')
async def create_user_v1() -> None:
    async with httpx.AsyncClient(app=app, base_url='http://test') as client:
        json_data = {
            "name": "test_name",
            "surname": "test_surname",
            "login": "test_login",
            "photo": "test_photo/path",
            "email": "test_email@example.com",
            "password": "test_password",
            "confirm_password": "test_password"
        }
        await client.post('/api/v1/auth/register', json=json_data)

@pytest.fixture(scope='function')
async def created_user_data_v1() -> dict:
    async with httpx.AsyncClient(app=app, base_url='http://test') as client:
        json_data = {
            "name": "test_name",
            "surname": "test_surname",
            "login": "test_login",
            "photo": "test_photo/path",
            "email": "test_email@example.com",
            "password": "test_password",
            "confirm_password": "test_password"
        }
        response =  await client.post('/api/v1/auth/register', json=json_data)
        yield response.json()

@pytest.fixture(scope='function')
async def database() -> None:
    await init_db()


@pytest.fixture(scope='session')
async def client() -> AsyncGenerator[httpx.AsyncClient, None]:
    async with httpx.AsyncClient(app=app, base_url='http://test') as client:
        yield client