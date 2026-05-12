from collections.abc import AsyncGenerator
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase
from app.core.configs.settings import settings

class Base(DeclarativeBase):
    pass

# Import models here to register them with Base.metadata
from app.infrastructure.entity.auth import User

engine = create_async_engine(settings.DATABASE_URL)
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)

async def create_db_and_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session
