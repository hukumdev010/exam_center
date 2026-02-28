FROM mcr.microsoft.com/vscode/devcontainers/typescript-node:latest

# Install Python and pip
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    python3-venv \
    python3-dev \
    build-essential \
    postgresql-client \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Create symlinks for python and pip
RUN ln -sf /usr/bin/python3 /usr/bin/python
RUN ln -sf /usr/bin/pip3 /usr/bin/pip

# Enable Corepack and set up Yarn v4
RUN corepack enable && corepack prepare yarn@4.10.3 --activate

# Ensure node user has proper permissions
USER node
RUN mkdir -p /home/node/.yarn/berry/cache && chmod -R 755 /home/node/.yarn
USER root

# Set environment variables for Yarn to disable telemetry and optimize performance
ENV YARN_ENABLE_GLOBAL_CACHE=false
ENV YARN_ENABLE_TELEMETRY=0
ENV YARN_ENABLE_IMMUTABLE_INSTALLS=false
ENV WATCHPACK_POLLING=true
ENV CHOKIDAR_USEPOLLING=true
ENV CHOKIDAR_INTERVAL=1000
ENV TURBOPACK_ALLOW_UNSAFE_FS_READS=1
ENV NEXT_TELEMETRY_DISABLED=1

# Install global npm packages (removed prisma)
RUN npm install -g tsx concurrently

# Copy and set permissions for devcontainer scripts
COPY post-create.sh /tmp/post-create.sh
RUN chmod +x /tmp/post-create.sh

# Create health check script inside container
RUN cat > /tmp/health-check.sh << 'EOF'
#!/bin/bash

echo "🏥 Health Check Script"
echo "===================="

# Test database connection
echo "Testing database connection..."
if curl -s http://localhost:10000/health > /dev/null 2>&1; then
    echo "✅ Backend API is responding"
else
    echo "❌ Backend API is not responding"
    echo "Make sure backend is running: cd backend && source venv/bin/activate && python -m uvicorn main:app --reload --host 0.0.0.0 --port 10000"
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
echo "Frontend: cd frontend && yarn dev"
echo "Backend:  cd backend && source venv/bin/activate && python -m uvicorn main:app --reload --host 0.0.0.0 --port 10000"
echo "Migration: cd backend && source venv/bin/activate && alembic upgrade head"
echo "Seed DB:   cd backend && source venv/bin/activate && python scripts/seed.py"
EOF

RUN chmod +x /tmp/health-check.sh

# Set up environment variables
ENV DATABASE_URL="postgresql+asyncpg://postgres:postgres@localhost:5432/exam_center"
ENV PYTHONPATH="/workspaces/exam_center/backend"

# Expose ports for both frontend and backend
EXPOSE 3000 10000

# Start command
CMD ["sleep", "infinity"]
