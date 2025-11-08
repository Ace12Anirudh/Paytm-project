from flask import Flask, request, jsonify
import pymysql
from flask_cors import CORS
import config

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": config.FRONTEND_ORIGIN}})  # Allow frontend to call backend

CORS(app, resources={r"/upload": {"origins": config.FRONTEND_ORIGIN}})



def get_db_connection():
    conn = pymysql.connect(
        host=config.DB_HOST,
        user=config.DB_USER,
        password=config.DB_PASS,
        database=config.DB_NAME,
        port=config.DB_PORT,
        cursorclass=pymysql.cursors.DictCursor
    )
    return conn

# ---------- SIGNUP / SAVE ----------
@app.route("/api/save", methods=["POST"])
def save_user():
    try:
        data = request.get_json()
        email = data.get("email")
        password = data.get("password")

        if not email or not password:
            return jsonify({"error": "Email and password required"}), 400

        conn = get_db_connection()
        cursor = conn.cursor()

        sql = "INSERT INTO users (email, password) VALUES (%s, %s)"
        cursor.execute(sql, (email, password))
        conn.commit()

        cursor.close()
        conn.close()

        return jsonify({"message": "User registered successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# upload
@app.route("/upload", methods=["POST"])
def upload_file():
    file = request.files['file']
    # upload to S3 here using boto3
    # ...
    return jsonify({"message": "Upload successful"}), 200

# ---------- LOGIN / CHECK ----------
@app.route("/api/login", methods=["POST"])
def login_user():
    try:
        data = request.get_json()
        email = data.get("email")
        password = data.get("password")

        if not email or not password:
            return jsonify({"error": "Email and password required"}), 400

        conn = get_db_connection()
        cursor = conn.cursor()

        sql = "SELECT * FROM users WHERE email = %s AND password = %s"
        cursor.execute(sql, (email, password))
        user = cursor.fetchone()

        cursor.close()
        conn.close()

        if user:
            return jsonify({"message": "Login successful", "email": email}), 200
        else:
            return jsonify({"error": "Invalid email or password"}), 401
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
