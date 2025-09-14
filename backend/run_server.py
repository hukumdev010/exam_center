#!/usr/bin/env python3
import os
import subprocess
import sys

# Change to backend directory
os.chdir("/workspaces/exam_center/backend")

# Activate virtual environment and run server
cmd = [
    "bash",
    "-c",
    "source venv/bin/activate && uvicorn main:app --host 0.0.0.0 --port 8000 --reload",
]

print("Starting FastAPI server on http://localhost:8000")
print("Server logs will appear below:")
print("-" * 50)

try:
    subprocess.run(cmd)
except KeyboardInterrupt:
    print("\nServer stopped by user")
