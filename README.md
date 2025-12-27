# ExamGuard-AI
### AI-Powered Online Exam Proctoring System

ExamGuard-AI is a real-time AI-based proctoring system designed to monitor online examinations using computer vision techniques. It detects suspicious behavior such as head movement, multiple faces, and mobile phone usage during exams.

---

## Features

-  Real-time webcam monitoring
-  Face detection using MediaPipe
-  Head orientation & stability detection
-  Mobile phone detection using YOLOv8
-  Misbehavior & violation counter
-  Modern dashboard UI
-  Flask-based backend

---

##  Technologies Used

- **Frontend:** HTML, CSS, JavaScript
- **Backend:** Python, Flask
- **AI Models:**
  - MediaPipe (Face Detection)
  - YOLOv8 (Phone Detection)
- **Libraries:** OpenCV, Ultralytics, Flask-CORS

---

##  Project Structure

<img width="311" height="541" alt="Screenshot 2025-12-26 at 5 55 25 AM" src="https://github.com/user-attachments/assets/072b4749-9392-42eb-b21a-03c436f888ff" />



 
 
 short explanation

📁 ai/              → AI & computer vision logic  
📁 static/          → Frontend CSS & JavaScript  
📁 templates/       → HTML templates (Flask)  
phone_detection.py → YOLOv8 mobile phone detection  
app.py             → Flask backend server  



---

##  Installation & Setup

###  Clone the Repository
git clone https://github.com/kpradeepreddy0/ExamGuard-AI.git
cd ExamGuard-AI

## Create Virtual Environment
python3 -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows

## Install Dependencies
pip install -r requirements.txt

## Run the Application
python3 app.py (Mac)
python app.py (Windows)

## Open in Browser
http://127.0.0.1:5000

## How It Works

User logs in to the exam portal

Webcam starts automatically

MediaPipe detects face & head movement

YOLOv8 detects mobile phones

Violations are counted in real-time

UI updates status instantly

##  Notes

YOLOv8 model (yolov8n.pt) is automatically downloaded on first run

Webcam permission is required

Best performance in good lighting

## Academic Use

This project is suitable for:

Final year project

AI/ML mini project

Online exam monitoring system demo

##  Author

Pradeep Reddy
GitHub: https://github.com/kpradeepreddy0

####

 License

This project is for educational purposes only.  remove all emojs and symbols

