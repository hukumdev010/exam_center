#!/bin/bash

# Install Python dependencies
pip install -r requirements.txt

# Generate Prisma client for Python
prisma generate

# Run database migrations (if needed)
# prisma migrate dev

# Start the FastAPI server
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
