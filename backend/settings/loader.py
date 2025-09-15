"""
Settings loader and global accessors
"""
import asyncio
from typing import Optional

from .base import Settings
from .with_secrets import SettingsWithSecrets

_settings_instance: Optional[SettingsWithSecrets] = None
_sync_settings_instance: Optional[Settings] = None


async def get_settings() -> SettingsWithSecrets:
    """Get the global settings instance, initializing if necessary"""
    global _settings_instance
    if _settings_instance is None:
        _settings_instance = SettingsWithSecrets()
        await _settings_instance.initialize()
    return _settings_instance


def get_settings_sync() -> Settings:
    """
    Get basic settings synchronously (for non-async contexts)
    This does not include secrets from AWS Secrets Manager
    Uses caching to avoid recreating Settings instances
    """
    global _sync_settings_instance
    if _sync_settings_instance is None:
        _sync_settings_instance = Settings()
    return _sync_settings_instance


def reset_settings_cache():
    """Reset settings cache - useful for testing/config changes"""
    global _settings_instance, _sync_settings_instance
    _settings_instance = None
    _sync_settings_instance = None


async def print_updated_env():
    settings = await get_settings()
    print(f"Loaded UPDATED settings for environment: {settings}")


# If you want to run this directly for testing:
if __name__ == "__main__":
    asyncio.run(print_updated_env())

