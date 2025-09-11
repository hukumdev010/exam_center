"""
Application settings with AWS Secrets Manager integration
"""
import os
import json
import asyncio
from typing import Optional, Dict, Any
from functools import lru_cache
import boto3
from botocore.exceptions import ClientError, NoCredentialsError
from pydantic_settings import BaseSettings
from pydantic import Field, validator


class Settings(BaseSettings):
    """Application settings with AWS Secrets Manager fallback"""
    
    # Environment detection
    environment: str = Field(default="development", env="ENVIRONMENT")
    debug: bool = Field(default=True, env="DEBUG")
    
    # Database settings
    database_url: str = Field(default="postgresql+asyncpg://postgres:postgres@localhost:5432/exam_center", env="DATABASE_URL")
    
    # JWT settings
    secret_key: str = Field(default="dev-secret-key-change-in-production", env="SECRET_KEY")
    algorithm: str = Field(default="HS256", env="ALGORITHM")
    access_token_expire_minutes: int = Field(default=30, env="ACCESS_TOKEN_EXPIRE_MINUTES")
    
    # OAuth settings
    google_client_id: str = Field(default="", env="GOOGLE_CLIENT_ID")
    google_client_secret: str = Field(default="", env="GOOGLE_CLIENT_SECRET")
    nextauth_secret: str = Field(default="", env="NEXTAUTH_SECRET")
    nextauth_url: str = Field(default="http://localhost:3000", env="NEXTAUTH_URL")
    
    # API settings
    api_base_url: str = Field(default="http://127.0.0.1:8000", env="API_BASE_URL")
    frontend_url: str = Field(default="http://127.0.0.1:3000", env="FRONTEND_URL")
    
    # AWS settings
    aws_region: str = Field(default="us-east-1", env="AWS_REGION")
    aws_access_key_id: Optional[str] = Field(default=None, env="AWS_ACCESS_KEY_ID")
    aws_secret_access_key: Optional[str] = Field(default=None, env="AWS_SECRET_ACCESS_KEY")
    
    # Secrets Manager settings
    use_secrets_manager: bool = Field(default=False, env="USE_SECRETS_MANAGER")
    secrets_manager_secret_name: str = Field(default="examCenterCredentials", env="SECRETS_MANAGER_SECRET_NAME")
    
    # AI settings
    gemini_api_key: str = Field(default="", env="GEMINI_API")
    
    @validator('environment')
    def validate_environment(cls, v):
        allowed = ['development', 'production', 'testing']
        if v not in allowed:
            raise ValueError(f'Environment must be one of {allowed}')
        return v
    
    @validator('use_secrets_manager', pre=True)
    def validate_use_secrets_manager(cls, v):
        if isinstance(v, str):
            return v.lower() in ('true', '1', 'yes', 'on')
        return bool(v)
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = False
        extra = "ignore"  # Ignore extra fields instead of raising validation error


class SecretsManager:
    """AWS Secrets Manager client for retrieving secrets"""
    
    def __init__(self, region_name: str = "us-east-1"):
        self.region_name = region_name
        self._client = None
        self._cache: Dict[str, Any] = {}
    
    @property
    def client(self):
        """Lazy initialization of boto3 client"""
        if self._client is None:
            try:
                self._client = boto3.client('secretsmanager', region_name=self.region_name)
            except NoCredentialsError:
                print("Warning: AWS credentials not found. Secrets Manager functionality disabled.")
                return None
        return self._client
    
    async def get_secret(self, secret_name: str) -> Optional[Dict[str, Any]]:
        """
        Retrieve secret from AWS Secrets Manager with caching
        """
        # Check cache first
        if secret_name in self._cache:
            return self._cache[secret_name]
        
        if not self.client:
            return None
        
        try:
            # Run the synchronous boto3 call in a thread pool
            loop = asyncio.get_event_loop()
            response = await loop.run_in_executor(
                None, 
                lambda: self.client.get_secret_value(SecretId=secret_name)
            )
            
            # Parse the secret
            secret_string = response.get('SecretString')
            if secret_string:
                secret_data = json.loads(secret_string)
                self._cache[secret_name] = secret_data
                return secret_data
                
        except ClientError as e:
            error_code = e.response['Error']['Code']
            if error_code == 'ResourceNotFoundException':
                print(f"Secret {secret_name} not found in AWS Secrets Manager")
            elif error_code == 'InvalidRequestException':
                print(f"Invalid request for secret {secret_name}")
            elif error_code == 'InvalidParameterException':
                print(f"Invalid parameter for secret {secret_name}")
            else:
                print(f"Error retrieving secret {secret_name}: {e}")
        except Exception as e:
            print(f"Unexpected error retrieving secret {secret_name}: {e}")
        
        return None
    
    def clear_cache(self):
        """Clear the secrets cache"""
        self._cache.clear()


class SettingsWithSecrets:
    """Settings class that integrates with AWS Secrets Manager"""
    
    def __init__(self):
        self._base_settings = Settings()
        self._secrets_manager = SecretsManager(region_name=self._base_settings.aws_region)
        self._secrets_cache: Optional[Dict[str, Any]] = None
        self._initialized = False
    
    async def initialize(self):
        """Initialize settings with secrets from AWS Secrets Manager if enabled"""
        if self._initialized:
            return
        
        if self._base_settings.use_secrets_manager or self._base_settings.environment == "production":
            print(f"Initializing settings with AWS Secrets Manager (secret: {self._base_settings.secrets_manager_secret_name})")
            self._secrets_cache = await self._secrets_manager.get_secret(
                self._base_settings.secrets_manager_secret_name
            )
            if self._secrets_cache:
                print("Successfully loaded secrets from AWS Secrets Manager")
            else:
                print("Failed to load secrets from AWS Secrets Manager, using environment variables")
        
        self._initialized = True
    
    def _get_value(self, key: str, default: Any = None) -> Any:
        """Get value from secrets cache first, then fall back to environment"""
        # First try secrets cache
        if self._secrets_cache and key in self._secrets_cache:
            return self._secrets_cache[key]
        
        # Then try base settings (which include environment variables)
        return getattr(self._base_settings, key.lower().replace('-', '_'), default)
    
    @property
    def environment(self) -> str:
        return self._get_value('environment', self._base_settings.environment)
    
    @property
    def debug(self) -> bool:
        debug_val = self._get_value('debug', self._base_settings.debug)
        if isinstance(debug_val, str):
            return debug_val.lower() in ('true', '1', 'yes', 'on')
        return bool(debug_val)
    
    @property
    def database_url(self) -> str:
        return self._get_value('DATABASE_URL', self._base_settings.database_url)
    
    @property
    def secret_key(self) -> str:
        return self._get_value('SECRET_KEY', self._base_settings.secret_key)
    
    @property
    def algorithm(self) -> str:
        return self._get_value('ALGORITHM', self._base_settings.algorithm)
    
    @property
    def access_token_expire_minutes(self) -> int:
        val = self._get_value('ACCESS_TOKEN_EXPIRE_MINUTES', self._base_settings.access_token_expire_minutes)
        return int(val) if val else 30
    
    @property
    def google_client_id(self) -> str:
        return self._get_value('GOOGLE_CLIENT_ID', self._base_settings.google_client_id)
    
    @property
    def google_client_secret(self) -> str:
        return self._get_value('GOOGLE_CLIENT_SECRET', self._base_settings.google_client_secret)
    
    @property
    def nextauth_secret(self) -> str:
        return self._get_value('NEXTAUTH_SECRET', self._base_settings.nextauth_secret)
    
    @property
    def nextauth_url(self) -> str:
        return self._get_value('NEXTAUTH_URL', self._base_settings.nextauth_url)
    
    @property
    def api_base_url(self) -> str:
        return self._get_value('API_BASE_URL', self._base_settings.api_base_url)
    
    @property
    def frontend_url(self) -> str:
        return self._get_value('FRONTEND_URL', self._base_settings.frontend_url)
    
    @property
    def aws_region(self) -> str:
        return self._get_value('AWS_REGION', self._base_settings.aws_region)
    
    @property
    def gemini_api_key(self) -> str:
        return self._get_value('GEMINI_API', self._base_settings.gemini_api_key)
    
    async def refresh_secrets(self):
        """Refresh secrets from AWS Secrets Manager"""
        self._secrets_manager.clear_cache()
        self._secrets_cache = None
        self._initialized = False
        await self.initialize()


# Global settings instance
_settings_instance: Optional[SettingsWithSecrets] = None


async def get_settings() -> SettingsWithSecrets:
    """Get the global settings instance, initializing if necessary"""
    global _settings_instance
    
    if _settings_instance is None:
        _settings_instance = SettingsWithSecrets()
        await _settings_instance.initialize()
    
    return _settings_instance


@lru_cache()
def get_settings_sync() -> Settings:
    """
    Get basic settings synchronously (for non-async contexts)
    This does not include secrets from AWS Secrets Manager
    """
    return Settings()
