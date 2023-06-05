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


async def test_delete_user_by_login_success(client: AsyncClient, database: Awaitable[Fixture], create_user_v1: Awaitable[Fixture]) -> None:
    params = {
        "user": "test_login",
    }
    
    response = await client.delete('/api/v1/users/delete', params=params)
    assert response.status_code == 200, "success deleted user by login"

async def test_delete_user_by_login_failed(client: AsyncClient, database: Awaitable[Fixture], create_user_v1: Awaitable[Fixture]) -> None:
    params = {
        "user": "test_login_failed",
    }
    
    response = await client.delete('/api/v1/users/delete', params=params)
    assert response.status_code == 400, "failed deleted user by login"

async def test_delete_user_by_email_success(client: AsyncClient, database: Awaitable[Fixture], create_user_v1: Awaitable[Fixture]) -> None:
    params = {
        "user": "test_email@example.com",
    }
    
    response = await client.delete('/api/v1/users/delete', params=params)
    assert response.status_code == 200, "success deleted user by email"

async def test_delete_user_by_email_failed(client: AsyncClient, database: Awaitable[Fixture], create_user_v1: Awaitable[Fixture]) -> None:
    params = {
        "user": "test_email_failed@example.com",
    }
    
    response = await client.delete('/api/v1/users/delete', params=params)
    assert response.status_code == 400, "failed deleted user by email"

async def test_delete_user_by_id_success(client: AsyncClient, database: Awaitable[Fixture], created_user_data_v1: Awaitable[Fixture]) -> None:
    params = {
        "user": created_user_data_v1['user']['id'],
    }
    
    response = await client.delete('/api/v1/users/delete', params=params)
    assert response.status_code == 200, "success deleted user by id"

async def test_delete_user_by_id_failed(client: AsyncClient, database: Awaitable[Fixture], create_user_v1: Awaitable[Fixture]) -> None:
    params = {
        "user": 'test_failed_id',
    }
    
    response = await client.delete('/api/v1/users/delete', params=params)
    assert response.status_code == 400, "failed deleted user by id"