from os import environ

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

from .models import Base


def get_engine():
    return create_async_engine(environ['POSTGRES_URL'], echo=True)


engine = get_engine()


async def clear_all():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


def get_session():
    return sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)
