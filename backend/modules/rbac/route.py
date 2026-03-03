"""
RBAC Management Routes

Admin API endpoints for managing roles, permissions, policies,
and user assignments.
"""
from typing import List, Optional
from fastapi import APIRouter, Depends, Query, status
from sqlalchemy.ext.asyncio import AsyncSession

from auth import get_current_user
from database import get_db
from models import User
from modules.rbac.decorators import require_policies
from .controller import RBACController
from .model import (
    PolicyBase, PolicyCreate, PolicyUpdate, PolicyResponse,
    PermissionCreate, PermissionUpdate, PermissionResponse,
    RoleCreate, RoleUpdate, RoleResponse,
    UserRoleAssignment, UserRoleResponse, PaginatedResponse
)

router = APIRouter(prefix="/rbac")


# Policy Management
@router.get("/policies", response_model=PaginatedResponse[PolicyResponse])
async def list_policies(
    skip: int = Query(0, ge=0, description="Number of records to skip"),
    limit: int = Query(
        100,
        ge=1,
        le=1000,
        description=(
            "Number of records to return"
        )
    ),
    search: Optional[str] = Query(
        None,
        description="Search in policy name/description"
    ),
    current_user: User = Depends(require_policies(["managePolicies"])),
    db: AsyncSession = Depends(get_db)
):
    """List all policies with pagination and search"""
    policies, total = await RBACController.list_policies(
        skip=skip, limit=limit, search=search, db=db
    )
    
    return PaginatedResponse(
        items=[PolicyResponse.model_validate(policy) for policy in policies],
        total=total,
        skip=skip,
        limit=limit
    )


@router.get("/policies/{policy_id}", response_model=PolicyResponse)
async def get_policy(
    policy_id: int,
    current_user: User = Depends(require_policies(["managePolicies"])),
    db: AsyncSession = Depends(get_db)
):
    """Get policy by ID"""
    policy = await RBACController.get_policy(policy_id, db)
    return PolicyResponse.model_validate(policy)


@router.post(
    "/policies",
    response_model=PolicyResponse,
    status_code=status.HTTP_201_CREATED
)
async def create_policy(
    policy_data: PolicyCreate,
    current_user: User = Depends(require_policies(["managePolicies"])),
    db: AsyncSession = Depends(get_db)
):
    """Create a new policy"""
    policy = await RBACController.create_policy(policy_data, db)
    return PolicyResponse.model_validate(policy)


@router.put("/policies/{policy_id}", response_model=PolicyResponse)
async def update_policy(
    policy_id: int,
    policy_data: PolicyUpdate,
    current_user: User = Depends(require_policies(["managePolicies"])),
    db: AsyncSession = Depends(get_db)
):
    """Update policy"""
    policy = await RBACController.update_policy(policy_id, policy_data, db)
    return PolicyResponse.model_validate(policy)


@router.delete("/policies/{policy_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_policy(
    policy_id: int,
    current_user: User = Depends(require_policies(["managePolicies"])),
    db: AsyncSession = Depends(get_db)
):
    """Delete policy"""
    await RBACController.delete_policy(policy_id, db)
    return None


# Permission Management
@router.get(
    "/permissions",
    response_model=PaginatedResponse[PermissionResponse]
)
async def list_permissions(
    skip: int = Query(0, ge=0, description="Number of records to skip"),
    limit: int = Query(
        100,
        ge=1,
        le=1000,
        description="Number of records to return"
    ),
    search: Optional[str] = Query(
        None, description="Search in permission name/description"
    ),
    current_user: User = Depends(require_policies(["managePermissions"])),
    db: AsyncSession = Depends(get_db)
):
    """List all permissions with pagination and search"""
    permissions, total = await RBACController.list_permissions(
        skip=skip, limit=limit, search=search, db=db
    )
    
    return PaginatedResponse(
        items=[
            PermissionResponse.model_validate(permission)
            for permission in permissions
        ],
        total=total,
        skip=skip,
        limit=limit
    )


@router.get("/permissions/{permission_id}", response_model=PermissionResponse)
async def get_permission(
    permission_id: int,
    current_user: User = Depends(require_policies(["managePermissions"])),
    db: AsyncSession = Depends(get_db)
):
    """Get permission by ID"""
    permission = await RBACController.get_permission(permission_id, db)
    return PermissionResponse.model_validate(permission)


@router.post(
    "/permissions",
    response_model=PermissionResponse,
    status_code=status.HTTP_201_CREATED
)
async def create_permission(
    permission_data: PermissionCreate,
    current_user: User = Depends(require_policies(["managePermissions"])),
    db: AsyncSession = Depends(get_db)
):
    """Create a new permission"""
    permission = await RBACController.create_permission(permission_data, db)
    return PermissionResponse.model_validate(permission)


@router.put("/permissions/{permission_id}", response_model=PermissionResponse)
async def update_permission(
    permission_id: int,
    permission_data: PermissionUpdate,
    current_user: User = Depends(require_policies(["managePermissions"])),
    db: AsyncSession = Depends(get_db)
):
    """Update permission"""
    permission = await RBACController.update_permission(
        permission_id,
        permission_data,
        db
    )
    return PermissionResponse.model_validate(permission)


@router.delete(
    "/permissions/{permission_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
async def delete_permission(
    permission_id: int,
    current_user: User = Depends(require_policies(["managePermissions"])),
    db: AsyncSession = Depends(get_db)
):
    """Delete permission"""
    await RBACController.delete_permission(permission_id, db)
    return None


# Role Management
@router.get("/roles", response_model=PaginatedResponse[RoleResponse])
async def list_roles(
    skip: int = Query(0, ge=0, description="Number of records to skip"),
    limit: int = Query(
        100, ge=1, le=1000, description="Number of records to return"
    ),
    search: Optional[str] = Query(
        None, description="Search in role name/description"
    ),
    current_user: User = Depends(require_policies(["manageRoles"])),
    db: AsyncSession = Depends(get_db)
):
    """List all roles with pagination and search"""
    roles, total = await RBACController.list_roles(
        skip=skip, limit=limit, search=search, db=db
    )
    
    return PaginatedResponse(
        items=[RoleResponse.model_validate(role) for role in roles],
        total=total,
        skip=skip,
        limit=limit
    )


@router.get("/roles/{role_id}", response_model=RoleResponse)
async def get_role(
    role_id: int,
    current_user: User = Depends(require_policies(["manageRoles"])),
    db: AsyncSession = Depends(get_db)
):
    """Get role by ID"""
    role = await RBACController.get_role(role_id, db)
    return RoleResponse.model_validate(role)


@router.post(
    "/roles", response_model=RoleResponse, status_code=status.HTTP_201_CREATED
)
async def create_role(
    role_data: RoleCreate,
    current_user: User = Depends(require_policies(["manageRoles"])),
    db: AsyncSession = Depends(get_db)
):
    """Create a new role"""
    role = await RBACController.create_role(role_data, db)
    return RoleResponse.model_validate(role)


@router.put("/roles/{role_id}", response_model=RoleResponse)
async def update_role(
    role_id: int,
    role_data: RoleUpdate,
    current_user: User = Depends(require_policies(["manageRoles"])),
    db: AsyncSession = Depends(get_db)
):
    """Update role"""
    role = await RBACController.update_role(role_id, role_data, db)
    return RoleResponse.model_validate(role)


@router.delete("/roles/{role_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_role(
    role_id: int,
    current_user: User = Depends(require_policies(["manageRoles"])),
    db: AsyncSession = Depends(get_db)
):
    """Delete role"""
    await RBACController.delete_role(role_id, db)
    return None


# User Role Management
@router.get("/users", response_model=PaginatedResponse[UserRoleResponse])
async def list_users_with_roles(
    skip: int = Query(0, ge=0, description="Number of records to skip"),
    limit: int = Query(
        100, ge=1, le=1000, description="Number of records to return"
    ),
    search: Optional[str] = Query(
        None, description="Search in user email/name"
    ),
    current_user: User = Depends(require_policies(["manageUserRoles"])),
    db: AsyncSession = Depends(get_db)
):
    """List users with their roles"""
    users, total = await RBACController.list_users_with_roles(
        skip=skip, limit=limit, search=search, db=db
    )
    
    return PaginatedResponse(
        items=[UserRoleResponse.model_validate(user) for user in users],
        total=total,
        skip=skip,
        limit=limit
    )


@router.get("/users/{user_id}/roles", response_model=UserRoleResponse)
async def get_user_roles(
    user_id: str,
    current_user: User = Depends(require_policies(["manageUserRoles"])),
    db: AsyncSession = Depends(get_db)
):
    """Get user roles by user ID"""
    user = await RBACController.get_user_roles(user_id, db)
    return UserRoleResponse.model_validate(user)


@router.post("/users/assign-roles", response_model=UserRoleResponse)
async def assign_roles_to_user(
    assignment: UserRoleAssignment,
    current_user: User = Depends(require_policies(["manageUserRoles"])),
    db: AsyncSession = Depends(get_db)
):
    """Assign roles to user"""
    user = await RBACController.assign_roles_to_user(assignment, db)
    return UserRoleResponse.model_validate(user)


@router.delete(
        "/users/{user_id}/roles/{role_id}", response_model=UserRoleResponse
        )
async def remove_role_from_user(
    user_id: str,
    role_id: int,
    current_user: User = Depends(require_policies(["manageUserRoles"])),
    db: AsyncSession = Depends(get_db)
):
    """Remove specific role from user"""
    user = await RBACController.remove_role_from_user(user_id, role_id, db)
    return UserRoleResponse.model_validate(user)


# Utility endpoints
@router.get("/my-policies", response_model=List[PolicyBase])
async def get_my_policies(
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """Get current user's policies"""
    from modules.rbac.service import RBACService
    
    policies = await RBACService.get_user_policies(current_user.id, db)
    return [PolicyBase.model_validate(policy) for policy in policies]


@router.get("/health")
async def rbac_health():
    """RBAC system health check"""
    return {"status": "healthy", "service": "rbac-management"}