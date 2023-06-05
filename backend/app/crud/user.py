import uuid
from functools import singledispatch

import schemas, models
from .utils.errors import PasswordsMismatchError
from database.core import AsyncSession
from services.auth.password import get_password_hash, verify_password


from sqlmodel import (
    select,
    update as update_query,
    delete as delete_query,
)
from sqlalchemy.sql.expression import Select, Update, Delete
from sqlalchemy.exc import IntegrityError
from pydantic import ValidationError, EmailStr

__all__ = [
    'get',
    'create',
    'delete',
    'update',
]


async def create(user: schemas.CreateUser | dict, _session: AsyncSession) -> schemas.UserWithID | None:
    if isinstance(user, schemas.CreateUser):
        data.email = data.email.lower()
        data = user.dict()
    else:
        data = user
    data['password'] = get_password_hash(data['password'])
    del data['confirm_password']
    try:
        user_data = models.User(**data)
        _session.add(user_data)
        await _session.flush()
        await _session.commit()
        await _session.refresh(user_data)
        return schemas.UserWithID(
            id=str(user_data.id),
            name=user_data.name,
            surname=user_data.surname,
            login=user_data.login,
            photo=user_data.photo,
            is_active=user_data.is_active,
        )
    except IntegrityError:
        return 

@singledispatch
async def get(user_id: uuid.UUID, _session: AsyncSession, private: bool = False) -> schemas.UserWithID | schemas.UserPrivate | None:
    
    qs = select(
        models.User.id,
        models.User.created_at,
        models.User.updated_at,
        models.User.login,
        models.User.name,
        models.User.surname,
        models.User.photo,
        models.User.email,
        models.User.is_active,
        models.User.role,
        models.User.password,
    ).where(models.User.id==user_id)

    return await _get_user(qs, _session, private)

@get.register
async def _(login: str, _session: AsyncSession, private: bool = False) -> schemas.UserWithID | schemas.UserPrivate | None:

    qs = select(
        models.User.id,
        models.User.created_at,
        models.User.updated_at,
        models.User.login,
        models.User.name,
        models.User.surname,
        models.User.photo,
        models.User.email,
        models.User.is_active,
        models.User.role,
        models.User.password,
    ).where(models.User.login==login)

    return await _get_user(qs, _session, private)

@get.register
async def _(email: EmailStr, _session: AsyncSession, private: bool = False) -> schemas.UserWithID | schemas.UserPrivate | None:

    qs = (select(
        models.User.id,
        models.User.created_at,
        models.User.updated_at,
        models.User.login,
        models.User.name,
        models.User.surname,
        models.User.photo,
        models.User.email,
        models.User.is_active,
        models.User.role,
        models.User.password,
    )
    .where(models.User.email==email)
    )

    return await _get_user(qs, _session, private)

@singledispatch  
async def delete(user_id: uuid.UUID, _session: AsyncSession) -> bool:

    qs = delete_query(models.User).where(models.User.id==user_id)
    return await _delete_user(qs, _session)

@delete.register
async def _(login: str, _session: AsyncSession) -> bool:

    qs = delete_query(models.User).where(models.User.login==login)
    return await _delete_user(qs, _session)

@delete.register
async def _(email: EmailStr, _session: AsyncSession) -> bool:

    qs = delete_query(models.User).where(models.User.email==email)
    return await _delete_user(qs, _session)

async def update(user: schemas.UpdateUser, _session: AsyncSession) -> bool:

    if isinstance(user.entity, uuid.UUID):
        user_qs = select(models.User).where(models.User.id==user.entity)
        update_qs = update_query(models.User).where(models.User.id==user.entity)
    elif isinstance(user.entity, EmailStr):
        user_qs = select(models.User).where(models.User.email==user.entity)
        update_qs = update_query(models.User).where(models.User.email==user.entity)
    else:
        user_qs = select(models.User).where(models.User.login==user.entity)
        update_qs = update_query(models.User).where(models.User.login==user.entity)

    user_in_db = (await _session.execute(user_qs)).one_or_none()
    if user_in_db:
        if 'password' in user.update:
            is_password_verified = verify_password(user.update['old_password'], user_in_db.User.password)
            if not is_password_verified:
                raise PasswordsMismatchError('Passwords mismatch')
            del user.update['old_password']
            user.update['password'] = get_password_hash(user.update['password'])
        
        return await _update_user(update_qs.values(**user.update), _session)
    
    return False

async def _get_user(qs: Select, _session: AsyncSession, private: bool) -> schemas.UserWithID | schemas.UserPrivate | None:
    try:
        result = (await _session.execute(qs)).one_or_none()
        if result:
            if not private:
                return schemas.UserWithID(
                    id=str(result.id),
                    name=result.name,
                    surname=result.surname,
                    login=result.login,
                    photo=result.photo,
                    is_active=result.is_active,
                )       
            return schemas.UserPrivate(
                id=str(result.id),
                name=result.name,
                surname=result.surname,
                login=result.login,
                photo=result.photo,
                email=result.email,
                role=result.role,
                is_active=result.is_active,
                password=result.password,
                created_at=result.created_at,
                updated_at=result.updated_at,
            )
    except ValidationError as e:
        print(e)

async def _delete_user(qs: Delete, _session: AsyncSession) -> bool:
    result = (await _session.execute(qs)).rowcount
    if result > 0:
        await _session.commit()

    return bool(result)

async def _update_user(qs: Update, _session: AsyncSession) -> bool:
    result = (await _session.execute(qs)).rowcount
    if result > 0:
        await _session.commit()

    return bool(result)

