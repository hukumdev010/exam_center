from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class GoogleAuthURL(BaseModel):
    auth_url: str


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"


class UserInfo(BaseModel):
    id: str
    email: str
    name: str
    image: str


class UserCreate(BaseModel):
    id: str
    name: Optional[str] = None
    email: str
    image: Optional[str] = None


class UserResponse(BaseModel):
    id: str
    name: Optional[str] = None
    email: str
    image: Optional[str] = None
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class LoginResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    user: UserInfo


class LogoutResponse(BaseModel):
    message: str


class EmailPasswordLogin(BaseModel):
    email: str
    password: str


class UserRegister(BaseModel):
    name: str
    email: str
    password: str