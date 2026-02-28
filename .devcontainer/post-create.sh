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

# Fix permissions for all frontend directories
echo "🔧 Fixing frontend directory permissions..."
sudo chown -R node:node /workspaces/exam_center/frontend/.yarn 2>/dev/null || echo "⚠️ Could not change yarn cache permissions"
sudo chown -R node:node /workspaces/exam_center/frontend/node_modules 2>/dev/null || echo "⚠️ Could not change node_modules permissions"
sudo chown -R node:node /workspaces/exam_center/frontend/.next 2>/dev/null || echo "⚠️ Could not change .next permissions"
sudo chmod -R 755 /workspaces/exam_center/frontend/.yarn 2>/dev/null || echo "⚠️ Could not change yarn cache permissions"
sudo chmod -R 755 /workspaces/exam_center/frontend/node_modules 2>/dev/null || echo "⚠️ Could not change node_modules permissions"

# Skip yarn telemetry config since it's already disabled via environment variables
echo "🔕 Yarn telemetry already disabled via environment variables"

# Install frontend dependencies
echo "📦 Installing frontend dependencies with Yarn v4..."
cd frontend

# Set yarn environment variables for this session
export YARN_ENABLE_TELEMETRY=0
export YARN_ENABLE_GLOBAL_CACHE=false
export YARN_ENABLE_IMMUTABLE_INSTALLS=false

if yarn install --mode=skip-build; then
    print_status "Frontend dependencies installed"
    cd /workspaces/exam_center
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

# # Install localtunnel globally
# echo "🌐 Installing localtunnel for ngrok-like tunneling..."
# if npm install -g cloudflared; then
#     print_status "Localtunnel installed successfully"
# else
#     echo "⚠️ Failed to install localtunnel, you can install it manually with: npm install -g localtunnel"
# fi

# Return to workspace root
cd /workspaces/exam_center

print_status "Devcontainer setup completed successfully!"
echo ""
echo "🎉 Setup complete! You can now start development:"
echo "   📱 Frontend: cd frontend && yarn dev"
echo "   🔧 Backend: cd backend && source venv/bin/activate && python -m uvicorn main:app --reload --host 0.0.0.0 --port 10000"
echo "   🌐 Tunnel Frontend: lt --port 3000 (expose frontend via public URL)"
echo "   🌐 Tunnel Backend: lt --port 10000 (expose backend via public URL)"
echo "   🗄️  Create Migration: cd backend && source venv/bin/activate && alembic revision --autogenerate -m 'description'"
echo "   🔄 Run Migrations: cd backend && source venv/bin/activate && alembic upgrade head"
echo "   🌱 Seed Database: cd backend && source venv/bin/activate && python scripts/seed.py"
echo "   🏥 Health Check: bash /tmp/health-check.sh"
echo ""
