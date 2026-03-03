"""
RBAC Management Controller

Handles RBAC management operations for admin dashboard.
"""
from typing import List, Optional, Tuple
from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload
from sqlalchemy import select, func

from models import Policy, Permission, Role, User
from modules.rbac.service import RBACService
from .model import (
    PolicyCreate, PolicyUpdate, PermissionCreate, PermissionUpdate,
    RoleCreate, RoleUpdate, UserRoleAssignment
)


class RBACController:
    """Controller for RBAC management operations"""

    # Policy Management
    @staticmethod
    async def list_policies(
        skip: int = 0,
        limit: int = 100,
        search: Optional[str] = None,
        db: AsyncSession = None
    ) -> Tuple[List[Policy], int]:
        """List all policies with optional search"""
        query = select(Policy)
        
        if search:
            query = query.where(
                Policy.name.ilike(f"%{search}%") |
                Policy.description.ilike(f"%{search}%")
            )
        
        # Get total count
        count_query = select(func.count(Policy.id))
        if search:
            count_query = count_query.where(
                Policy.name.ilike(f"%{search}%") |
                Policy.description.ilike(f"%{search}%")
            )
        
        total_result = await db.execute(count_query)
        total = total_result.scalar()
        
        # Get paginated results
        query = query.offset(skip).limit(limit).order_by(Policy.name)
        result = await db.execute(query)
        policies = result.scalars().all()
        
        return list(policies), total

    @staticmethod
    async def get_policy(policy_id: int, db: AsyncSession) -> Policy:
        """Get policy by ID"""
        stmt = select(Policy).where(Policy.id == policy_id)
        result = await db.execute(stmt)
        policy = result.scalar_one_or_none()
        
        if not policy:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Policy not found"
            )
        
        return policy

    @staticmethod
    async def create_policy(
        policy_data: PolicyCreate,
        db: AsyncSession
    ) -> Policy:
        """Create a new policy"""
        # Check if policy name already exists
        existing_stmt = select(Policy).where(Policy.name == policy_data.name)
        existing_result = await db.execute(existing_stmt)
        existing_policy = existing_result.scalar_one_or_none()
        
        if existing_policy:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Policy name already exists"
            )
        
        return await RBACService.create_policy(
            name=policy_data.name,
            description=policy_data.description,
            resource=policy_data.resource,
            action=policy_data.action,
            is_system=policy_data.is_system,
            db=db
        )

    @staticmethod
    async def update_policy(
        policy_id: int,
        policy_data: PolicyUpdate,
        db: AsyncSession
    ) -> Policy:
        """Update policy"""
        policy = await RBACController.get_policy(policy_id, db)
        
        if policy.is_system:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Cannot modify system policy"
            )
        
        if policy_data.description is not None:
            policy.description = policy_data.description
        
        await db.commit()
        await db.refresh(policy)
        return policy

    @staticmethod
    async def delete_policy(policy_id: int, db: AsyncSession) -> bool:
        """Delete policy"""
        policy = await RBACController.get_policy(policy_id, db)
        
        if policy.is_system:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Cannot delete system policy"
            )
        
        await db.delete(policy)
        await db.commit()
        return True

    # Permission Management
    @staticmethod
    async def list_permissions(
        skip: int = 0,
        limit: int = 100,
        search: Optional[str] = None,
        db: AsyncSession = None
    ) -> Tuple[List[Permission], int]:
        """List all permissions with optional search"""
        query = select(Permission).options(
            selectinload(Permission.policies)
        )
        
        if search:
            query = query.where(
                Permission.name.ilike(f"%{search}%") |
                Permission.description.ilike(f"%{search}%")
            )
        
        # Get total count
        count_query = select(func.count(Permission.id))
        if search:
            count_query = count_query.where(
                Permission.name.ilike(f"%{search}%") |
                Permission.description.ilike(f"%{search}%")
            )
        
        total_result = await db.execute(count_query)
        total = total_result.scalar()
        
        # Get paginated results
        query = query.offset(skip).limit(limit).order_by(Permission.name)
        result = await db.execute(query)
        permissions = result.scalars().all()
        
        return list(permissions), total

    @staticmethod
    async def get_permission(
        permission_id: int, db: AsyncSession
    ) -> Permission:
        """Get permission by ID with policies"""
        stmt = select(Permission).options(
            selectinload(Permission.policies)
        ).where(Permission.id == permission_id)
        
        result = await db.execute(stmt)
        permission = result.scalar_one_or_none()
        
        if not permission:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Permission not found"
            )
        
        return permission

    @staticmethod
    async def create_permission(
        permission_data: PermissionCreate,
        db: AsyncSession
    ) -> Permission:
        """Create a new permission"""
        # Check if permission name already exists
        existing_stmt = select(Permission).where(
            Permission.name == permission_data.name
        )
        existing_result = await db.execute(existing_stmt)
        existing_permission = existing_result.scalar_one_or_none()
        
        if existing_permission:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Permission name already exists"
            )
        
        return await RBACService.create_permission(
            name=permission_data.name,
            description=permission_data.description,
            policy_ids=permission_data.policy_ids,
            is_system=permission_data.is_system,
            db=db
        )

    @staticmethod
    async def update_permission(
        permission_id: int,
        permission_data: PermissionUpdate,
        db: AsyncSession
    ) -> Permission:
        """Update permission"""
        permission = await RBACController.get_permission(permission_id, db)
        
        if permission.is_system:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Cannot modify system permission"
            )
        
        if permission_data.description is not None:
            permission.description = permission_data.description
        
        if permission_data.policy_ids is not None:
            # Get new policies
            policy_stmt = select(Policy).where(
                Policy.id.in_(permission_data.policy_ids)
            )
            policy_result = await db.execute(policy_stmt)
            new_policies = policy_result.scalars().all()
            
            # Replace policies
            permission.policies.clear()
            permission.policies.extend(new_policies)
        
        await db.commit()
        await db.refresh(permission)
        return permission

    @staticmethod
    async def delete_permission(permission_id: int, db: AsyncSession) -> bool:
        """Delete permission"""
        permission = await RBACController.get_permission(permission_id, db)
        
        if permission.is_system:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Cannot delete system permission"
            )
        
        await db.delete(permission)
        await db.commit()
        return True

    # Role Management
    @staticmethod
    async def list_roles(
        skip: int = 0,
        limit: int = 100,
        search: Optional[str] = None,
        db: AsyncSession = None
    ) -> Tuple[List[Role], int]:
        """List all roles with optional search"""
        query = select(Role).options(
            selectinload(Role.policies),
            selectinload(Role.permissions).selectinload(Permission.policies)
        )
        
        if search:
            query = query.where(
                Role.name.ilike(f"%{search}%") |
                Role.description.ilike(f"%{search}%")
            )
        
        # Get total count
        count_query = select(func.count(Role.id))
        if search:
            count_query = count_query.where(
                Role.name.ilike(f"%{search}%") |
                Role.description.ilike(f"%{search}%")
            )
        
        total_result = await db.execute(count_query)
        total = total_result.scalar()
        
        # Get paginated results
        query = query.offset(skip).limit(limit).order_by(Role.name)
        result = await db.execute(query)
        roles = result.scalars().all()
        
        return list(roles), total

    @staticmethod
    async def get_role(role_id: int, db: AsyncSession) -> Role:
        """Get role by ID with policies and permissions"""
        stmt = select(Role).options(
            selectinload(Role.policies),
            selectinload(Role.permissions).selectinload(Permission.policies)
        ).where(Role.id == role_id)
        
        result = await db.execute(stmt)
        role = result.scalar_one_or_none()
        
        if not role:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Role not found"
            )
        
        return role

    @staticmethod
    async def create_role(role_data: RoleCreate, db: AsyncSession) -> Role:
        """Create a new role"""
        # Check if role name already exists
        existing_stmt = select(Role).where(Role.name == role_data.name)
        existing_result = await db.execute(existing_stmt)
        existing_role = existing_result.scalar_one_or_none()
        
        if existing_role:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Role name already exists"
            )
        
        return await RBACService.create_role(
            name=role_data.name,
            description=role_data.description,
            policy_ids=role_data.policy_ids,
            permission_ids=role_data.permission_ids,
            is_system=role_data.is_system,
            is_default=role_data.is_default,
            db=db
        )

    @staticmethod
    async def update_role(
        role_id: int,
        role_data: RoleUpdate,
        db: AsyncSession
    ) -> Role:
        """Update role"""
        role = await RBACController.get_role(role_id, db)
        
        if role.is_system:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Cannot modify system role"
            )
        
        if role_data.description is not None:
            role.description = role_data.description
        
        if role_data.is_default is not None:
            role.is_default = role_data.is_default
        
        if role_data.policy_ids is not None:
            # Get new policies
            policy_stmt = select(Policy).where(
                Policy.id.in_(role_data.policy_ids)
            )
            policy_result = await db.execute(policy_stmt)
            new_policies = policy_result.scalars().all()
            
            # Replace policies
            role.policies.clear()
            role.policies.extend(new_policies)
        
        if role_data.permission_ids is not None:
            # Get new permissions
            permission_stmt = select(Permission).where(
                Permission.id.in_(role_data.permission_ids)
            )
            permission_result = await db.execute(permission_stmt)
            new_permissions = permission_result.scalars().all()
            
            # Replace permissions
            role.permissions.clear()
            role.permissions.extend(new_permissions)
        
        await db.commit()
        await db.refresh(role)
        return role

    @staticmethod
    async def delete_role(role_id: int, db: AsyncSession) -> bool:
        """Delete role"""
        role = await RBACController.get_role(role_id, db)
        
        if role.is_system:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Cannot delete system role"
            )
        
        await db.delete(role)
        await db.commit()
        return True

    # User Role Management
    @staticmethod
    async def list_users_with_roles(
        skip: int = 0,
        limit: int = 100,
        search: Optional[str] = None,
        db: AsyncSession = None
    ) -> Tuple[List[User], int]:
        """List users with their roles"""
        query = select(User).options(
            selectinload(User.roles).selectinload(Role.policies),
            selectinload(User.roles).selectinload(Role.permissions).selectinload(Permission.policies)
        )
        
        if search:
            query = query.where(
                User.email.ilike(f"%{search}%") |
                User.name.ilike(f"%{search}%")
            )
        
        # Get total count
        count_query = select(func.count(User.id))
        if search:
            count_query = count_query.where(
                User.email.ilike(f"%{search}%") |
                User.name.ilike(f"%{search}%")
            )
        
        total_result = await db.execute(count_query)
        total = total_result.scalar()
        
        # Get paginated results
        query = query.offset(skip).limit(limit).order_by(User.email)
        result = await db.execute(query)
        users = result.scalars().all()
        
        return list(users), total

    @staticmethod
    async def get_user_roles(user_id: str, db: AsyncSession) -> User:
        """Get user with roles"""
        stmt = select(User).options(
            selectinload(User.roles).selectinload(Role.policies),
            selectinload(User.roles).selectinload(Role.permissions).selectinload(Permission.policies)
        ).where(
            User.id == user_id
        )
        result = await db.execute(stmt)
        user = result.scalar_one_or_none()
        
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found"
            )
        
        return user

    @staticmethod
    async def assign_roles_to_user(
        assignment: UserRoleAssignment,
        db: AsyncSession
    ) -> User:
        """Assign roles to user"""
        user = await RBACController.get_user_roles(assignment.user_id, db)
        
        # Get roles to assign
        role_stmt = select(Role).where(Role.id.in_(assignment.role_ids))
        role_result = await db.execute(role_stmt)
        roles = role_result.scalars().all()
        
        if len(roles) != len(assignment.role_ids):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="One or more roles not found"
            )
        
        # Replace user roles
        user.roles.clear()
        user.roles.extend(roles)
        
        await db.commit()
        await db.refresh(user)
        return user

    @staticmethod
    async def remove_role_from_user(
        user_id: str,
        role_id: int,
        db: AsyncSession
    ) -> User:
        """Remove specific role from user"""
        success = await RBACService.remove_role_from_user(user_id, role_id, db)
        
        if not success:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Failed to remove role from user"
            )
        
        return await RBACController.get_user_roles(user_id, db)