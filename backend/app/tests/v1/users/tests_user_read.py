from tests.conftest import (
    client, 
    database, 
    anyio_backend,
    create_user_v1,
    pytestmark,
    Fixture
)

from httpx import AsyncClient

from typing import Awaitable



async def test_get_user_by_login_success(client: AsyncClient, database: Awaitable[Fixture], create_user_v1: Awaitable[Fixture]) -> None:
    params = {
        "user": "test_login",
    }
    
    response = await client.get('/api/v1/users/get', params=params)
    assert response.status_code == 200, "success fetched by login"


async def test_get_user_by_login_failed(client: AsyncClient, database: Awaitable[Fixture], create_user_v1: Awaitable[Fixture]) -> None:
    params = {
        "user": "test_login_failed",
    }
    
    response = await client.get('/api/v1/users/get', params=params)
    assert response.status_code == 400, "No such user by login"

async def test_get_user_by_email_success(client: AsyncClient, database: Awaitable[Fixture], create_user_v1: Awaitable[Fixture]) -> None:
    params = {
        "user": "test_email@example.com",
    }
    
    response = await client.get('/api/v1/users/get', params=params)
    assert response.status_code == 200, "success fetched by email"

async def test_get_user_by_email_failed(client: AsyncClient, database: Awaitable[Fixture], create_user_v1: Awaitable[Fixture]) -> None:
    params = {
        "user": "test_email_failed@example.com",
    }
    
    response = await client.get('/api/v1/users/get', params=params)
    assert response.status_code == 400, "No such user by email"


async def test_get_user_by_id_success(client: AsyncClient, database: Awaitable[Fixture], created_user_data_v1: dict) -> None:
    
    user_id = created_user_data_v1['user']['id']

    params = {
        "user": user_id,
    }
    
    response = await client.get('/api/v1/users/get', params=params)
    assert response.status_code == 200, "success fetched by id"

async def test_get_user_by_id_failed(client: AsyncClient, database: Awaitable[Fixture], create_user_v1: Awaitable[Fixture]) -> None:

    params = {
        "user": 'failed_id',
    }
    
    response = await client.get('/api/v1/users/get', params=params)
    assert response.status_code == 400, "failed fetched by id"