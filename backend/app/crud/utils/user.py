from pydantic import EmailStr, BaseModel, Field


class CreateUserConstructor(BaseModel):
    name: str
    surname: str
    login: str = Field(regex=r'^[0-9a-zA-Z_]{4,64}$')
    email: EmailStr
    password: str

    def to_dict(self) -> dict:
        return self.__dict__