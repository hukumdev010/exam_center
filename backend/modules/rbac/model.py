"""
RBAC Management API Models

Pydantic models for RBAC management API endpoints.
"""
from typing import List, Optional, TypeVar, Generic
from pydantic import BaseModel
from datetime import datetime

T = TypeVar('T')


# Policy Models
class PolicyBase(BaseModel):
    name: str
    description: Optional[str] = None
    resource: str
    action: str


class PolicyCreate(PolicyBase):
    is_system: bool = False


class PolicyUpdate(BaseModel):
    description: Optional[str] = None


class Policy(PolicyBase):
    id: int
    is_system: bool
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


# Permission Models
class PermissionBase(BaseModel):
    name: str
    description: Optional[str] = None


class PermissionCreate(PermissionBase):
    policy_ids: List[int] = []
    is_system: bool = False


class PermissionUpdate(BaseModel):
    description: Optional[str] = None
    policy_ids: Optional[List[int]] = None


class Permission(PermissionBase):
    id: int
    is_system: bool
    created_at: datetime
    updated_at: datetime
    policies: List[Policy] = []

    class Config:
        from_attributes = True


# Role Models
class RoleBase(BaseModel):
    name: str
    description: Optional[str] = None


class RoleCreate(RoleBase):
    policy_ids: List[int] = []
    permission_ids: List[int] = []
    is_system: bool = False
    is_default: bool = False


class RoleUpdate(BaseModel):
    description: Optional[str] = None
    policy_ids: Optional[List[int]] = None
    permission_ids: Optional[List[int]] = None
    is_default: Optional[bool] = None


class Role(RoleBase):
    id: int
    is_system: bool
    is_default: bool
    created_at: datetime
    updated_at: datetime
    policies: List[Policy] = []
    permissions: List[Permission] = []

    class Config:
        from_attributes = True


# User Role Management Models
class UserRoleAssignment(BaseModel):
    user_id: str
    role_ids: List[int]


class UserWithRoles(BaseModel):
    id: str
    email: str
    name: Optional[str] = None
    roles: List[Role] = []

    class Config:
        from_attributes = True


# Response Models
class PolicyResponse(Policy):
    """Policy response model"""
    pass


class PermissionResponse(Permission):
    """Permission response model"""
    pass


class RoleResponse(Role):
    """Role response model"""
    pass


class UserRoleResponse(UserWithRoles):
    """User with roles response model"""
    pass


class PaginatedResponse(BaseModel, Generic[T]):
    """Generic paginated response model"""
    items: List[T]
    total: int
    skip: int = 0
    limit: int = 100


class PolicyListResponse(BaseModel):
    policies: List[Policy]
    total: int


class PermissionListResponse(BaseModel):
    permissions: List[Permission]
    total: int


class RoleListResponse(BaseModel):
    roles: List[Role]
    total: int


class UserListResponse(BaseModel):
    users: List[UserWithRoles]
    total: int