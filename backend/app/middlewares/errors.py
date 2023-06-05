from fastapi import Request, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse


async def validation_exception_handler(request: Request, exc: RequestValidationError):
    error_messages = []
    for error in exc.errors():
        if len(error['loc']) > 1:
            match error['loc'][1]:
                case 'login':
                    error["msg"] = 'invalid login'
                case 'email':
                    error["msg"] = 'invalid email'
                case 'password':
                    error["msg"] = 'password length should be 8-32 symbols and not contents spaces'
            error_messages.append({"field": dict([tuple(error['loc'])]), "message": error["msg"]})
        else:
            error_messages.append({"field": error['loc'][0], "message": error["msg"]})
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content={'status': status.HTTP_422_UNPROCESSABLE_ENTITY, "errors": error_messages},
    )
