#!/bin/bash

echo "🔍 DevContainer Troubleshooting Script"
echo "======================================"

# Check if we're in the right directory
echo "📍 Current directory: $(pwd)"

# Check database connectivity
echo "🗄️ Testing database connection..."
if pg_isready -h localhost -p 5432 -U postgres > /dev/null 2>&1; then
    echo "✅ Database is accessible"
else
    echo "❌ Database is not accessible"
    echo "Try: docker-compose restart db"
fi

# Check if virtual environment exists
if [ -d "/workspaces/exam_center/backend/venv" ]; then
    echo "✅ Python virtual environment exists"
    
    # Check if virtual environment is activated
    if [[ "$VIRTUAL_ENV" == *"backend/venv"* ]]; then
        echo "✅ Virtual environment is activated"
    else
        echo "⚠️ Virtual environment is not activated"
        echo "Run: cd backend && source venv/bin/activate"
    fi
else
    echo "❌ Python virtual environment not found"
    echo "Run: cd backend && python3 -m venv venv"
fi

# Check if Node.js dependencies are installed
if [ -d "/workspaces/exam_center/frontend/node_modules" ]; then
    echo "✅ Frontend dependencies installed"
else
    echo "❌ Frontend dependencies not installed"
    echo "Run: npm install --prefix frontend"
fi

if [ -d "/workspaces/exam_center/backend/node_modules" ]; then
    echo "✅ Backend dependencies installed"
else
    echo "❌ Backend dependencies not installed"
    echo "Run: cd backend && npm install"
fi

# Check if Python dependencies are installed
echo "🐍 Checking Python dependencies..."
cd /workspaces/exam_center/backend
if [ -d "venv" ]; then
    if source venv/bin/activate && python -c "import sqlalchemy, alembic, fastapi" 2>/dev/null; then
        echo "✅ Python dependencies installed"
        
        # Test database connection with SQLAlchemy
        if source venv/bin/activate && python -c "
import asyncio
from database import engine
async def test():
    try:
        async with engine.begin() as conn:
            await conn.execute(sqlalchemy.text('SELECT 1'))
        print('✅ SQLAlchemy database connection working')
    except Exception as e:
        print(f'❌ SQLAlchemy connection failed: {e}')
import sqlalchemy
asyncio.run(test())
" 2>/dev/null; then
            echo "✅ SQLAlchemy database connection working"
        else
            echo "❌ SQLAlchemy database connection failed"
        fi
    else
        echo "❌ Python dependencies not properly installed"
        echo "Run: cd backend && source venv/bin/activate && pip install -r requirements.txt"
    fi
else
    echo "❌ Python virtual environment not found"
fi

# Test Python imports
echo "🐍 Testing Python setup..."
cd /workspaces/exam_center/backend
if [ -f "venv/bin/activate" ]; then
    source venv/bin/activate
    if python -c "import sys; print(f'Python version: {sys.version}')" 2>/dev/null; then
        echo "✅ Python is working"
    else
        echo "❌ Python is not working properly"
    fi
    
    if python -c "import uvicorn" 2>/dev/null; then
        echo "✅ uvicorn is installed"
    else
        echo "❌ uvicorn is not installed"
        echo "Run: pip install -r requirements.txt"
    fi
fi

echo ""
echo "🔧 Manual setup commands if needed:"
echo "1. Create tables:"
echo "   cd backend && source venv/bin/activate && python scripts/create_tables.py"
echo "2. Run migrations:"
echo "   cd backend && source venv/bin/activate && alembic upgrade head"
echo "3. Seed database:"
echo "   cd backend && source venv/bin/activate && python scripts/seed.py"
echo "4. Start frontend:"
echo "   npm run dev --prefix frontend"
echo "5. Start backend:"
echo "   cd backend && source venv/bin/activate && python -m uvicorn main:app --reload --host 0.0.0.0 --port 8000"
echo "6. Health check:"
echo "   bash /tmp/health-check.sh"
echo "7. Test database:"
echo "   cd backend && source venv/bin/activate && python scripts/test_db.py"
