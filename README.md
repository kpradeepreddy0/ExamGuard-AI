ExamGuard-AI
AI-Powered Online Exam Proctoring System

ExamGuard-AI is a real-time AI-based online exam proctoring system designed to monitor students during online examinations using computer vision techniques. The system detects suspicious activities such as unusual head movements, the presence of multiple faces, and mobile phone usage during exams.

Features

Real-time webcam monitoring

Face detection using MediaPipe

Head orientation and stability detection

Mobile phone detection using YOLOv8

Automatic misbehavior and violation counter

Modern and responsive dashboard user interface

Flask-based backend architecture

## Technologies Used
Frontend

HTML

CSS

JavaScript

Backend

Python

Flask

AI Models

MediaPipe for face detection

YOLOv8 for mobile phone detection

Libraries and Tools

OpenCV

Ultralytics

Flask-CORS

---

## 📁 Project Structure

<img width="311" height="541" alt="Screenshot 2025-12-26 at 5 55 25 AM" src="https://github.com/user-attachments/assets/072b4749-9392-42eb-b21a-03c436f888ff" />



 
 
 short explanation

📁 ai/              → AI & computer vision logic  
📁 static/          → Frontend CSS & JavaScript  
📁 templates/       → HTML templates (Flask)  
phone_detection.py → YOLOv8 mobile phone detection  
app.py             → Flask backend server  



---

Installation and Setup
Clone the Repository
git clone https://github.com/kpradeepreddy0/ExamGuard-AI.git
cd ExamGuard-AI

Create Virtual Environment

For macOS or Linux:

python3 -m venv venv
source venv/bin/activate


For Windows:

python -m venv venv
venv\Scripts\activate

Install Dependencies
pip install -r requirements.txt

Run the Application

For macOS:

python3 app.py


For Windows:

python app.py

Open in Browser
http://127.0.0.1:5000

How It Works

The user logs in to the exam portal

The webcam starts automatically

MediaPipe detects the face and tracks head movement

YOLOv8 detects mobile phone usage

Violations are counted in real time

The user interface updates the status instantly

Notes

The YOLOv8 model file (yolov8n.pt) is automatically downloaded during the first run

Webcam access permission is required for proper functioning

Best performance is achieved under good lighting conditions

Academic Use

This project is suitable for:

Final year engineering projects

AI and Machine Learning mini projects

Online exam monitoring system demonstrations

Author

Pradeep Reddy
GitHub: https://github.com/kpradeepredd0

License

This project is developed for educational purposes only.


