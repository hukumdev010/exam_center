"""
Base application settings using Pydantic BaseSettings
"""

from typing import Optional

from pydantic import Field, validator
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application settings with AWS Secrets Manager fallback"""

    # Environment detection
    environment: str = Field(default="development", env="ENVIRONMENT")
    debug: bool = Field(default=True, env="DEBUG")
    # Database settings
    database_url: str = Field(
        default="postgresql+asyncpg://postgres:postgres@localhost:5432/exam_center",
        env="DATABASE_URL",
    )
    # JWT settings
    secret_key: str = Field(
        default="dev-secret-key-change-in-production", env="SECRET_KEY"
    )
    algorithm: str = Field(default="HS256", env="ALGORITHM")
    access_token_expire_minutes: int = Field(
        default=30, env="ACCESS_TOKEN_EXPIRE_MINUTES"
    )
    # OAuth settings
    google_client_id: str = Field(default="", env="GOOGLE_CLIENT_ID")
    google_client_secret: str = Field(default="", env="GOOGLE_CLIENT_SECRET")
    nextauth_secret: str = Field(default="", env="NEXTAUTH_SECRET")
    nextauth_url: str = Field(default="http://localhost:3000", env="NEXTAUTH_URL")
    # API settings
    api_base_url: str = Field(default="http://127.0.0.1:8000", env="API_BASE_URL")
    frontend_url: str = Field(default="http://127.0.0.1:3000", env="FRONTEND_URL")
    # AWS settings
    aws_region: str = Field(default="", env="AWS_REGION")
    aws_access_key_id: Optional[str] = Field(default=None, env="AWS_ACCESS_KEY_ID")
    aws_secret_access_key: Optional[str] = Field(
        default=None, env="AWS_SECRET_ACCESS_KEY"
    )
    # Secrets Manager settings
    use_secrets_manager: bool = Field(default=False, env="USE_SECRETS_MANAGER")
    secrets_manager_secret_name: str = Field(
        default="examCenterCredentials", env="SECRETS_MANAGER_SECRET_NAME"
    )
    # AI settings
    gemini_api_key: str = Field(default="", env="GEMINI_API")

    @validator("environment")
    def validate_environment(cls, v):
        allowed = ["development", "production", "testing"]
        if v not in allowed:
            raise ValueError(f"Environment must be one of {allowed}")
        return v

    @validator("use_secrets_manager", pre=True)
    def validate_use_secrets_manager(cls, v):
        if isinstance(v, str):
            return v.lower() in ("true", "1", "yes", "on")
        return bool(v)

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = False
        extra = "ignore"  # Ignore extra fields instead of raising validation error
