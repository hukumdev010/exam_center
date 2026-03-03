import asyncio
import os
import sys

from database import init_db

# Add parent directory to path to import our modules
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


async def create_tables():
    """Create all database tables"""
    try:
        print("🔧 Creating database tables...")
        await init_db()
        print("✅ Database tables created successfully!")
    except Exception as e:
        print(f"❌ Error creating tables: {e}")
        raise


if __name__ == "__main__":
    asyncio.run(create_tables())
