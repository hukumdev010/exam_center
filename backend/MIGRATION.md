# SQLAlchemy Migration Guide

This document outlines the migration from Prisma to SQLAlchemy + Alembic for the Exam Center backend.

## What Changed

### Dependencies
- **Removed**: `prisma`, `prisma-client-py`
- **Added**: `sqlalchemy[asyncio]`, `alembic`, `asyncpg`, `psycopg2-binary`

### Database Layer
- **ORM**: Prisma → SQLAlchemy with async support
- **Migrations**: Prisma migrations → Alembic migrations
- **Models**: Prisma schema → SQLAlchemy models in `models.py`

### Key Files Changed
- `requirements.txt` - Updated dependencies
- `database.py` - New SQLAlchemy connection setup
- `models.py` - SQLAlchemy models (converted from Prisma schema)
- `main.py` - Updated database initialization
- All routers (`categories.py`, `certifications.py`, etc.) - Updated to use SQLAlchemy queries
- `auth.py` - Updated user authentication with SQLAlchemy

## Database Operations

### Before (Prisma)
```python
# Find with relations
categories = await db.category.find_many(
    include={"certifications": True}
)

# Create
user = await db.user.create(data={
    "email": "test@example.com",
    "name": "Test User"
})
```

### After (SQLAlchemy)
```python
from sqlalchemy import select
from sqlalchemy.orm import selectinload

# Find with relations
stmt = select(Category).options(
    selectinload(Category.certifications)
)
result = await db.execute(stmt)
categories = result.scalars().all()

# Create
user = User(email="test@example.com", name="Test User")
db.add(user)
await db.commit()
```

## Development Commands

### Database Management
```bash
# Create tables manually (for development)
cd backend && source venv/bin/activate && python scripts/create_tables.py

# Generate migration
cd backend && source venv/bin/activate && alembic revision --autogenerate -m "Description"

# Run migrations
cd backend && source venv/bin/activate && alembic upgrade head

# Seed database
cd backend && source venv/bin/activate && python scripts/seed.py

# Test database
cd backend && source venv/bin/activate && python scripts/test_db.py
```

### Development Server
```bash
# Start backend
cd backend && source venv/bin/activate && python -m uvicorn main:app --reload --host 0.0.0.0 --port 8000

# Or use the startup script
cd backend && bash start-dev.sh
```

## DevContainer Changes

### Dockerfile
- Removed Prisma-related global npm packages
- Added `libpq-dev` for PostgreSQL development headers
- Updated health check script commands

### Configuration
- Removed `prisma.prisma` extension from VS Code extensions
- Updated post-create script to use Alembic instead of Prisma
- Updated troubleshooting script with SQLAlchemy checks

## Model Changes

The Prisma schema has been converted to SQLAlchemy models with the following key changes:

### Field Naming
- `camelCase` → `snake_case` (e.g., `userId` → `user_id`)
- `@default(autoincrement())` → `autoincrement=True`
- `@unique` → `unique=True`
- `@relation` → `relationship()`

### Relationships
```python
# Prisma (schema.prisma)
model Category {
  certifications Certification[]
}

# SQLAlchemy (models.py)
class Category(Base):
    certifications = relationship("Certification", back_populates="category")
```

### Constraints
```python
# Unique constraints
__table_args__ = (
    UniqueConstraint('user_id', 'certification_id'),
)
```

## Authentication Changes

- Simplified auth for development (removed Google OAuth dependencies for Windows compatibility)
- Uses mock authentication with token "dev-user"
- Can be extended with proper JWT/OAuth later

## Troubleshooting

### Common Issues
1. **Import Errors**: Make sure virtual environment is activated and dependencies installed
2. **Database Connection**: Ensure PostgreSQL is running and DATABASE_URL is correct
3. **Migration Issues**: Use `python scripts/create_tables.py` for manual table creation

### Helpful Scripts
- `scripts/test_db.py` - Test database connectivity and basic operations
- `scripts/create_tables.py` - Create tables without migrations
- `scripts/seed.py` - Populate database with sample data
- `.devcontainer/troubleshoot.sh` - Comprehensive system check

## Benefits of Migration

1. **Better Python Integration**: Native Python ORM vs. external client
2. **More Control**: Direct SQL access when needed
3. **Mature Ecosystem**: Alembic for migrations, extensive SQLAlchemy features
4. **Performance**: Async support with `asyncpg`
5. **Debugging**: Better error messages and debugging tools
