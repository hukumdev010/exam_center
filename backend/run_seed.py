#!/usr/bin/env python
"""
Simple runner script to seed the database.
Run this from the backend directory: python run_seed.py
"""
import sys
import os
import asyncio
import subprocess


# Check if virtual environment is activated
def is_venv_activated():
    """Check if a virtual environment is currently activated."""
    return hasattr(sys, 'real_prefix') or (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix)


def activate_venv():
    """Activate the virtual environment if it exists."""
    backend_dir = os.path.dirname(os.path.abspath(__file__))
    venv_path = os.path.join(backend_dir, 'venv')
    
    if os.path.exists(venv_path):
        activate_script = os.path.join(venv_path, 'bin', 'activate')
        if os.path.exists(activate_script):
            print(f"Activating virtual environment from {venv_path}...")
            # Run the script in a new shell
            subprocess.run(['bash', '-c', f'source {activate_script} && python {__file__}'], check=False)
            sys.exit(0)
    
    print("Virtual environment not found or already activated. Proceeding...")

# Add backend directory to path so absolute imports work
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Check and activate venv if needed
if not is_venv_activated():
    activate_venv()

from scripts.seed.main import seed_database

if __name__ == "__main__":
    print("Running database seed script...")
    asyncio.run(seed_database())
