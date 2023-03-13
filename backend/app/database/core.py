import os
from typing import AsyncGenerator

from sqlmodel import SQLModel
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio.session import AsyncSession

from settings import settings, module


async_engine = create_async_engine(
    url=settings.pg_dsn,
    echo=settings.pg_echo,
    future=settings.pg_future
)

async def init_db() -> None:
    async with async_engine.begin() as connection:
        match module:
            case 'development':
                # await connection.run_sync(SQLModel.metadata.drop_all)
                await connection.run_sync(SQLModel.metadata.create_all)
            case 'test':
                await connection.run_sync(SQLModel.metadata.drop_all)
                await connection.run_sync(SQLModel.metadata.create_all)
      

async def get_session() -> AsyncGenerator[AsyncSession, None]:
    async with AsyncSession(bind=async_engine) as session:
        yield session