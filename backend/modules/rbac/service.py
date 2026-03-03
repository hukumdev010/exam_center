"""
RBAC Service Layer

This module provides services for Role-Based Access Control (RBAC)
functionality including policy checking, role management, permission
management, and user role assignments.
"""
from typing import List, Optional, Set
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload
from sqlalchemy import select
from models import Policy, Permission, Role, User


class RBACService:
    """Service class for RBAC operations"""

    @staticmethod
    async def get_user_policies(user_id: str, db: AsyncSession) -> Set[str]:
        """
        Get all policy names that a user has access to through their roles
        and permissions.
        
        Args:
            user_id: The user ID
            db: Database session
            
        Returns:
            Set of policy names the user has access to
        """
        # Get user with all roles and their policies/permissions
        stmt = (
            select(User)
            .options(
                selectinload(User.roles).selectinload(Role.policies),
                selectinload(User.roles)
                .selectinload(Role.permissions)
                .selectinload(Permission.policies)
            )
            .where(User.id == user_id)
        )
        
        result = await db.execute(stmt)
        user = result.scalar_one_or_none()
        
        if not user:
            return set()
        
        policies = set()
        
        # Collect policies from direct role assignments
        for role in user.roles:
            for policy in role.policies:
                policies.add(policy.name)
            
            # Collect policies from permissions assigned to roles
            for permission in role.permissions:
                for policy in permission.policies:
                    policies.add(policy.name)
        
        return policies

    @staticmethod
    async def has_policy(
        user_id: str, policy_name: str, db: AsyncSession
    ) -> bool:
        """
        Check if a user has access to a specific policy.
        
        Args:
            user_id: The user ID
            policy_name: Name of the policy to check
            db: Database session
            
        Returns:
            True if user has the policy, False otherwise
        """
        user_policies = await RBACService.get_user_policies(user_id, db)
        return policy_name in user_policies

    @staticmethod
    async def has_any_policy(
        user_id: str, policy_names: List[str], db: AsyncSession
    ) -> bool:
        """
        Check if a user has access to any of the specified policies.
        
        Args:
            user_id: The user ID
            policy_names: List of policy names to check
            db: Database session
            
        Returns:
            True if user has any of the policies, False otherwise
        """
        user_policies = await RBACService.get_user_policies(user_id, db)
        return any(policy in user_policies for policy in policy_names)

    @staticmethod
    async def has_all_policies(
        user_id: str, policy_names: List[str], db: AsyncSession
    ) -> bool:
        """
        Check if a user has access to all of the specified policies.
        
        Args:
            user_id: The user ID
            policy_names: List of policy names to check
            db: Database session
            
        Returns:
            True if user has all policies, False otherwise
        """
        user_policies = await RBACService.get_user_policies(user_id, db)
        return all(policy in user_policies for policy in policy_names)

    @staticmethod
    async def assign_role_to_user(
        user_id: str, 
        role_id: int, 
        assigned_by: Optional[str] = None,
        db: AsyncSession = None
    ) -> bool:
        """
        Assign a role to a user.
        
        Args:
            user_id: The user ID
            role_id: The role ID
            assigned_by: ID of user who assigned the role
            db: Database session
            
        Returns:
            True if successful, False otherwise
        """
        try:
            # Check if user and role exist
            user_stmt = select(User).where(User.id == user_id)
            role_stmt = select(Role).where(Role.id == role_id)
            
            user_result = await db.execute(user_stmt)
            role_result = await db.execute(role_stmt)
            
            user = user_result.scalar_one_or_none()
            role = role_result.scalar_one_or_none()
            
            if not user or not role:
                return False
            
            # Check if user already has this role
            if role in user.roles:
                return True
            
            # Assign role
            user.roles.append(role)
            await db.commit()
            return True
            
        except Exception:
            await db.rollback()
            return False

    @staticmethod
    async def remove_role_from_user(
        user_id: str, role_id: int, db: AsyncSession
    ) -> bool:
        """
        Remove a role from a user.
        
        Args:
            user_id: The user ID
            role_id: The role ID
            db: Database session
            
        Returns:
            True if successful, False otherwise
        """
        try:
            # Get user with roles
            stmt = (
                select(User)
                .options(selectinload(User.roles))
                .where(User.id == user_id)
            )
            
            result = await db.execute(stmt)
            user = result.scalar_one_or_none()
            
            if not user:
                return False
            
            # Find and remove the role
            role_to_remove = None
            for role in user.roles:
                if role.id == role_id:
                    role_to_remove = role
                    break
            
            if role_to_remove:
                user.roles.remove(role_to_remove)
                await db.commit()
            
            return True
            
        except Exception:
            await db.rollback()
            return False

    @staticmethod
    async def get_user_roles(user_id: str, db: AsyncSession) -> List[Role]:
        """
        Get all roles assigned to a user.
        
        Args:
            user_id: The user ID
            db: Database session
            
        Returns:
            List of Role objects
        """
        stmt = (
            select(User)
            .options(selectinload(User.roles))
            .where(User.id == user_id)
        )
        
        result = await db.execute(stmt)
        user = result.scalar_one_or_none()
        
        return user.roles if user else []

    @staticmethod
    async def create_policy(
        name: str,
        description: str,
        resource: str,
        action: str,
        is_system: bool = False,
        db: AsyncSession = None
    ) -> Optional[Policy]:
        """
        Create a new policy.
        
        Args:
            name: Policy name
            description: Policy description
            resource: Resource type (e.g., "category", "certification")
            action: Action type (e.g., "read", "create", "update", "delete")
            is_system: Whether this is a system policy
            db: Database session
            
        Returns:
            Created Policy object or None if failed
        """
        try:
            policy = Policy(
                name=name,
                description=description,
                resource=resource,
                action=action,
                is_system=is_system
            )
            
            db.add(policy)
            await db.commit()
            await db.refresh(policy)
            
            return policy
            
        except Exception:
            await db.rollback()
            return None

    @staticmethod
    async def create_permission(
        name: str,
        description: str,
        policy_ids: List[int] = None,
        is_system: bool = False,
        db: AsyncSession = None
    ) -> Optional[Permission]:
        """
        Create a new permission.
        
        Args:
            name: Permission name
            description: Permission description
            policy_ids: List of policy IDs to attach to this permission
            is_system: Whether this is a system permission
            db: Database session
            
        Returns:
            Created Permission object or None if failed
        """
        try:
            permission = Permission(
                name=name,
                description=description,
                is_system=is_system
            )
            
            # Attach policies if provided
            if policy_ids:
                policy_stmt = select(Policy).where(Policy.id.in_(policy_ids))
                policy_result = await db.execute(policy_stmt)
                policies = policy_result.scalars().all()
                permission.policies.extend(policies)
            
            db.add(permission)
            await db.commit()
            await db.refresh(permission)
            
            return permission
            
        except Exception:
            await db.rollback()
            return None

    @staticmethod
    async def create_role(
        name: str,
        description: str,
        policy_ids: List[int] = None,
        permission_ids: List[int] = None,
        is_system: bool = False,
        is_default: bool = False,
        db: AsyncSession = None
    ) -> Optional[Role]:
        """
        Create a new role.
        
        Args:
            name: Role name
            description: Role description
            policy_ids: List of policy IDs to attach to this role
            permission_ids: List of permission IDs to attach to this role
            is_system: Whether this is a system role
            is_default: Whether this is a default role assigned to new users
            db: Database session
            
        Returns:
            Created Role object or None if failed
        """
        try:
            role = Role(
                name=name,
                description=description,
                is_system=is_system,
                is_default=is_default
            )
            
            # Attach policies if provided
            if policy_ids:
                policy_stmt = select(Policy).where(Policy.id.in_(policy_ids))
                policy_result = await db.execute(policy_stmt)
                policies = policy_result.scalars().all()
                role.policies.extend(policies)
            
            # Attach permissions if provided
            if permission_ids:
                permission_stmt = (
                    select(Permission)
                    .where(Permission.id.in_(permission_ids))
                )
                permission_result = await db.execute(permission_stmt)
                permissions = permission_result.scalars().all()
                role.permissions.extend(permissions)
            
            db.add(role)
            await db.commit()
            await db.refresh(role)
            
            return role
            
        except Exception:
            await db.rollback()
            return None

    @staticmethod
    async def assign_default_roles_to_user(
        user_id: str, db: AsyncSession
    ) -> bool:
        """
        Assign default roles to a new user.
        
        Args:
            user_id: The user ID
            db: Database session
            
        Returns:
            True if successful, False otherwise
        """
        try:
            # Get all default roles
            stmt = select(Role).where(Role.is_default.is_(True))
            result = await db.execute(stmt)
            default_roles = result.scalars().all()
            
            # Get user
            user_stmt = select(User).where(User.id == user_id)
            user_result = await db.execute(user_stmt)
            user = user_result.scalar_one_or_none()
            
            if not user:
                return False
            
            # Assign default roles
            for role in default_roles:
                if role not in user.roles:
                    user.roles.append(role)
            
            await db.commit()
            return True
            
        except Exception:
            await db.rollback()
            return False