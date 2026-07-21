# 📸 SnapClass – Intelligent AI Attendance System

SnapClass is an AI-powered attendance management system that automates attendance using **Face Recognition**, **Voice Recognition**, and **Computer Vision**. The system enables teachers to create classes, enroll students, and mark attendance through facial and voice recognition, providing a secure and efficient alternative to traditional attendance methods.

---

# 🌐 Live Demo

### 🎨 Landing Page

https://snapclassfrontend.vercel.app/


---

# 📌 Project Overview

SnapClass simplifies attendance management by leveraging Artificial Intelligence to recognize students in real time. It combines computer vision and voice recognition technologies with an intuitive Streamlit interface, making attendance fast, accurate, and contactless.

---

# ✨ Features

* 📸 AI-powered Face Recognition
* 🎤 Voice Recognition Attendance
* 👤 Student Enrollment
* 👨‍🏫 Teacher Dashboard
* 👨‍🎓 Student Dashboard
* 📚 Subject & Course Management
* 📊 Attendance Tracking
* 🔗 Share Subject Links
* 🤖 Automatic Student Enrollment
* ⚡ Real-time Attendance Processing

---

# 🛠️ Tech Stack

### Programming Language

* Python

### Framework

* Streamlit

### Artificial Intelligence

* Face Recognition
* OpenCV
* Dlib
* Scikit-learn

### Voice Recognition

* Librosa
* Resemblyzer

### Database

* Supabase

### Security

* Bcrypt

### Other Libraries

* NumPy
* Pandas
* Pillow
* Segno

---

# 📂 Project Structure

```text
intelligent-ai-attendance--face-recog.-system-main/
│
├── app.py                         # Main Streamlit application
├── requirements.txt               # Project dependencies
├── .gitignore
│
└── src/
    ├── components/
    │   ├── dialog_add_photo.py
    │   ├── dialog_attendance_results.py
    │   ├── dialog_auto_enroll.py
    │   ├── dialog_create_subject.py
    │   ├── dialog_enroll.py
    │   ├── dialog_share_subject.py
    │   ├── dialog_voice_attendance.py
    │   ├── footer.py
    │   ├── header.py
    │   └── subject_card.py
    │
    ├── database/
    │   ├── config.py
    │   └── db.py
    │
    ├── pipelines/
    │   ├── face_pipeline.py
    │   └── voice_pipeline.py
    │
    ├── screens/
    │   ├── home_screen.py
    │   ├── student_screen.py
    │   └── teacher_screen.py
    │
    └── ui/
        └── base_layout.py
```

---

# 🚀 Installation

## Clone the Repository

```bash
git clone https://github.com/KushiArun/intelligent-ai-attendance--face-recog.-system.git

cd intelligent-ai-attendance--face-recog.-system
```

---

## Create a Virtual Environment

### Windows

```bash
python -m venv .venv

.venv\Scripts\activate
```

### macOS / Linux

```bash
python3 -m venv .venv

source .venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run the Application

```bash
streamlit run app.py
```

Open your browser:

```
http://localhost:8501
```

---

# 🔐 Environment Variables

Create a `.streamlit/secrets.toml` file or configure the following environment variables:

```toml
SUPABASE_URL = "your_supabase_url"
SUPABASE_KEY = "your_supabase_key"
```

---

# 📸 Application Workflow

### Teacher

* Login
* Create Subject
* Share Subject Link
* View Attendance Records
* Mark Attendance via Face Recognition
* Mark Attendance via Voice Recognition

### Student

* Login
* Join Subject
* Enroll Face Data
* Participate in Attendance Sessions
* View Attendance Status

---

# 📈 Future Improvements

* Face Liveness Detection
* Mobile Application
* Multi-Camera Attendance
* Attendance Analytics Dashboard
* Email Notifications
* Export Attendance to Excel/PDF
* QR Code Attendance
* Multi-Factor Authentication

---

# 🎯 Use Cases

* Schools
* Colleges
* Universities
* Coaching Institutes
* Corporate Training
* Smart Classrooms

---

# 💻 GitHub Repositories

### 🤖 AI Attendance System

https://github.com/KushiArun/intelligent-ai-attendance--face-recog.-system

### 🎨 Landing Page

https://github.com/KushiArun/snapclassfrontend

---

# 🌍 Live Applications

**Landing Page**

https://snapclassfrontend.vercel.app/



---

# 👨‍💻 Author

**Kushi Arun**

GitHub: https://github.com/KushiArun

---
