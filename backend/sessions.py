# Session storage for user authentication
# In production, this should be replaced with Redis or a database-backed
# session store

from typing import Any, Dict

# In-memory session storage (use Redis or database in production)
user_sessions: Dict[str, Dict[str, Any]] = {
    # Default mock session for testing - using existing user
    "mock_token": {
        "id": "112278074915864654062",
        "email": "basnethukum789@gmail.com",
        "name": "Hukum Basnet"
    }
}


def get_user_session(token: str) -> Dict[str, Any] | None:
    """Get user session by token"""
    return user_sessions.get(token)


def set_user_session(token: str, user_data: Dict[str, Any]) -> None:
    """Set user session data"""
    user_sessions[token] = user_data


def remove_user_session(token: str) -> None:
    """Remove user session"""
    if token in user_sessions:
        del user_sessions[token]
