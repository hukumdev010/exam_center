#!/bin/bash

set -e  # Exit on any command failure

echo "🚀 Starting devcontainer post-create setup..."

# Function to print status messages
print_status() {
    echo "✅ $1"
}

print_error() {
    echo "❌ $1"
    exit 1
}

# Wait for database to be ready
echo "⏳ Waiting for database to be ready..."
timeout=60
counter=0
until pg_isready -h localhost -p 5432 -U postgres > /dev/null 2>&1; do
    if [ $counter -ge $timeout ]; then
        print_error "Database connection timeout after ${timeout} seconds"
    fi
    sleep 2
    counter=$((counter + 2))
done
print_status "Database is ready"

# Move to workspace root
cd /workspaces/exam_center

# Install frontend dependencies
echo "📦 Installing frontend dependencies..."
if npm install --prefix frontend; then
    print_status "Frontend dependencies installed"
else
    print_error "Failed to install frontend dependencies"
fi

# Create Python virtual environment
echo "🐍 Setting up Python virtual environment..."
cd backend
if python3 -m venv venv; then
    print_status "Python virtual environment created"
else
    print_error "Failed to create Python virtual environment"
fi

# Activate virtual environment and install Python dependencies
echo "📦 Installing Python dependencies..."
if source venv/bin/activate && pip install --upgrade pip && pip install -r requirements.txt; then
    print_status "Python dependencies installed"
else
    print_error "Failed to install Python dependencies"
fi

# Run Alembic migration to create tables
echo "🗄️ Running database migrations..."
if source venv/bin/activate && alembic upgrade head; then
    print_status "Database migrations completed"
else
    echo "⚠️ Database migrations failed, creating tables manually..."
    # If Alembic fails, we'll let the seed script create tables
fi

# Seed database
echo "🌱 Seeding database..."
if source venv/bin/activate && python scripts/seed.py; then
    print_status "Database seeded successfully"
else
    echo "⚠️ Database seeding failed, but continuing..."
    echo "ℹ️ You can manually seed the database later with: cd backend && source venv/bin/activate && python scripts/seed.py"
fi

# Return to workspace root
cd /workspaces/exam_center

# Make troubleshoot script executable (with error handling for mounted filesystem permissions)
chmod +x troubleshoot.sh 2>/dev/null || echo "⚠️ Could not make troubleshoot.sh executable, use: bash troubleshoot.sh"

print_status "Devcontainer setup completed successfully!"
echo ""
echo "🎉 Setup complete! You can now start development:"
echo "   📱 Frontend: npm run dev --prefix frontend"
echo "   🔧 Backend: cd backend && source venv/bin/activate && python -m uvicorn main:app --reload --host 0.0.0.0 --port 8000"
echo "   🗄️  Create Migration: cd backend && source venv/bin/activate && alembic revision --autogenerate -m 'description'"
echo "   🔄 Run Migrations: cd backend && source venv/bin/activate && alembic upgrade head"
echo "   🌱 Seed Database: cd backend && source venv/bin/activate && python scripts/seed.py"
echo "   🔍 Troubleshoot: ./troubleshoot.sh or bash troubleshoot.sh"
echo "   🏥 Health Check: bash /tmp/health-check.sh"
echo ""
