from .base import BaseResponse


class NoSuchUserResponse(BaseResponse):
    ...

class UserWasntCreatedResponse(BaseResponse):
    ...

class UserCreatedSuccessfullyResponse(BaseResponse):
    ...
    
class UserLoginUpdatedSuccessfully(BaseResponse):
    ...

class UserPasswordUpdatedSuccessfully(BaseResponse):
    ...

class UserPasswordMismatchResponse(BaseResponse):
    ...


class UserEmailUpdatedSuccessfully(BaseResponse):
    ...

class UserDeletedSuccessfully(BaseResponse):
    ...