"""
AWS Secrets Manager client for retrieving secrets
"""

import asyncio
import json
from typing import Any, Dict, Optional

import boto3
from botocore.exceptions import ClientError, NoCredentialsError


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
                self._client = boto3.client(
                    "secretsmanager", region_name=self.region_name
                )
            except NoCredentialsError:
                print(
                    "Warning: AWS credentials not found. Secrets Manager functionality disabled."
                )
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
            loop = asyncio.get_event_loop()
            response = await loop.run_in_executor(
                None, lambda: self.client.get_secret_value(SecretId=secret_name)
            )
            secret_string = response.get("SecretString")
            if secret_string:
                secret_data = json.loads(secret_string)
                self._cache[secret_name] = secret_data
                return secret_data
        except ClientError as e:
            error_code = e.response["Error"]["Code"]
            if error_code == "ResourceNotFoundException":
                print(f"Secret {secret_name} not found in AWS Secrets Manager")
            elif error_code == "InvalidRequestException":
                print(f"Invalid request for secret {secret_name}")
            elif error_code == "InvalidParameterException":
                print(f"Invalid parameter for secret {secret_name}")
            else:
                print(f"Error retrieving secret {secret_name}: {e}")
        except Exception as e:
            print(f"Unexpected error retrieving secret {secret_name}: {e}")
        return None

    def clear_cache(self):
        """Clear the secrets cache"""
        self._cache.clear()
