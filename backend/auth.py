from fastapi import HTTPException, Depends, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy import select
from typing import Optional, Dict, Any
from pydantic import BaseModel
import os
import httpx
from database import get_db
from models import User as UserModel
from sessions import get_user_session
from settings import get_settings
from uuid import uuid4

security = HTTPBearer()

class User(BaseModel):
    id: str
    email: str
    name: Optional[str] = None
    image: Optional[str] = None

    class Config:
        from_attributes = True

class UserSession(BaseModel):
    user: User

async def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security),
    db = Depends(get_db)
) -> UserSession:
    """Get current authenticated user"""
    try:
        token = credentials.credentials
        
        # First check if it's a session token from Google OAuth
        user_data = get_user_session(token)
        if user_data:
            user_id = user_data.get("id")
            email = user_data.get("email")
            name = user_data.get("name")
            picture = user_data.get("image")
        elif token == "dev-user":
            # Mock user for development
            user_id = "dev-user-123"
            email = "dev@example.com"
            name = "Development User"
            picture = None
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid authentication token"
            )
        
        # Get or create user in database
        stmt = select(UserModel).where(UserModel.email == email)
        result = await db.execute(stmt)
        user = result.scalar_one_or_none()
        
        if user:
            # Update user info
            user.name = name
            user.image = picture
        else:
            # Create new user
            user = UserModel(
                id=user_id,
                email=email,
                name=name,
                image=picture
            )
            db.add(user)
        
        await db.commit()
        await db.refresh(user)
        
        return UserSession(
            user=User(
                id=user.id,
                email=user.email,
                name=user.name,
                image=user.image
            )
        )
        
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials"
        )

async def get_optional_user(
    credentials: Optional[HTTPAuthorizationCredentials] = Depends(security),
    db = Depends(get_db)
) -> Optional[UserSession]:
    """Get current user if authenticated, otherwise None"""
    if not credentials:
        return None
    try:
        return await get_current_user(credentials, db)
    except HTTPException:
        return None
