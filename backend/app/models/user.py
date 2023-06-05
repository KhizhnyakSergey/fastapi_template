from sqlmodel import Column, String, Boolean
from pydantic import EmailStr

from .base import UUIDBaseModel
from .base import Field




class User(UUIDBaseModel, table=True):
    __tablename__ = 'users'

    name: str = Field(
        sa_column=Column(
            String(length=50),
            nullable=False,
        )
    )
    surname: str = Field(
        sa_column=Column(
            String(length=50),
            nullable=False,
        )
    )
    login: str = Field(
        sa_column=String(length=50),
            default=None,
            nullable=False,
            unique=True,
            index=True,
        )
    email: EmailStr = Field(
        default=None,
        nullable=False,
        unique=True,
        index=True,
    )
    photo: str = Field(
        sa_column=Column(
            String(), 
            nullable=True,
            unique=False,
    ))
    role: str = Field(
        sa_column=Column(
            String(), 
            server_default='user',
            unique=False,
    ))
    is_active: bool = Field(
        sa_column=Column(
            Boolean(), 
            server_default='False',
            unique=False,
    ))
    password: str = Field(
        default=None,
        nullable=False,
    )

    def __repr__(self) -> str:
        return f'''{self.__class__.__name__}\
            (name={self.name}, \
            surname={self.surname}, \
            login={self.login}, \
            email={self.email}, \
            photo={self.photo}, \
            role={self.role}, \
            password={self.password})'''