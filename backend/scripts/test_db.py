#!/usr/bin/env python3
"""
Test script to verify SQLAlchemy setup
"""
import asyncio
import sys
import os
from datetime import datetime

# Add parent directory to path to import our modules
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

async def test_database():
    """Test database connection and basic operations"""
    try:
        from database import engine, AsyncSessionLocal, init_db
        from models import Base, Category
        
        print("🔧 Testing database connection...")
        
        # Test basic connection
        async with engine.begin() as conn:
            result = await conn.execute(sqlalchemy.text("SELECT 1"))
            print("✅ Database connection successful")
        
        # Create tables
        print("🔧 Creating tables...")
        await init_db()
        print("✅ Tables created successfully")
        
        # Test basic CRUD operations
        print("🔧 Testing basic CRUD operations...")
        async with AsyncSessionLocal() as session:
            # Create a test category
            test_category = Category(
                name="Test Category",
                description="A test category",
                slug="test-category",
                icon="test",
                color="blue"
            )
            session.add(test_category)
            await session.commit()
            await session.refresh(test_category)
            print(f"✅ Created category with ID: {test_category.id}")
            
            # Query the category
            from sqlalchemy import select
            stmt = select(Category).where(Category.slug == "test-category")
            result = await session.execute(stmt)
            found_category = result.scalar_one_or_none()
            
            if found_category:
                print(f"✅ Found category: {found_category.name}")
            else:
                print("❌ Could not find test category")
            
            # Clean up
            await session.delete(found_category)
            await session.commit()
            print("✅ Test category deleted")
        
        print("🎉 All database tests passed!")
        return True
        
    except Exception as e:
        print(f"❌ Database test failed: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    import sqlalchemy
    success = asyncio.run(test_database())
    sys.exit(0 if success else 1)
