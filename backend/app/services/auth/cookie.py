import typing
from datetime import datetime

from pydantic import BaseModel


class Cookie(BaseModel):


    key: str
    value: str = ""
    max_age: typing.Optional[int] = None
    expires: typing.Optional[typing.Union[datetime, str, int]] = None
    path: str = "/"
    domain: typing.Optional[str] = None
    secure: bool = False
    httponly: bool = False
    samesite: typing.Optional[typing.Literal["lax", "strict", "none"]] = "lax"