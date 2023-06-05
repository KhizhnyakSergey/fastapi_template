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


async def test_create_user_success(client: AsyncClient, database: Awaitable[Fixture]) -> None:
    json_data = {
        "name": "test_name",
        "surname": "test_surname",
        "login": "test_login",
        "photo": "test_photo/path",
        "email": "test_email@example.com",
        "password": "test_password",
        "confirm_password": "test_password"
    }

    response = await client.post('/api/v1/auth/register', json=json_data)
    assert response.status_code == 201, "success created"
    assert isinstance(response.json().get('user'), dict), "user key exists"

async def test_create_user_failed_invalid_email(client: AsyncClient, database: Awaitable[Fixture]) -> None:
    json_data = {
        "name": "test_name",
        "surname": "test_surname",
        "login": "test_login",
        "photo": "test_photo/path",
        "email": "test_email_failed@@@@@example.com",
        "password": "test_password",
        "confirm_password": "test_password"
    }
    
    response = await client.post('/api/v1/auth/register', json=json_data)
    assert response.status_code == 422, "invalid email"
    email_error = None
    errors = response.json()['errors']
    assert len(errors) == 1, "valid length"
    for error in errors:
        if error['field']['body'] == 'email':
            email_error = error['field']['body']
    assert email_error == 'email', "email value exists"

async def test_create_user_failed_invalid_email_and_invalid_login(client: AsyncClient, database: Awaitable[Fixture]) -> None:
    json_data = {
        "name": "test_name",
        "surname": "test_surname",
        "login": "test_login_failed@@",
        "photo": "test_photo/path",
        "email": "test_email_failed@@@@@example.com",
        "password": "test_password",
        "confirm_password": "test_password"
    }
    
    response = await client.post('/api/v1/auth/register', json=json_data)
    assert response.status_code == 422, "invalid email and invalid login"
    email_error = None
    login_error = None
    errors = response.json()['errors']
    assert len(errors) == 2, "valid length"
    for error in errors:
        if error['field']['body'] == 'email':
            email_error = error['field']['body']
        if error['field']['body'] == 'login':
            login_error = error['field']['body']
        
    assert email_error == 'email' and login_error == 'login', "email and login value exists"

async def test_create_user_failed_invalid_login(client: AsyncClient, database: Awaitable[Fixture]) -> None:
    json_data = {
        "name": "test_name",
        "surname": "test_surname",
        "login": "test_login_failed@",
        "photo": "test_photo/path",
        "email": "test_email@example.com",
        "password": "test_password",
        "confirm_password": "test_password"
    }
    
    response = await client.post('/api/v1/auth/register', json=json_data)
    assert response.status_code == 422, "invalid login"
    login_error = None
    errors = response.json()['errors']
    assert len(errors) == 1, "valid length"
    for error in errors:
        if error['field']['body'] == 'login':
            login_error = error['field']['body']
    assert login_error == 'login', "login value exists"


async def test_create_user_failed_mismatch_passwords(client: AsyncClient, database: Awaitable[Fixture]) -> None:
    json_data = {
        "name": "test_name",
        "surname": "test_surname",
        "login": "test_login",
        "photo": "test_photo/path",
        "email": "test_email@example.com",
        "password": "test_password",
        "confirm_password": "test_failed_password"
    }
    
    response = await client.post('/api/v1/auth/register', json=json_data)
    assert response.status_code == 400, "passwords mismatch"
    assert response.json().get('message') == 'Passwords mismatch', "massage equals"

async def test_create_user_failed_user_already_exist(client: AsyncClient, database: Awaitable[Fixture], create_user_v1: Awaitable[Fixture] ) -> None:
    
    json_data = {
        "name": "test_name",
        "surname": "test_surname",
        "login": "test_login",
        "photo": "test_photo/path",
        "email": "test_email@example.com",
        "password": "test_password",
        "confirm_password": "test_password"
    }
    
    response = await client.post('/api/v1/auth/register', json=json_data)
    assert response.status_code == 409, "User exists"
    assert response.json().get('message') == 'User already exists', "user already exists"
