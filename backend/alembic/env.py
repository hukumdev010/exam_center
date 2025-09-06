from logging.config import fileConfig
from sqlalchemy import pool
from sqlalchemy.ext.asyncio import create_async_engine
from alembic import context
import asyncio
import os
import sys

# Add the parent directory to the path to import our models
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from models import Base
from settings import get_settings, get_settings_sync

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# Interpret the config file for Python logging.
# This line sets up loggers basically.
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# add your model's MetaData object here
# for 'autogenerate' support
target_metadata = Base.metadata

# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.


def get_url():
    """Get database URL from settings with Secrets Manager support"""
    try:
        # Try to get from environment first (for basic compatibility)
        env_url = os.getenv("DATABASE_URL")
        if env_url:
            return env_url
        
        # Fall back to sync settings (won't include secrets, but better than hardcoded)
        settings = get_settings_sync()
        return settings.database_url
    except Exception as e:
        print(f"Warning: Error getting database URL from settings: {e}")
        return "postgresql+asyncpg://postgres:postgres@localhost:5432/exam_center"


async def get_url_async():
    """Get database URL from settings with Secrets Manager support (async)"""
    try:
        settings = await get_settings()
        return settings.database_url
    except Exception as e:
        print(f"Warning: Error getting database URL from async settings: {e}")
        return get_url()


def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    url = get_url()
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


async def run_async_migrations():
    """In this scenario we need to create an Engine
    and associate a connection with the context.
    Uses async settings to get database URL with Secrets Manager support.
    """
    
    # Get database URL with secrets support
    database_url = await get_url_async()
    connectable = create_async_engine(database_url)

    async with connectable.connect() as connection:
        await connection.run_sync(do_run_migrations)

    await connectable.dispose()


def do_run_migrations(connection):
    context.configure(connection=connection, target_metadata=target_metadata)

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Run migrations in 'online' mode."""
    asyncio.run(run_async_migrations())


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
