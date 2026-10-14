from flask import Flask, render_template, request, redirect, url_for, session, jsonify
import os
import hashlib
import secrets
from urllib.parse import urlparse, urlunparse, parse_qs, urlencode

import psycopg
from psycopg.rows import dict_row

# ================= OPTIONAL OPENCV =================
try:
    import cv2
    import numpy as np
    OPENCV_AVAILABLE = True
except Exception as e:
    cv2 = None
    np = None
    OPENCV_AVAILABLE = False
    print("OpenCV unavailable:", e)

# ================= OPTIONAL PHONE DETECTION =================
phone_detection = None
PHONE_DETECTION_AVAILABLE = False

if OPENCV_AVAILABLE:
    try:
        import phone_detection
        PHONE_DETECTION_AVAILABLE = True
    except Exception as e:
        print("Phone detection disabled:", e)

# ================= EXAM QUESTIONS =================
from exam_data import QUESTIONS

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY") or secrets.token_hex(32)

# ================= NEON POSTGRESQL =================
DATABASE_URL = os.environ.get("DATABASE_URL")


def get_db_connection():
    if not DATABASE_URL:
        raise RuntimeError("DATABASE_URL environment variable is not configured")

    # psycopg accepts Neon PostgreSQL URLs directly.
    return psycopg.connect(DATABASE_URL, row_factory=dict_row)


def create_users_table():
    with get_db_connection() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id BIGSERIAL PRIMARY KEY,
                username TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL
            )
        """)


# Create the table during application initialization.
create_users_table()


# ================= HOME =================
@app.route("/")
def index():
    return redirect(url_for("login"))


# ================= REGISTER =================
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "")

        if not username or not password:
            return "Username and password are required", 400

        # Keep the existing application's password-hash format.
        hashed_password = hashlib.sha256(password.encode()).hexdigest()

        try:
            with get_db_connection() as conn:
                conn.execute(
                    "INSERT INTO users (username, password) VALUES (%s, %s)",
                    (username, hashed_password)
                )
            return redirect(url_for("login"))

        except psycopg.errors.UniqueViolation:
            return "Username already exists", 409

    return render_template("register.html")


# ================= LOGIN =================
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "")
        hashed_password = hashlib.sha256(password.encode()).hexdigest()

        with get_db_connection() as conn:
            user = conn.execute(
                "SELECT id, username FROM users WHERE username = %s AND password = %s",
                (username, hashed_password)
            ).fetchone()

        if user:
            session["user"] = user["username"]
            return redirect(url_for("dashboard"))

        return "Invalid username or password", 401

    return render_template("login.html")


# ================= DASHBOARD =================
@app.route("/dashboard")
def dashboard():
    if "user" in session:
        return render_template("dashboard.html", user=session["user"])
    return redirect(url_for("login"))


# ================= EXAM PAGE =================
@app.route("/exam")
def exam():
    if "user" in session:
        return render_template("index.html")
    return redirect(url_for("login"))


# ================= GET QUESTIONS =================
@app.route("/get_questions")
def get_questions():
    if "user" not in session:
        return jsonify({"error": "Unauthorized"}), 401
    return jsonify(QUESTIONS)


# ================= SUBMIT EXAM =================
@app.route("/submit_exam", methods=["POST"])
def submit_exam():
    if "user" not in session:
        return jsonify({"error": "Unauthorized"}), 401

    data = request.get_json(silent=True) or {}
    score = 0

    for question in QUESTIONS:
        question_id = str(question["id"])
        if question_id in data and data[question_id] == question["answer"]:
            score += 1

    total = len(QUESTIONS)
    percentage = round((score / total) * 100, 1) if total else 0

    session["last_exam_result"] = {
        "score": score,
        "total": total,
        "percentage": percentage
    }

    return jsonify({
        "score": score,
        "total": total,
        "percentage": percentage
    })


# ================= RESULT PAGE =================
@app.route("/result")
def result():
    if "user" not in session:
        return redirect(url_for("login"))

    result_data = session.get("last_exam_result", {
        "score": 0,
        "total": len(QUESTIONS),
        "percentage": 0
    })

    score = int(result_data.get("score", 0))
    total = int(result_data.get("total", len(QUESTIONS)))
    percentage = float(result_data.get("percentage", 0))

    return render_template(
        "result.html",
        user=session["user"],
        score=score,
        total=total,
        percentage=percentage
    )


# ================= PHONE DETECTION API =================
@app.route("/detect_phone", methods=["POST"])
def detect_phone_api():
    if not OPENCV_AVAILABLE or not PHONE_DETECTION_AVAILABLE:
        return jsonify({
            "phone": False,
            "box": None,
            "message": "Phone detection is unavailable on this deployment."
        })

    if "frame" not in request.files:
        return jsonify({"phone": False, "box": None}), 400

    try:
        image_data = request.files["frame"].read()
        if not image_data:
            return jsonify({"phone": False, "box": None}), 400

        npimg = np.frombuffer(image_data, np.uint8)
        frame = cv2.imdecode(npimg, cv2.IMREAD_COLOR)

        if frame is None:
            return jsonify({"phone": False, "box": None}), 400

        phone, box = phone_detection.detect_phone(frame)
        return jsonify({"phone": bool(phone), "box": box})

    except Exception as e:
        print("Phone detection error:", e)
        return jsonify({"phone": False, "box": None}), 500


# ================= LOGOUT =================
@app.route("/logout")
def logout():
    session.pop("user", None)
    session.pop("last_exam_result", None)
    return redirect(url_for("login"))


# ================= LOCAL DEVELOPMENT =================
if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 8000)),
        debug=False
    )
