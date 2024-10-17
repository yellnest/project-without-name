from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, DeclarativeBase

from app.config import settings

# DATABASE_URL = f'postgresql+asyncpg://{settings.DB_USER}:{settings.DB_PASS}@{settings.DB_HOST}:{settings.DB_PORT}/{settings.DB_NAME}'

engine = create_async_engine(settings.get_db_url())

async_session_marker = sessionmaker(Engine=engine, class_=AsyncSession, expire_on_commit=False)


class Base(DeclarativeBase):
    pass
