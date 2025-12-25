from flask import Flask, render_template, jsonify, request
import cv2
import numpy as np
from phone_detection import detect_phone

app = Flask(__name__)

@app.route("/")
def login():
    return render_template("login.html")

@app.route("/exam")
def exam():
    return render_template("index.html")

@app.route("/detect_phone", methods=["POST"])
def detect_phone_api():
    if "frame" not in request.files:
        return jsonify({"phone": False, "box": None})

    file = request.files["frame"]
    npimg = np.frombuffer(file.read(), np.uint8)
    frame = cv2.imdecode(npimg, cv2.IMREAD_COLOR)

    if frame is None:
        return jsonify({"phone": False, "box": None})

    phone_found, box = detect_phone(frame)

    return jsonify({
        "phone": phone_found,
        "box": box
    })

if __name__ == "__main__":
    app.run(debug=True)
