"""
Settings loader and global accessors
"""

from typing import Optional

from .base import Settings
from .with_secrets import SettingsWithSecrets

_settings_instance: Optional[SettingsWithSecrets] = None


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
    """
    return Settings()


settings = get_settings_sync()

print(f"Loaded settings for environment: {settings.environment}")
