#!/bin/bash

echo "🏥 Health Check Script"
echo "===================="

# Test database connection
echo "Testing database connection..."
if curl -s http://localhost:8000/health > /dev/null 2>&1; then
    echo "✅ Backend API is responding"
else
    echo "❌ Backend API is not responding"
    echo "Make sure backend is running: cd backend && source venv/bin/activate && npm run dev"
fi

# Test frontend
if curl -s http://localhost:3000 > /dev/null 2>&1; then
    echo "✅ Frontend is responding"
else
    echo "❌ Frontend is not responding"
    echo "Make sure frontend is running: npm run dev --prefix frontend"
fi

# Test database directly
if echo "SELECT 1;" | psql postgresql://postgres:postgres@localhost:5432/exam_center > /dev/null 2>&1; then
    echo "✅ Database is accessible"
else
    echo "❌ Database is not accessible"
fi

echo ""
echo "🚀 Quick start commands:"
echo "Frontend: npm run dev --prefix frontend"
echo "Backend:  cd backend && source venv/bin/activate && npm run dev"
