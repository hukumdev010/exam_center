from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from models import Base
import os
from typing import AsyncGenerator
from settings import get_settings, get_settings_sync

# For synchronous contexts, use basic settings
_sync_settings = get_settings_sync()
DATABASE_URL = _sync_settings.database_url

# Create async engine with initial URL (will be updated in init_db)
engine = create_async_engine(DATABASE_URL, echo=False)

# Create async session factory
AsyncSessionLocal = sessionmaker(
    engine, class_=AsyncSession, expire_on_commit=False
)

async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with AsyncSessionLocal() as session:
        try:
            yield session
        finally:
            await session.close()

async def init_db():
    """Initialize database tables with settings from Secrets Manager"""
    global engine
    
    # Get settings with secrets
    settings = await get_settings()
    
    # Recreate engine with potentially updated database URL from secrets
    if settings.database_url != DATABASE_URL:
        await engine.dispose()
        engine = create_async_engine(settings.database_url, echo=settings.debug)
        print(f"Database engine updated with URL from settings")
    
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
