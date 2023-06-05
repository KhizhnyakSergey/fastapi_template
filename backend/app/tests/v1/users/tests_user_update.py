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


async def test_update_user_login_success(client: AsyncClient, database: Awaitable[Fixture], create_user_v1: Awaitable[Fixture]) -> None:
    json_data = {
        "old_login": "test_login",
        "new_login": "test_new_login"
    }
    
    response = await client.put('/api/v1/users/update/login', json=json_data)
    assert response.status_code == 200, "success updated login"

async def test_update_user_login_failed(client: AsyncClient, database: Awaitable[Fixture], create_user_v1: Awaitable[Fixture]) -> None:
    json_data = {
        "old_login": "test_not_valid_login",
        "new_login": "test_new_login"
    }
    
    response = await client.put('/api/v1/users/update/login', json=json_data)
    assert response.status_code == 400, "login doesn't exists"


async def test_update_user_email_success(client: AsyncClient, database: Awaitable[Fixture], create_user_v1: Awaitable[Fixture]) -> None:
    json_data = {
        "old_email": "test_email@example.com",
        "new_email": "test_new_email@example.com"
    }
    
    response = await client.put('/api/v1/users/update/email', json=json_data)
    assert response.status_code == 200, "success updated email"


async def test_update_user_email_failed(client: AsyncClient, database: Awaitable[Fixture], create_user_v1: Awaitable[Fixture]) -> None:
    json_data = {
        "old_email": "test_failed_email@example.com",
        "new_email": "test_new_email@example.com"
    }
    
    response = await client.put('/api/v1/users/update/email', json=json_data)
    assert response.status_code == 400, "email doesn't exists"

async def test_update_user_password_by_login_success(client: AsyncClient, database: Awaitable[Fixture], create_user_v1: Awaitable[Fixture]) -> None:
    json_data = {
        "old_password": "test_password",
        "new_password": "test_new_password",
        "login": "test_login"
    }
    
    response = await client.put('/api/v1/users/update/password', json=json_data)
    assert response.status_code == 200, "success updated password by login"

async def test_update_user_password_by_login_failed(client: AsyncClient, database: Awaitable[Fixture], create_user_v1: Awaitable[Fixture]) -> None:
    json_data = {
        "old_password": "test_password1",
        "new_password": "test_new_password",
        "login": "test_login"
    }
    
    response = await client.put('/api/v1/users/update/password', json=json_data)
    assert response.status_code == 400, "failed updated password by login with incorrect old_password"

async def test_update_user_password_by_incorrect_login_failed(client: AsyncClient, database: Awaitable[Fixture], create_user_v1: Awaitable[Fixture]) -> None:
    json_data = {
        "old_password": "test_password",
        "new_password": "test_new_password",
        "login": "test_failed_login"
    }
    
    response = await client.put('/api/v1/users/update/password', json=json_data)
    assert response.status_code == 400, "failed updated password by incorrect login"


async def test_update_user_password_by_email_success(client: AsyncClient, database: Awaitable[Fixture], create_user_v1: Awaitable[Fixture]) -> None:
    json_data = {
        "old_password": "test_password",
        "new_password": "test_new_password",
        "email": "test_email@example.com"
    }
    
    response = await client.put('/api/v1/users/update/password', json=json_data)
    assert response.status_code == 200, "success updated password by email"

async def test_update_user_password_by_email_failed(client: AsyncClient, database: Awaitable[Fixture], create_user_v1: Awaitable[Fixture]) -> None:
    json_data = {
        "old_password": "test_password1",
        "new_password": "test_new_password",
        "email": "test_email@example.com"
    }
    
    response = await client.put('/api/v1/users/update/password', json=json_data)
    assert response.status_code == 400, "failed updated password by email with incorrect old_password"

async def test_update_user_password_by_incorrect_email_failed(client: AsyncClient, database: Awaitable[Fixture], create_user_v1: Awaitable[Fixture]) -> None:
    json_data = {
        "old_password": "test_password",
        "new_password": "test_new_password",
        "email": "test_failed_email@example.com"
    }
    
    response = await client.put('/api/v1/users/update/password', json=json_data)
    assert response.status_code == 400, "failed updated password by incorrect email"

async def test_update_user_password_by_id_success(client: AsyncClient, database: Awaitable[Fixture], created_user_data_v1: Awaitable[Fixture]) -> None:
    json_data = {
        "old_password": "test_password",
        "new_password": "test_new_password",
        "user_id": created_user_data_v1['user']['id']
    }
    
    response = await client.put('/api/v1/users/update/password', json=json_data)
    assert response.status_code == 200, "success updated password by id"

async def test_update_user_password_by_id_failed(client: AsyncClient, database: Awaitable[Fixture], created_user_data_v1: Awaitable[Fixture]) -> None:
    json_data = {
        "old_password": "test_password1",
        "new_password": "test_new_password",
        "user_id": created_user_data_v1['user']['id']
    }
    
    response = await client.put('/api/v1/users/update/password', json=json_data)
    assert response.status_code == 400, "failed updated password by id with incorrect old_password"

async def test_update_user_password_by_incorrect_id_failed(client: AsyncClient, database: Awaitable[Fixture], create_user_v1: Awaitable[Fixture]) -> None:
    json_data = {
        "old_password": "test_password",
        "new_password": "test_new_password",
        "user_id": "test_failed_id"
    }
    
    response = await client.put('/api/v1/users/update/password', json=json_data)
    assert response.status_code == 400, "failed updated password by incorrect id"