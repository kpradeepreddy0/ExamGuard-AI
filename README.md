ExamGuard AI
AI Based Online Examination Monitoring System

Introduction

With the rapid growth of online education, conducting secure examinations has become a major challenge. Most existing online exam systems do not have proper monitoring, which makes cheating easier for students.

To address this issue, ExamGuard AI was developed as an intelligent online proctoring system. It uses Artificial Intelligence to monitor students in real time during examinations.

The system can detect suspicious activities such as absence of face, unusual head movements, and use of mobile phones. This helps in maintaining fairness and discipline during online exams.

This project is developed as a final year academic project and runs securely on a local system.

Objective

The main objective of this project is to design and develop a secure online examination system that can automatically monitor students using Artificial Intelligence.

The system aims to reduce cheating, ensure fairness, and minimize the need for human invigilators during online exams.

Key Features

User Authentication

The system includes a secure login and registration process. Passwords are encrypted using SHA 256, and session management ensures that only authorized users can access the system.

Example
A user cannot access the exam page without logging in
Session ends automatically after logout

Online Examination System

The platform allows students to attempt multiple choice questions within a fixed time limit. The system also supports automatic submission when time expires.

Example
If the student does not submit manually, the system submits automatically
The timer ensures strict exam duration

AI Based Proctoring

This is the core feature of the system. The webcam is used to monitor the student continuously.

The system detects
Face absence
Head movement
Mobile phone usage

Example
If the student looks away frequently, warnings are generated
If the face is not detected, a violation is recorded

Live Camera Monitoring

The system displays real time webcam feed with detection overlays.

Example
Face is highlighted using a bounding box
Warning messages are shown instantly

User Interface

The interface is designed using modern styling with a clean and professional look. It is responsive and easy to use.

Example
Smooth transitions improve usability
Layout adjusts for different screen sizes

Technologies Used

Frontend
HTML5
CSS3
JavaScript
MediaPipe
TensorFlow js
COCO SSD

Backend
Python
Flask
SQLite
OpenCV
NumPy

System Workflow

The working of the system follows these steps

User opens the application
User registers or logs in
Dashboard is displayed
User starts the exam
AI monitoring starts automatically
System tracks behavior continuously
Exam is submitted either manually or automatically

Installation and Setup

To run the project locally, follow these steps

git clone https://github.com/kpradeepreddy0/ExamGuard-AI.git

cd ExamGuard-AI
pip install -r requirements.txt
python3 app.py

Open in browser
http://127.0.0.1:8000

http://localhost:8000

Limitations

The system has some limitations that need to be considered

It works only on localhost and is not deployed online
Detection accuracy depends on camera quality and lighting
Mobile detection may not be fully reliable in all cases
System has not been tested for multiple users at scale

Future Enhancements

The system can be improved further with the following features

Deployment on cloud platforms
Detection of multiple persons in frame
Audio monitoring for detecting conversations
Tab switching detection
Admin panel for monitoring and analytics

Project Status

Core functionality completed
AI monitoring implemented
Authentication system secured
User interface completed
Ready for demonstration

Developer

Pradeep Reddy K
Final Year Student

Conclusion

This project is for educational use only.


