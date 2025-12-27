from flask import Flask, render_template, request, redirect, url_for, session, jsonify
import sqlite3
import hashlib
import cv2
import numpy as np
import os

# ================= SAFE PHONE DETECTION IMPORT =================
try:
    import phone_detection
    PHONE_DETECTION_AVAILABLE = True
except Exception as e:
    PHONE_DETECTION_AVAILABLE = False
    print("⚠️ Phone detection disabled:", e)

# ================= EXAM QUESTIONS =================
from exam_data import QUESTIONS

app = Flask(__name__)
app.secret_key = "examguard_secret_key"

# ================= DATABASE =================
DB_NAME = "users.db"

def get_db_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn

def create_users_table():
    conn = get_db_connection()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

create_users_table()

# ================= ROUTES =================

# HOME → LOGIN
@app.route("/")
def index():
    return redirect(url_for("login"))

# -------- REGISTER --------
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        hashed_password = hashlib.sha256(password.encode()).hexdigest()

        try:
            conn = get_db_connection()
            conn.execute(
                "INSERT INTO users (username, password) VALUES (?, ?)",
                (username, hashed_password)
            )
            conn.commit()
            conn.close()
            return redirect(url_for("login"))
        except sqlite3.IntegrityError:
            return "Username already exists"

    return render_template("register.html")

# -------- LOGIN --------
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        hashed_password = hashlib.sha256(password.encode()).hexdigest()

        conn = get_db_connection()
        user = conn.execute(
            "SELECT * FROM users WHERE username=? AND password=?",
            (username, hashed_password)
        ).fetchone()
        conn.close()

        if user:
            session["user"] = username
            return redirect(url_for("dashboard"))
        else:
            return "Invalid username or password"

    return render_template("login.html")

# -------- DASHBOARD --------
@app.route("/dashboard")
def dashboard():
    if "user" in session:
        return render_template("dashboard.html", user=session["user"])
    return redirect(url_for("login"))

# -------- EXAM PAGE --------
@app.route("/exam")
def exam():
    if "user" in session:
        return render_template("index.html")
    return redirect(url_for("login"))

# ================= EXAM PLATFORM =================

# GET QUESTIONS
@app.route("/get_questions")
def get_questions():
    if "user" not in session:
        return jsonify({"error": "Unauthorized"}), 401
    return jsonify(QUESTIONS)

# SUBMIT EXAM
@app.route("/submit_exam", methods=["POST"])
def submit_exam():
    if "user" not in session:
        return jsonify({"error": "Unauthorized"}), 401

    data = request.json
    score = 0

    for q in QUESTIONS:
        qid = str(q["id"])
        if qid in data and data[qid] == q["answer"]:
            score += 1

    return jsonify({
        "score": score,
        "total": len(QUESTIONS)
    })

# ================= PHONE DETECTION API =================
@app.route("/detect_phone", methods=["POST"])
def detect_phone_api():
    if not PHONE_DETECTION_AVAILABLE:
        return jsonify({"phone": False, "box": None})

    if "frame" not in request.files:
        return jsonify({"phone": False, "box": None})

    file = request.files["frame"]
    file.seek(0)

    npimg = np.frombuffer(file.read(), np.uint8)
    frame = cv2.imdecode(npimg, cv2.IMREAD_COLOR)

    if frame is None:
        return jsonify({"phone": False, "box": None})

    phone, box = phone_detection.detect_phone(frame)

    return jsonify({
        "phone": phone,
        "box": box
    })

# -------- LOGOUT --------
@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))

# ================= RUN (RAILWAY / CLOUD READY) =================
if __name__ == "__main__":
   app.run(port=8000, debug=True)


    
