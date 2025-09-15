import os
import uuid
from urllib.parse import urlencode

import httpx
from fastapi import HTTPException
from pydantic import BaseModel

from sessions import set_user_session


class GoogleAuthURL(BaseModel):
    auth_url: str


class AuthService:
    def __init__(self):
        self.google_client_id = os.getenv("GOOGLE_CLIENT_ID")
        self.google_client_secret = os.getenv("GOOGLE_CLIENT_SECRET")
        self.api_base_url = os.getenv('API_BASE_URL', 'http://localhost:8000')

    def get_google_auth_url(self) -> GoogleAuthURL:
        """Generate Google OAuth2 authorization URL"""
        params = {
            "client_id": self.google_client_id,
            "redirect_uri": f"{self.api_base_url}/api/auth/callback/google",
            "response_type": "code",
            "scope": "openid email profile",
            "access_type": "offline",
            "prompt": "consent",
        }

        auth_url = (
            f"https://accounts.google.com/o/oauth2/v2/auth?"
            f"{urlencode(params)}"
        )
        return GoogleAuthURL(auth_url=auth_url)

    async def exchange_code_for_token(self, code: str) -> str:
        """Exchange authorization code for access token"""
        token_url = "https://oauth2.googleapis.com/token"
        token_data = {
            "client_id": self.google_client_id,
            "client_secret": self.google_client_secret,
            "code": code,
            "grant_type": "authorization_code",
            "redirect_uri": f"{self.api_base_url}/api/auth/callback/google",
        }

        async with httpx.AsyncClient() as client:
            token_response = await client.post(token_url, data=token_data)

        if token_response.status_code != 200:
            raise HTTPException(
                status_code=400, detail="Failed to exchange code for token"
            )

        tokens = token_response.json()
        access_token = tokens.get("access_token")

        if not access_token:
            raise HTTPException(
                status_code=400,
                detail="No access token received")

        return access_token

    async def get_user_info(self, access_token: str) -> dict:
        """Get user information from Google using access token"""
        async with httpx.AsyncClient() as client:
            user_response = await client.get(
                "https://www.googleapis.com/oauth2/v2/userinfo",
                headers={"Authorization": f"Bearer {access_token}"},
            )

        if user_response.status_code != 200:
            raise HTTPException(
                status_code=400,
                detail="Failed to get user info")

        return user_response.json()

    async def create_user_session(self, user_info: dict) -> str:
        """Create a user session and return session token"""
        # Create a simple token (in production, use proper JWT)
        session_token = str(uuid.uuid4())

        # Store user session (in production, use proper session storage)
        user_data = {
            "id": user_info.get("id"),
            "email": user_info.get("email"),
            "name": user_info.get("name"),
            "image": user_info.get("picture"),
        }

        # Store in session
        set_user_session(session_token, user_data)
        return session_token

