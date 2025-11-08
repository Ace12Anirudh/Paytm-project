# Backend/config.py
"""
Centralized configuration for the backend.
Reads sensitive values from environment variables (preferred) and falls back to safe defaults.
Don't commit a .env with real secrets into the repo.
"""
import os

# Database (RDS) configuration
DB_HOST = os.environ.get("PAYTM_DB_HOST", "rds-endpoint-placeholder")
DB_USER = os.environ.get("PAYTM_DB_USER", "admin")
DB_PASS = os.environ.get("PAYTM_DB_PASSWORD", "replace_with_secure_password")
DB_NAME = os.environ.get("PAYTM_DB_NAME", "paytm")
DB_PORT = int(os.environ.get("PAYTM_DB_PORT", "3306"))

# S3 / storage
S3_BUCKET = os.environ.get("PAYTM_S3_BUCKET", "your-s3-bucket-name")
S3_REGION = os.environ.get("PAYTM_S3_REGION", "ap-northeast-1")

# Backend host/port for local binding (gunicorn uses socket)
BACKEND_HOST = os.environ.get("PAYTM_BACKEND_HOST", "0.0.0.0")
BACKEND_PORT = int(os.environ.get("PAYTM_BACKEND_PORT", "5000"))

# Frontend origin (for CORS)
# Use the full scheme and domain (e.g., https://frontend.example.com)
FRONTEND_ORIGIN = os.environ.get("PAYTM_FRONTEND_URL", "http://localhost:3000")
