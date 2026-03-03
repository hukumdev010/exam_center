# Export auth functions for backwards compatibility
from auth import get_optional_user, get_current_user, UserSession

__all__ = ["get_optional_user", "get_current_user", "UserSession"]