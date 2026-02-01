"""
Simple run script - Execute from backend directory
Usage: python run.py
"""
import subprocess
import sys
import os

# Use venv Python
venv_python = os.path.join(os.path.dirname(__file__), "venv", "Scripts", "python.exe")

print("🚀 Starting Pothole Detection Backend...")
print("📍 Server will be at: http://localhost:8000")
print("📖 API Docs at: http://localhost:8000/docs\n")

# Run uvicorn using venv Python
subprocess.run([
    venv_python, "-m", "uvicorn",
    "app.main:app",
    "--host", "0.0.0.0",
    "--port", "8000",
    "--reload"
])
