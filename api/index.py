from fastapi import FastAPI
import sys
import os

# Add the parent directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import your main app
from main import app

# This is important for Vercel serverless function
handler = app
