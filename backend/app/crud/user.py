import schemas, models
from .utils.user import CreateUserConstructor
from .utils.errors import PasswordsMismatchError
from database.core import AsyncSession
from services.auth.password import get_password_hash, verify_password


from sqlmodel import (
    select,
    update,
    delete,
)
from sqlalchemy.sql.expression import Select, Update, Delete
from sqlalchemy.exc import IntegrityError
from pydantic import ValidationError

__all__ = [
    'get_by_login',
    'get_by_email',
    'create',
    'delete_by_login',
    'delete_by_email',
]

async def _get_user(qs: Select, _session: AsyncSession) -> schemas.User | None:
    try:
        result = (await _session.execute(qs)).one_or_none()
        if result:
            return schemas.User(
                login=result.login,
                name=result.name,
                surname=result.surname,
            )
    except ValidationError:
        ...

    
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


async def get_by_login(login: str, _session: AsyncSession) -> schemas.User | None:
    qs = select(
        models.User.login,
        models.User.name,
        models.User.surname,
    ).where(models.User.login==login)

    return await _get_user(qs, _session)

async def get_by_email(email: str, _session: AsyncSession) -> schemas.User | None:
    qs = select(
        models.User.login,
        models.User.name,
        models.User.surname,
        models.User.email,
    ).where(models.User.email==email)

    return await _get_user(qs, _session)
    

async def create(user: CreateUserConstructor | dict, _session: AsyncSession) -> bool:

    if isinstance(user, CreateUserConstructor):
        data = user.to_dict()
    elif isinstance(user, dict):
        data = user
    else:
        raise TypeError(f'user param should be {type(CreateUserConstructor)} type or a dict')
    data['password'] = get_password_hash(data['password'])
    try:
        user_data = models.User(**data)
        _session.add(user_data)
        await _session.flush()
        if not user_data.id:
            return False
        await _session.commit()
        return True
    except IntegrityError:
        return False

async def delete_by_login(login: str, _session: AsyncSession) -> bool:
    qs = delete(models.User).where(models.User.login==login)
    return await _delete_user(qs=qs, _session=_session)

async def delete_by_email(email: str, _session: AsyncSession) -> bool:
    qs = delete(models.User).where(models.User.email==email)
    return await _delete_user(qs=qs, _session=_session)

async def update_login(old_login: str, new_login: str, _session: AsyncSession) -> bool:
    qs = update(models.User).where(models.User.login==old_login).values(login=new_login)
    return await _update_user(qs=qs, _session=_session)
    
async def update_email(old_email: str, new_email: str, _session: AsyncSession) -> bool:
    qs = update(models.User).where(models.User.email==old_email).values(email=new_email)
    return await _update_user(qs=qs, _session=_session)

async def update_password_by_login(login: str, old_password: str, new_password: str, _session: AsyncSession) -> bool:
    qs = select(models.User).where(models.User.login==login)
    user = (await _session.execute(qs)).one_or_none()
    if user:
        is_password_verified = verify_password(old_password, user.User.password)
        if not is_password_verified:
            raise PasswordsMismatchError('Passwords mismatch')
        
        qs = update(models.User).where(models.User.login==login).values(password=get_password_hash(new_password))
        return await _update_user(qs=qs, _session=_session)
    return False

async def update_password_by_email(email: str, old_password: str, new_password: str, _session: AsyncSession) -> bool:
    qs = select(models.User).where(models.User.email==email)
    user = (await _session.execute(qs)).one_or_none()
    if user:
        is_password_verified = verify_password(old_password, user.User.password)
        if not is_password_verified:
            raise PasswordsMismatchError('Passwords mismatch')
        
        qs = update(models.User).where(models.User.email==email).values(password=get_password_hash(new_password))
        return await _update_user(qs=qs, _session=_session)
    return False