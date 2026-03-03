"""
RBAC Decorators and Middleware

This module provides decorators and middleware for protecting API routes
with role-based access control policies.
"""
from functools import wraps
from typing import List, Optional, Union, Callable
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_db
from auth import get_current_user
from modules.rbac.service import RBACService


security = HTTPBearer()


def require_policies(
    policies: Union[str, List[str]], 
    require_all: bool = False
):
    """
    Decorator to require specific policies for route access.
    
    Args:
        policies: Single policy name or list of policy names
        require_all: If True, user must have ALL policies. If False, user must have ANY policy.
        
    Returns:
        Dependency function for FastAPI routes
        
    Example:
        @router.get("/categories", dependencies=[Depends(require_policies("readCategory"))])
        @router.post("/categories", dependencies=[Depends(require_policies("createCategory"))])
    """
    if isinstance(policies, str):
        policies = [policies]
    
    async def policy_dependency(
        current_user=Depends(get_current_user),
        db: AsyncSession = Depends(get_db)
    ):
        """FastAPI dependency that checks policies"""
        # Check policies using user id from session
        user_id = current_user.user.id
        
        if require_all:
            has_access = await RBACService.has_all_policies(
                user_id, policies, db
            )
        else:
            has_access = await RBACService.has_any_policy(
                user_id, policies, db
            )
        
        if not has_access:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail=f"Insufficient permissions. Required policies: {policies}"
            )
        
        return current_user
    
    return policy_dependency


def require_superadmin(func: Callable) -> Callable:
    """
    Decorator to require superadmin role for route access.
    
    Args:
        func: The route function to protect
        
    Returns:
        Protected route function
    """
    @wraps(func)
    async def wrapper(*args, **kwargs):
        # Extract dependencies from kwargs
        current_user = kwargs.get('current_user')
        db = kwargs.get('db')
        
        if not current_user or not db:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Authentication required"
            )
        
        # Check if user has superadmin role
        user_roles = await RBACService.get_user_roles(current_user.id, db)
        is_superadmin = any(role.name == "superadmin" for role in user_roles)
        
        if not is_superadmin:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Superadmin access required"
            )
        
        return await func(*args, **kwargs)
    
    return wrapper


async def get_rbac_user(
    current_user = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """
    Dependency to get current user with RBAC context.
    
    Args:
        current_user: Current authenticated user
        db: Database session
        
    Returns:
        User object with RBAC context
    """
    return {
        'user': current_user,
        'policies': await RBACService.get_user_policies(current_user.id, db),
        'roles': await RBACService.get_user_roles(current_user.id, db)
    }


class PolicyChecker:
    """
    Class for checking policies in route handlers without decorators.
    """
    
    def __init__(self, user_id: str, db: AsyncSession):
        self.user_id = user_id
        self.db = db
        self._cached_policies: Optional[set] = None
    
    async def has_policy(self, policy_name: str) -> bool:
        """Check if user has a specific policy."""
        if self._cached_policies is None:
            self._cached_policies = await RBACService.get_user_policies(
                self.user_id, self.db
            )
        return policy_name in self._cached_policies
    
    async def has_any_policy(self, policy_names: List[str]) -> bool:
        """Check if user has any of the specified policies."""
        if self._cached_policies is None:
            self._cached_policies = await RBACService.get_user_policies(
                self.user_id, self.db
            )
        return any(policy in self._cached_policies for policy in policy_names)
    
    async def has_all_policies(self, policy_names: List[str]) -> bool:
        """Check if user has all of the specified policies."""
        if self._cached_policies is None:
            self._cached_policies = await RBACService.get_user_policies(
                self.user_id, self.db
            )
        return all(policy in self._cached_policies for policy in policy_names)
    
    async def require_policy(self, policy_name: str) -> None:
        """Raise HTTPException if user doesn't have the required policy."""
        if not await self.has_policy(policy_name):
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail=f"Required policy not found: {policy_name}"
            )
    
    async def require_any_policy(self, policy_names: List[str]) -> None:
        """Raise HTTPException if user doesn't have any of the required policies."""
        if not await self.has_any_policy(policy_names):
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail=f"At least one required policy not found: {policy_names}"
            )
    
    async def require_all_policies(self, policy_names: List[str]) -> None:
        """Raise HTTPException if user doesn't have all required policies."""
        if not await self.has_all_policies(policy_names):
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail=f"All required policies not found: {policy_names}"
            )


def get_policy_checker(
    current_user=Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
) -> PolicyChecker:
    """
    Dependency to get a PolicyChecker instance for the current user.
    
    Args:
        current_user: Current authenticated user
        db: Database session
        
    Returns:
        PolicyChecker instance
    """
    return PolicyChecker(current_user.user.id, db)


# Convenience functions for common policies
def require_read_category():
    """Require readCategory policy"""
    return require_policies("readCategory")

def require_create_category():
    """Require createCategory policy"""
    return require_policies("createCategory")

def require_update_category():
    """Require updateCategory policy"""
    return require_policies("updateCategory")

def require_delete_category():
    """Require deleteCategory policy"""
    return require_policies("deleteCategory")

def require_read_certification():
    """Require readCertification policy"""
    return require_policies("readCertification")

def require_create_certification():
    """Require createCertification policy"""
    return require_policies("createCertification")

def require_update_certification():
    """Require updateCertification policy"""
    return require_policies("updateCertification")

def require_delete_certification():
    """Require deleteCertification policy"""
    return require_policies("deleteCertification")

def require_create_quiz_attempt():
    """Require createQuizAttempt policy"""
    return require_policies("createQuizAttempt")


def require_admin():
    """Require any admin-level policy"""
    return require_policies([
        "createCategory", "updateCategory", "deleteCategory",
        "createCertification", "updateCertification", "deleteCertification",
        "createUser", "updateUser", "deleteUser"
    ])