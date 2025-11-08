# Backend/wsgi.py
from rds import app  # adjust import if your app object lives in a different module, e.g., from server import app

if __name__ == "__main__":
    # For local debugging only
    app.run(host="0.0.0.0", port=5000, debug=True)
