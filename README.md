# ExamGuard-AI 🛡️  
### AI-Powered Secure Online Examination System

ExamGuard-AI is a **smart online exam proctoring system** that uses **Artificial Intelligence** to monitor candidates during online examinations.  
It ensures exam integrity by detecting suspicious activities such as **face absence, head movement, and mobile phone usage**.

This project is designed as a **final year academic project** and runs securely on **localhost**.

---

## 🚀 Features

- 🔐 **User Authentication**
  - Register & Login system
  - Secure password hashing (SHA-256)
  - Session-based access control

- 📝 **Online Exam Platform**
  - Multiple-choice questions
  - Timer-based examination
  - Auto submission support (logic ready)

- 🤖 **AI-Based Proctoring**
  - Face detection using MediaPipe
  - Head movement monitoring
  - Phone detection using YOLO / OpenCV
  - Live violation counter

- 🎥 **Live Camera Monitoring**
  - Real-time webcam feed
  - Face bounding box overlay
  - Warning alerts for suspicious behavior

- 🎨 **Modern UI**
  - Glassmorphism design
  - Dark professional theme
  - Smooth animations
  - Responsive layout

---

## 🛠️ Technologies Used

### Frontend
- HTML5
- CSS3 (Glassmorphism UI)
- JavaScript
- MediaPipe (Face Detection)
- TensorFlow.js
- COCO-SSD

### Backend
- Python
- Flask Framework
- SQLite Database
- OpenCV
- NumPy

---

## 📁 Project Structure

<img width="313" height="632" alt="Screenshot 2025-12-28 at 2 18 05 AM" src="https://github.com/user-attachments/assets/1bb152ec-734e-4100-8639-e4f7d41452a4" />




---

## ⚙️ Installation & Setup (Localhost)

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/kpradeepreddy0/ExamGuard-AI.git
cd ExamGuard-AI
2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Run the Application
python3 app.py

4️⃣ Open in Browser
(http://127.0.0.1:8000) (safari)
http://localhost:8000 (chrome or orther browser)


🔑 Application Flow

User opens the link

Login / Register

Dashboard access

Enter exam page

AI monitoring starts automatically

Exam submission

📌 Notes

This project is intended for academic purposes

Runs on localhost (no deployment required)

Deployment-ready structure is implemented

AI phone detection is disabled automatically in cloud environments

🎓 Final Year Project Status

✅ Core functionality completed

✅ AI monitoring implemented

✅ Secure authentication

✅ Professional UI

🔄 Deployment optional

👨‍💻 Developer

Pradeep Reddy K
Final Year Student
Project: ExamGuard-AI

📜 License

This project is for educational use only.end



