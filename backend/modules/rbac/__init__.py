"""
RBAC (Role-Based Access Control) Module

This module provides comprehensive role-based access control functionality
for the Exam Center application including:

- Policy management (fine-grained permissions)
- Permission groups (collections of policies)
- Role definitions (collections of policies and permissions)
- User role assignments
- Access control decorators
- Administrative management APIs

The RBAC system uses a policy-based approach where:
1. Policies are attached to specific routes (e.g., readCategory, updateCategory)
2. Permissions group multiple related policies
3. Roles can contain both individual policies and permissions
4. Users can have multiple roles assigned
5. "student" role is assigned by default to new users
6. "superadmin" role has access to all policies

Components:
- service.py: Core business logic for RBAC operations
- decorators.py: FastAPI decorators for route protection
- controller.py: API request handlers
- route.py: REST API endpoints for RBAC management
- model.py: Pydantic models for API requests/responses
"""

from .service import RBACService
from .decorators import require_policies, require_read_category
from .controller import RBACController

__all__ = [
    "RBACService",
    "require_policies",
    "require_read_category",
    "RBACController"
]