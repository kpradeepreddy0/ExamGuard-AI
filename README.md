AI-Based Online Exam Proctoring System

ExamGuard-AI is an AI-based online exam proctoring system developed to monitor students during online examinations. The main aim of this project is to reduce cheating in online exams by using computer vision techniques. The system observes the student through a webcam and detects suspicious activities such as head movement, presence of multiple faces, and mobile phone usage during the exam.

This project helps in maintaining fairness and discipline in online examinations without the need for continuous human supervision.

Features

Real-time webcam monitoring during exams

Face detection using MediaPipe

Detection of head movement and orientation

Mobile phone detection using YOLOv8

Automatic counting of exam violations

Simple and user-friendly dashboard

Flask-based backend system

Technologies Used
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

Libraries

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
Step 1: Clone the Repository
git clone https://github.com/kpradeepreddy0/ExamGuard-AI.git
cd ExamGuard-AI

Step 2: Create Virtual Environment

For Windows:

python -m venv venv
venv\Scripts\activate


For macOS or Linux:

python3 -m venv venv
source venv/bin/activate

Step 3: Install Required Libraries
pip install -r requirements.txt

Step 4: Run the Project

For Windows:

python app.py


For macOS:

python3 app.py

Step 5: Open in Browser
http://127.0.0.1:5000

Working of the System

The student logs in to the exam portal

The webcam starts automatically

MediaPipe detects the student’s face and tracks head movement

YOLOv8 checks for mobile phone usage

Any suspicious activity is counted as a violation

The exam status is updated in real time on the dashboard

Advantages

Reduces cheating in online exams

Works automatically without human monitoring

Easy to use and understand

Suitable for remote examinations

Limitations

Requires good lighting conditions

Performance depends on webcam quality

Internet connection is required

Applications

Final year academic project

Online examination monitoring

AI and Machine Learning demonstrations

Conclusion

ExamGuard-AI is a useful system for monitoring online exams using artificial intelligence. It helps in detecting suspicious activities and maintaining exam integrity. This project demonstrates the practical use of AI and computer vision in real-world applications.

Author

Pradeep Reddy

License

This project is developed only for educational purposes.


