"""
Settings loader and global accessors
"""
import asyncio
from typing import Optional
from pathlib import Path

from dotenv import load_dotenv
from .base import Settings
from .with_secrets import SettingsWithSecrets

_settings_instance: Optional[SettingsWithSecrets] = None
_sync_settings_instance: Optional[Settings] = None
_env_file_last_modified: Optional[float] = None


def _get_env_file_path() -> Path:
    """Get the path to the .env file"""
    return Path(__file__).parent.parent / ".env"


def _should_reload_env() -> bool:
    """Check if the .env file has been modified since last load"""
    global _env_file_last_modified
    env_file = _get_env_file_path()
    
    if not env_file.exists():
        return False
    
    current_mtime = env_file.stat().st_mtime
    
    if (
        _env_file_last_modified is None
        or current_mtime > _env_file_last_modified
    ):
        _env_file_last_modified = current_mtime
        return True
    
    return False


def _reload_env_if_needed():
    """Reload environment variables if .env file has changed"""
    if _should_reload_env():
        # Clear cached environment variables by reloading .env
        env_file = _get_env_file_path()
        load_dotenv(env_file, override=True)
        # Clear settings cache to force reload
        reset_settings_cache()
        print(f"Environment variables reloaded from {env_file}")


async def get_settings() -> SettingsWithSecrets:
    """Get the global settings instance, initializing if necessary"""
    global _settings_instance
    
    # Check if we need to reload environment variables
    _reload_env_if_needed()
    
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
    
    # Check if we need to reload environment variables
    _reload_env_if_needed()
    
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

