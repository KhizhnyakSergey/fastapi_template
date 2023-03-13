from pydantic import BaseModel


class BaseResponse(BaseModel):
    status: int
    message: str

    def to_dict(self) -> dict:
        return self.__dict__
