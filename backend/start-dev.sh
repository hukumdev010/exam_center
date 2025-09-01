#!/bin/bash
cd /workspaces/exam_center/backend
source venv/bin/activate
python -m uvicorn main:app --reload --host 0.0.0.0 --port 8000
