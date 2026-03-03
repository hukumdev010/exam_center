#!/usr/bin/env python3
"""
Simple script to assign super admin role to basnethukum789@gmail.com
"""

import asyncio
import sys
from sqlalchemy import select

from database import AsyncSessionLocal
from models import User, Role
from modules.rbac.service import RBACService


async def assign_superadmin():
    """Assign superadmin role to basnethukum789@gmail.com"""
    
    email = "basnethukum789@gmail.com"
    
    async with AsyncSessionLocal() as db:
        # Find user
        user_stmt = select(User).where(User.email == email)
        user_result = await db.execute(user_stmt)
        user = user_result.scalar_one_or_none()
        
        if not user:
            print(f"User {email} not found. "
                  "Please make sure they log in first.")
            return False
            
        # Find superadmin role
        role_stmt = select(Role).where(Role.name == "superadmin")
        role_result = await db.execute(role_stmt)
        superadmin_role = role_result.scalar_one_or_none()
        
        if not superadmin_role:
            print("Superadmin role not found. Run seed_rbac.py first.")
            return False
            
        # Check if user already has the role
        user_roles = await RBACService.get_user_roles(user.id, db)
        has_superadmin = any(role.name == "superadmin" for role in user_roles)
        
        if has_superadmin:
            print(f"✅ User {email} already has superadmin role!")
            return True
            
        # Assign role
        success = await RBACService.assign_role_to_user(
            user_id=user.id,
            role_id=superadmin_role.id,
            assigned_by="system",
            db=db
        )
        
        if success:
            print(f"✅ Successfully assigned superadmin role to {email}")
            return True
        else:
            print(f"❌ Failed to assign superadmin role to {email}")
            return False


if __name__ == "__main__":
    success = asyncio.run(assign_superadmin())
    sys.exit(0 if success else 1)