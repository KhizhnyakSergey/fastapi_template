from pydantic import BaseModel


class BaseResponse(BaseModel):
    
    status: int | str
    message: str
