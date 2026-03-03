#!/bin/bash

# Backend startup script for development
set -e

echo "🚀 Starting Exam Center Backend"
echo "==============================="

# Move to backend directory
cd /workspaces/exam_center/backend

# Activate virtual environment
if [ -f "venv/bin/activate" ]; then
    echo "🐍 Activating virtual environment..."
    source venv/bin/activate
else
    echo "❌ Virtual environment not found. Please run: python3 -m venv venv && source venv/bin/activate && pip install -r requirements.txt"
    exit 1
fi

# Check if dependencies are installed
echo "📦 Checking dependencies..."
if ! python -c "import fastapi, sqlalchemy, alembic" >/dev/null 2>&1; then
    echo "⚠️ Dependencies missing. Installing..."
    pip install -r requirements.txt
fi

# Start the server
echo "🌟 Starting FastAPI server..."
python -m uvicorn main:app --reload --host 0.0.0.0 --port 10000
