"""
RBAC Seed Script

This script creates the default policies, permissions, and roles for the RBAC system.
It should be run after the database migration to set up the initial RBAC configuration.
"""
import asyncio
import sys

from sqlalchemy.ext.asyncio import AsyncSession
from database import AsyncSessionLocal
from modules.rbac.service import RBACService


class RBACSeeder:
    """Class to seed RBAC data"""
    
    def __init__(self, db: AsyncSession):
        self.db = db
        self.policies = {}
        self.permissions = {}
        self.roles = {}
    
    async def create_policies(self):
        """Create all default policies"""
        policy_definitions = [
            # Category policies
            ("readCategory", "Read categories", "category", "read"),
            ("createCategory", "Create new categories", "category", "create"),
            ("updateCategory", "Update existing categories", "category", "update"),
            ("deleteCategory", "Delete categories", "category", "delete"),
            
            # Certification policies
            ("readCertification", "Read certifications", "certification", "read"),
            ("createCertification", "Create new certifications", "certification", "create"),
            ("updateCertification", "Update existing certifications", "certification", "update"),
            ("deleteCertification", "Delete certifications", "certification", "delete"),
            
            # Question policies
            ("readQuestion", "Read questions", "question", "read"),
            ("createQuestion", "Create new questions", "question", "create"),
            ("updateQuestion", "Update existing questions", "question", "update"),
            ("deleteQuestion", "Delete questions", "question", "delete"),
            
            # User management policies
            ("readUser", "Read user information", "user", "read"),
            ("createUser", "Create new users", "user", "create"),
            ("updateUser", "Update user information", "user", "update"),
            ("deleteUser", "Delete users", "user", "delete"),
            ("manageUserRoles", "Manage user role assignments", "user", "manageRoles"),
            
            # Progress policies
            ("readProgress", "Read user progress", "progress", "read"),
            ("updateProgress", "Update user progress", "progress", "update"),
            
            # Quiz attempt policies
            ("readQuizAttempt", "Read quiz attempts", "quizAttempt", "read"),
            ("createQuizAttempt", "Create quiz attempts", "quizAttempt", "create"),
            ("updateQuizAttempt", "Update quiz attempts", "quizAttempt", "update"),
            ("deleteQuizAttempt", "Delete quiz attempts", "quizAttempt", "delete"),
            
            # Teacher policies
            ("readTeacher", "Read teacher information", "teacher", "read"),
            ("createTeacher", "Create teacher profiles", "teacher", "create"),
            ("updateTeacher", "Update teacher profiles", "teacher", "update"),
            ("deleteTeacher", "Delete teacher profiles", "teacher", "delete"),
            ("approveTeacher", "Approve teacher applications", "teacher", "approve"),
            
            # Session policies
            ("readSession", "Read teaching sessions", "session", "read"),
            ("createSession", "Create teaching sessions", "session", "create"),
            ("updateSession", "Update teaching sessions", "session", "update"),
            ("deleteSession", "Delete teaching sessions", "session", "delete"),
            ("bookSession", "Book teaching sessions", "session", "book"),
            ("manageSession", "Manage all teaching sessions", "session", "manage"),
            
            # AI Assistant policies
            ("useAIAssistant", "Use AI assistant features", "aiAssistant", "use"),
            
            # RBAC management policies
            ("readRole", "Read roles", "role", "read"),
            ("createRole", "Create new roles", "role", "create"),
            ("updateRole", "Update existing roles", "role", "update"),
            ("deleteRole", "Delete roles", "role", "delete"),
            ("manageRoles", "Full role management access", "role", "manage"),
            ("readPermission", "Read permissions", "permission", "read"),
            ("createPermission", "Create new permissions", "permission", "create"),
            ("updatePermission", "Update existing permissions", "permission", "update"),
            ("deletePermission", "Delete permissions", "permission", "delete"),
            ("managePermissions", "Full permission management access", "permission", "manage"),
            ("readPolicy", "Read policies", "policy", "read"),
            ("createPolicy", "Create new policies", "policy", "create"),
            ("updatePolicy", "Update existing policies", "policy", "update"),
            ("deletePolicy", "Delete policies", "policy", "delete"),
            ("managePolicies", "Full policy management access", "policy", "manage"),
        ]
        
        print("Creating policies...")
        for name, description, resource, action in policy_definitions:
            policy = await RBACService.create_policy(
                name=name,
                description=description,
                resource=resource,
                action=action,
                is_system=True,
                db=self.db
            )
            if policy:
                self.policies[name] = policy
                print(f"  ✓ Created policy: {name}")
            else:
                print(f"  ✗ Failed to create policy: {name}")
    
    async def create_permissions(self):
        """Create default permissions"""
        permission_definitions = [
            # Student permissions
            ("StudentAccess", "Basic student access permissions", [
                "readCategory", "readCertification", "readQuestion", 
                "readProgress", "updateProgress", "createQuizAttempt", 
                "readQuizAttempt", "useAIAssistant", "readSession", "bookSession"
            ]),
            
            # Teacher permissions
            ("TeacherAccess", "Teacher access permissions", [
                "readCategory", "readCertification", "readQuestion",
                "readProgress", "readQuizAttempt", "useAIAssistant",
                "readSession", "createSession", "updateSession", "readTeacher"
            ]),
            
            # Content Manager permissions
            ("ContentManager", "Content management permissions", [
                "readCategory", "createCategory", "updateCategory",
                "readCertification", "createCertification", "updateCertification",
                "readQuestion", "createQuestion", "updateQuestion"
            ]),
            
            # User Manager permissions
            ("UserManager", "User management permissions", [
                "readUser", "updateUser", "manageUserRoles",
                "readTeacher", "approveTeacher"
            ]),
            
            # Session Manager permissions
            ("SessionManager", "Session management permissions", [
                "readSession", "createSession", "updateSession", 
                "deleteSession", "manageSession"
            ]),
        ]
        
        print("\nCreating permissions...")
        for name, description, policy_names in permission_definitions:
            policy_ids = [
                self.policies[policy_name].id 
                for policy_name in policy_names 
                if policy_name in self.policies
            ]
            
            permission = await RBACService.create_permission(
                name=name,
                description=description,
                policy_ids=policy_ids,
                is_system=True,
                db=self.db
            )
            
            if permission:
                self.permissions[name] = permission
                print(f"  ✓ Created permission: {name} with {len(policy_ids)} policies")
            else:
                print(f"  ✗ Failed to create permission: {name}")
    
    async def create_roles(self):
        """Create default roles"""
        role_definitions = [
            # Student role (default)
            ("student", "Default student role", True, True, ["StudentAccess"], []),
            
            # Teacher role
            ("teacher", "Teacher role", False, False, ["TeacherAccess"], []),
            
            # Admin role
            ("admin", "Administrator role", False, False, 
             ["ContentManager", "UserManager", "SessionManager"], []),
            
            # Superadmin role (has all policies)
            ("superadmin", "Super administrator with all permissions", True, False, [], 
             list(self.policies.keys())),
        ]
        
        print("\nCreating roles...")
        for name, description, is_system, is_default, permission_names, policy_names in role_definitions:
            permission_ids = [
                self.permissions[perm_name].id 
                for perm_name in permission_names 
                if perm_name in self.permissions
            ]
            
            policy_ids = [
                self.policies[policy_name].id 
                for policy_name in policy_names 
                if policy_name in self.policies
            ]
            
            role = await RBACService.create_role(
                name=name,
                description=description,
                policy_ids=policy_ids,
                permission_ids=permission_ids,
                is_system=is_system,
                is_default=is_default,
                db=self.db
            )
            
            if role:
                self.roles[name] = role
                print(f"  ✓ Created role: {name} (permissions: {len(permission_ids)}, policies: {len(policy_ids)})")
            else:
                print(f"  ✗ Failed to create role: {name}")
    
    async def seed_all(self):
        """Seed all RBAC data"""
        try:
            print("Starting RBAC seed process...")
            
            await self.create_policies()
            await self.create_permissions()
            await self.create_roles()
            
            print("\n✅ RBAC seed process completed successfully!")
            print(f"Created {len(self.policies)} policies, {len(self.permissions)} permissions, and {len(self.roles)} roles.")
            
        except Exception as e:
            print(f"\n❌ Error during RBAC seed process: {str(e)}")
            await self.db.rollback()
            raise


async def main():
    """Main function to run the seeder"""
    print("🌱 RBAC Seeder Starting...")
    
    # Get database session
    async with AsyncSessionLocal() as db:
        seeder = RBACSeeder(db)
        await seeder.seed_all()
    
    print("🏁 RBAC Seeder Complete!")


if __name__ == "__main__":
    asyncio.run(main())