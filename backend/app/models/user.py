from sqlmodel import Column, String
from pydantic import EmailStr

from .base import BaseModel
from .base import Field


class User(BaseModel, table=True):
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
    email: str = Field(
        default=None,
        nullable=False,
        unique=True,
        index=True,
    )
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
            password={self.password})'''