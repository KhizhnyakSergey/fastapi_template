from .base import BaseResponse


class NoSuchUserResponse(BaseResponse):
    ...

class UserNotActivetedResponse(BaseResponse):
    ...

class MissingTokenResponse(BaseResponse):
    ...

class InvalidTokenResponse(BaseResponse):
    ...

class UserWasntCreatedResponse(BaseResponse):
    ...

class UserCreatedSuccessfullyResponse(BaseResponse):

    user: dict
    
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

class UserLoginSuccessfullyResponse(BaseResponse):
    
    token: str

class UserDoesNotExistsResponse(BaseResponse):
    ...

class UserDoesNotActivatedResponse(BaseResponse):
    ...
