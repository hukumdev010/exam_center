import json
from fastapi import APIRouter, Header, HTTPException, Depends, Response
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_db
from .controller import AuthController
from .model import GoogleAuthURL, EmailPasswordLogin, UserRegister


router = APIRouter()
auth_controller = AuthController()


@router.get("/me")
async def get_current_user(authorization: str = Header(None)):
    """Get current user info from session"""
    if not authorization:
        raise HTTPException(
            status_code=401,
            detail="Authorization header required"
        )
    
    if not authorization.startswith("Bearer "):
        raise HTTPException(
            status_code=401,
            detail="Invalid authorization header format"
        )
    
    token = authorization.replace("Bearer ", "", 1)
    return await auth_controller.get_current_user(token)


@router.post("/logout")
async def logout(authorization: str = Header(None), response: Response = None):
    """Logout user by removing session and clearing cookies"""
    if not authorization:
        raise HTTPException(
            status_code=401,
            detail="Authorization header required"
        )
    
    if not authorization.startswith("Bearer "):
        raise HTTPException(
            status_code=401,
            detail="Invalid authorization header format"
        )
    
    token = authorization.replace("Bearer ", "", 1)
    result = await auth_controller.logout(token)
    
    # Clear auth cookies
    if response:
        response.delete_cookie("auth_token", path="/")
        response.delete_cookie("user_data", path="/")
    
    return result


@router.get("/google", response_model=GoogleAuthURL)
async def get_google_auth_url():
    """Get Google OAuth2 authorization URL"""
    return await auth_controller.get_google_auth_url()


@router.get("/callback/google")
async def google_callback(
    code: str = None,
    error: str = None,
    db: AsyncSession = Depends(get_db),
    response: Response = None
):
    """Handle Google OAuth2 callback"""
    callback_response = await auth_controller.google_callback(code, error, db)
    
    # If it's a successful response, set cookies before redirecting
    # Check if it's a RedirectResponse
    if hasattr(callback_response, 'url') and 'token=' in str(
        callback_response.url
         ):
        # Extract token from redirect URL
        import re
        match = re.search(r'token=([^&]+)', str(callback_response.url))
        if match:
            token = match.group(1)
            if response:
                response.set_cookie(
                    key="auth_token",
                    value=token,
                    max_age=7 * 24 * 60 * 60,  # 7 days
                    secure=True,
                    httponly=True,
                    samesite="lax"
                )
    
    return callback_response


@router.post("/logout/simple")
async def logout_simple():
    """Logout user (invalidate token)"""
    return await auth_controller.logout_simple()


@router.post("/login")
async def login_with_email_password(
    login_data: EmailPasswordLogin,
    db: AsyncSession = Depends(get_db),
    response: Response = None
):
    """Login with email and password"""
    login_response = await auth_controller.login_with_email_password(
        login_data,
        db
        )
    
    # Set auth token as HTTP cookie
    if response:
        response.set_cookie(
            key="auth_token",
            value=login_response.access_token,
            max_age=7 * 24 * 60 * 60,  # 7 days
            secure=True,  # Only send over HTTPS in production
            httponly=True,  # Prevent JavaScript access
            samesite="lax"  # CSRF protection
        )
        # Also set user data cookie for quick access
        user_json = json.dumps({
            "id": login_response.user.id,
            "email": login_response.user.email,
            "name": login_response.user.name,
            "image": login_response.user.image
        })
        response.set_cookie(
            key="user_data",
            value=user_json,
            max_age=7 * 24 * 60 * 60,  # 7 days
            secure=True,
            httponly=False,  # Allow JS access for user data
            samesite="lax"
        )
    
    return login_response


@router.post("/register")
async def register_user(
    user_data: UserRegister,
    db: AsyncSession = Depends(get_db),
    response: Response = None
):
    """Register a new user with email and password"""
    register_response = await auth_controller.register_user(user_data, db)
    
    # If registration was successful and we have a session token, set cookies
    if "access_token" in register_response and response:
        response.set_cookie(
            key="auth_token",
            value=register_response["access_token"],
            max_age=7 * 24 * 60 * 60,  # 7 days
            secure=True,
            httponly=True,
            samesite="lax"
        )
        
        # Set user data cookie
        if "user" in register_response:
            user_json = json.dumps(register_response["user"])
            response.set_cookie(
                key="user_data",
                value=user_json,
                max_age=7 * 24 * 60 * 60,  # 7 days
                secure=True,
                httponly=False,
                samesite="lax"
            )
    
    return register_response
