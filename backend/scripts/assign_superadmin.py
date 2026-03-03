#!/usr/bin/env python3
"""
Super Admin Assignment Script
This script assigns the superadmin role to a specified user email.
Usage: python assign_superadmin.py [email]
If no email is provided, it will assign to the default email:
basnethukum789@gmail.com
"""

import asyncio
import os
import sys
from typing import Optional

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from database import AsyncSessionLocal
from models import User, Role
from modules.rbac.service import RBACService

# Add parent directory to path to import our modules
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class SuperAdminAssigner:
    """Class to handle super admin role assignment"""
    def __init__(self, db: AsyncSession):
        self.db = db
    
    async def find_user_by_email(self, email: str) -> Optional[User]:
        """Find user by email address"""
        stmt = select(User).where(User.email == email)
        result = await self.db.execute(stmt)
        return result.scalar_one_or_none()
    
    async def find_superadmin_role(self) -> Optional[Role]:
        """Find the superadmin role"""
        stmt = select(Role).where(Role.name == "superadmin")
        result = await self.db.execute(stmt)
        return result.scalar_one_or_none()
    
    async def assign_superadmin_role(self, email: str) -> bool:
        """
        Assign superadmin role to the specified email address
        
        Args:
            email: The email address of the user to assign superadmin role
            
        Returns:
            True if successful, False otherwise
        """
        try:
            # Find the user
            print(f"🔍 Looking for user with email: {email}")
            user = await self.find_user_by_email(email)
            
            if not user:
                print(f"❌ User with email '{email}' not found!")
                print("💡 The user needs to log in at least once before we "
                      "can assign roles.")
                return False
            
            print(f"✅ Found user: {user.name} ({user.email})")
            
            # Find the superadmin role
            print("🔍 Looking for superadmin role...")
            superadmin_role = await self.find_superadmin_role()
            
            if not superadmin_role:
                print("❌ Superadmin role not found!")
                print("💡 Please run the RBAC seed script first: "
                      "python scripts/seed_rbac.py")
                return False
            
            print(f"✅ Found superadmin role: {superadmin_role.name}")
            
            # Check if user already has superadmin role
            user_roles = await RBACService.get_user_roles(user.id, self.db)
            has_superadmin = any(
                role.name == "superadmin" for role in user_roles
            )
            
            if has_superadmin:
                print(f"✅ User '{email}' already has superadmin role!")
                return True
            
            # Assign the role
            print(f"🔧 Assigning superadmin role to {email}...")
            success = await RBACService.assign_role_to_user(
                user_id=user.id,
                role_id=superadmin_role.id,
                assigned_by="system",  # System assignment
                db=self.db
            )
            
            if success:
                print(f"✅ Successfully assigned superadmin role to {email}!")
                
                # Verify the assignment
                updated_roles = await RBACService.get_user_roles(
                    user.id, self.db
                )
                role_names = [role.name for role in updated_roles]
                print(f"📋 User now has roles: {', '.join(role_names)}")
                
                return True
            else:
                print(f"❌ Failed to assign superadmin role to {email}")
                return False
                
        except Exception as e:
            print(f"❌ Error assigning superadmin role: {str(e)}")
            await self.db.rollback()
            return False


async def main():
    """Main function to assign superadmin role"""
    
    # Get email from command line argument or use default
    email = "basnethukum789@gmail.com"
    if len(sys.argv) > 1:
        email = sys.argv[1]
    
    print("🚀 Starting Super Admin Assignment Script")
    print(f"📧 Target email: {email}")
    print("=" * 50)
    
    async with AsyncSessionLocal() as db:
        assigner = SuperAdminAssigner(db)
        success = await assigner.assign_superadmin_role(email)
        
        if success:
            print("\n" + "=" * 50)
            print("🎉 Super admin assignment completed successfully!")
            print(f"🔐 User '{email}' now has full administrator privileges.")
            print("\n💡 The user can now:")
            print("   - Access all admin features")
            print("   - Manage users and roles")
            print("   - Approve teachers")
            print("   - Manage content and categories")
            print("   - Access all system policies")
            return 0
        else:
            print("\n" + "=" * 50)
            print("❌ Super admin assignment failed!")
            return 1


if __name__ == "__main__":
    exit_code = asyncio.run(main())
    sys.exit(exit_code)