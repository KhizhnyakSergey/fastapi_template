import uvicorn
from fastapi import FastAPI
from routers import router

from database import init_db

app = FastAPI()
app.include_router(router)

@app.on_event("startup")
async def start_up() -> None:
    await init_db()


def main() -> None:
    uvicorn.run("main:app", host="127.0.0.1", port=8001, reload=True)


if __name__ == '__main__':
    main()