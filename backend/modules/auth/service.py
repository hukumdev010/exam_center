import os
import uuid
from urllib.parse import urlencode
import hashlib

import httpx
from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from sessions import set_user_session
from modules.users.service import UserService
from models import User
from .model import GoogleAuthURL, EmailPasswordLogin, UserRegister


class AuthService:
    def __init__(self):
        self.google_client_id = os.getenv("GOOGLE_CLIENT_ID")
        self.google_client_secret = os.getenv("GOOGLE_CLIENT_SECRET")
        self.api_base_url = os.getenv('API_BASE_URL', 'http://localhost:10000')

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

    async def create_user_session(
        self, user_info: dict, db: AsyncSession
    ) -> str:
        """Create or update user in database and create a session"""
        # Create or update user in database
        user = await UserService.create_or_update_user(db, user_info)
        
        # Create a simple token (in production, use proper JWT)
        session_token = str(uuid.uuid4())

        # Store user session data
        user_data = {
            "id": user.id,
            "email": user.email,
            "name": user.name,
            "image": user.image,
        }

        # Store in session
        set_user_session(session_token, user_data)
        return session_token

    def hash_password(self, password: str) -> str:
        """Hash a password using SHA256"""
        return hashlib.sha256(password.encode()).hexdigest()

    def verify_password(self, password: str, password_hash: str) -> bool:
        """Verify a password against its hash"""
        return hashlib.sha256(password.encode()).hexdigest() == password_hash

    async def authenticate_user(self, email: str, password: str, db: AsyncSession) -> User:
        """Authenticate user with email and password"""
        result = await db.execute(select(User).filter(User.email == email))
        user = result.scalars().first()
        
        if not user or not user.password_hash:
            raise HTTPException(status_code=401, detail="Invalid email or password")
        
        if not self.verify_password(password, user.password_hash):
            raise HTTPException(status_code=401, detail="Invalid email or password")
        
        return user

    async def register_user(self, user_data: UserRegister, db: AsyncSession) -> User:
        """Register a new user with email and password"""
        # Check if user already exists
        result = await db.execute(select(User).filter(User.email == user_data.email))
        existing_user = result.scalars().first()
        
        if existing_user:
            raise HTTPException(status_code=400, detail="User with this email already exists")
        
        # Create new user
        user = User(
            id=str(uuid.uuid4()),
            name=user_data.name,
            email=user_data.email,
            password_hash=self.hash_password(user_data.password)
        )
        
        db.add(user)
        await db.commit()
        await db.refresh(user)
        
        return user

    async def login_with_email_password(self, login_data: EmailPasswordLogin, db: AsyncSession) -> str:
        """Login with email and password and create session"""
        user = await self.authenticate_user(login_data.email, login_data.password, db)
        
        # Create session
        session_token = str(uuid.uuid4())
        
        user_data = {
            "id": user.id,
            "email": user.email,
            "name": user.name,
            "image": user.image,
        }
        
        set_user_session(session_token, user_data)
        
        return session_token