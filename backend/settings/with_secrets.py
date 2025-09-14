"""
Settings class that integrates with AWS Secrets Manager
"""

from typing import Any, Dict, Optional

from .base import Settings
from .secrets_manager import SecretsManager


class SettingsWithSecrets:
    """Settings class that integrates with AWS Secrets Manager"""

    def __init__(self):
        self._base_settings = Settings()
        self._secrets_manager = SecretsManager(
            region_name=self._base_settings.aws_region
        )
        self._secrets_cache: Optional[Dict[str, Any]] = None
        self._initialized = False

    async def initialize(self):
        """Initialize settings with secrets from AWS Secrets Manager if enabled"""
        if self._initialized:
            return
        if (
            self._base_settings.use_secrets_manager
            or self._base_settings.environment == "production"
        ):
            print(
                f"Initializing settings with AWS Secrets Manager (secret: {self._base_settings.secrets_manager_secret_name})"
            )
            self._secrets_cache = await self._secrets_manager.get_secret(
                self._base_settings.secrets_manager_secret_name
            )
            if self._secrets_cache:
                print("Successfully loaded secrets from AWS Secrets Manager")
            else:
                print(
                    "Failed to load secrets from AWS Secrets Manager, using environment variables"
                )
        self._initialized = True

    def _get_value(self, key: str, default: Any = None) -> Any:
        """Get value from secrets cache first, then fall back to environment"""
        if self._secrets_cache and key in self._secrets_cache:
            return self._secrets_cache[key]
        return getattr(
            self._base_settings,
            key.lower().replace(
                "-",
                "_"),
            default)

    @property
    def environment(self) -> str:
        return self._get_value("environment", self._base_settings.environment)

    @property
    def debug(self) -> bool:
        debug_val = self._get_value("debug", self._base_settings.debug)
        if isinstance(debug_val, str):
            return debug_val.lower() in ("true", "1", "yes", "on")
        return bool(debug_val)

    @property
    def database_url(self) -> str:
        return self._get_value(
            "DATABASE_URL",
            self._base_settings.database_url)

    @property
    def secret_key(self) -> str:
        return self._get_value("SECRET_KEY", self._base_settings.secret_key)

    @property
    def algorithm(self) -> str:
        return self._get_value("ALGORITHM", self._base_settings.algorithm)

    @property
    def access_token_expire_minutes(self) -> int:
        val = self._get_value(
            "ACCESS_TOKEN_EXPIRE_MINUTES",
            self._base_settings.access_token_expire_minutes,
        )
        return int(val) if val else 30

    @property
    def google_client_id(self) -> str:
        return self._get_value(
            "GOOGLE_CLIENT_ID",
            self._base_settings.google_client_id)

    @property
    def google_client_secret(self) -> str:
        return self._get_value(
            "GOOGLE_CLIENT_SECRET", self._base_settings.google_client_secret
        )

    @property
    def nextauth_secret(self) -> str:
        return self._get_value(
            "NEXTAUTH_SECRET",
            self._base_settings.nextauth_secret)

    @property
    def nextauth_url(self) -> str:
        return self._get_value(
            "NEXTAUTH_URL",
            self._base_settings.nextauth_url)

    @property
    def api_base_url(self) -> str:
        return self._get_value(
            "API_BASE_URL",
            self._base_settings.api_base_url)

    @property
    def frontend_url(self) -> str:
        return self._get_value(
            "FRONTEND_URL",
            self._base_settings.frontend_url)

    @property
    def aws_region(self) -> str:
        return self._get_value("AWS_REGION", self._base_settings.aws_region)

    @property
    def gemini_api_key(self) -> str:
        return self._get_value(
            "GEMINI_API",
            self._base_settings.gemini_api_key)

    async def refresh_secrets(self):
        """Refresh secrets from AWS Secrets Manager"""
        self._secrets_manager.clear_cache()
        self._secrets_cache = None
        self._initialized = False
        await self.initialize()
