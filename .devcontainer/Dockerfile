FROM mcr.microsoft.com/vscode/devcontainers/typescript-node:latest

# Install Python and pip
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    python3-venv \
    python3-dev \
    build-essential \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

# Create symlinks for python and pip
RUN ln -sf /usr/bin/python3 /usr/bin/python
RUN ln -sf /usr/bin/pip3 /usr/bin/pip

# Install global npm packages
RUN npm install -g prisma tsx concurrently

# Set up environment variables
ENV DATABASE_URL="postgresql://postgres:postgres@localhost:5432/exam_center"
ENV PYTHONPATH="/workspaces/exam_center/backend"

# Expose ports for both frontend and backend
EXPOSE 3000 8000

# Start command
CMD ["sleep", "infinity"]
