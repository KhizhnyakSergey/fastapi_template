import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.exceptions import RequestValidationError

from routers import router
from database import init_db
from middlewares import errors
from settings import settings

app = FastAPI()

origins = [
    settings.client_origin
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)
app.add_exception_handler(RequestValidationError, errors.validation_exception_handler)
app.include_router(router)


@app.on_event("startup")
async def start_up() -> None:
    await init_db()


def main() -> None:
    uvicorn.run("main:app", host="127.0.0.1", port=8001, reload=True)


if __name__ == '__main__':
    main()