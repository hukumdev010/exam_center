from fastapi import HTTPException, Depends, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy import select
from typing import Optional, Dict, Any
from pydantic import BaseModel
import os
import httpx
from database import get_db
from models import User as UserModel
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
        # For development, we'll accept a simple bearer token
        # In production, implement proper JWT verification
        token = credentials.credentials
        
        # For development - simple mock authentication
        # This is NOT secure and should be replaced with proper auth
        if token == "dev-user":
            # Mock user for development
            user_id = "dev-user-123"
            email = "dev@example.com"
            name = "Development User"
            picture = None
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid token format"
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
