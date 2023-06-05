import uuid
from datetime import datetime

from pydantic import BaseModel, EmailStr, Field, constr



class UserBase(BaseModel):

    name: str
    surname: str
    login: constr(min_length=8, max_length=32, regex=r'^[0-9a-zA-Z_]+$')
    photo: str | None = None


class UserWithID(UserBase):

    id: str
    is_active: bool
    
class UserWithEmail(UserBase):

    email: EmailStr

class CreateUser(UserWithEmail):

    password: constr(min_length=8, max_length=32, regex=r'^[\w\S]+$')
    confirm_password: str


class UpdateUserLogin(BaseModel):

    old_login: str
    new_login: str

class UpdateUserPassword(BaseModel):

    old_password: str
    new_password: str

class UpdateUserEmail(BaseModel):
    
    old_email: EmailStr
    new_email: EmailStr

class UpdateUserPasswordWithLogin(UpdateUserPassword):

    login: str

class UpdateUserPasswordWithEmail(UpdateUserPassword):

    email: EmailStr

class UpdateUserPasswordWithId(UpdateUserPassword):

    user_id: str


class AuthBase(BaseModel):

    password: constr(min_length=8, max_length=32, regex=r'^[\w\S]+$')

class AuthenticateWithLogin(AuthBase):

    login: constr(min_length=8, max_length=32, regex=r'^[0-9a-zA-Z_]+$')

class AuthenticateWithEmail(AuthBase):

    email: EmailStr

class UserPrivate(UserWithID, UserWithEmail):
    
    role: str
    password: str
    created_at: datetime
    updated_at: datetime

class UpdateUser(BaseModel):
    
    entity:  str | EmailStr | uuid.UUID
    update: dict
