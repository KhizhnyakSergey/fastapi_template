from pydantic import BaseModel, EmailStr, Field


class User(BaseModel):

    login: str
    name: str
    surname: str

    
class UserWithEmail(User):

    email: EmailStr

class UpdateUserBase(BaseModel):

    def to_dict(self) -> dict:
        return self.__dict__

class UpdateUserLogin(UpdateUserBase):

    old_login: str
    new_login: str

class UpdateUserPassword(UpdateUserBase):

    old_password: str
    new_password: str

class UpdateUserEmail(UpdateUserBase):
    
    old_email: EmailStr
    new_email: EmailStr

class UpdateUserPasswordWithLogin(UpdateUserPassword):

    login: str

class UpdateUserPasswordWithEmail(UpdateUserPassword):

    email: EmailStr



