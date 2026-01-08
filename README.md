💄 Beauty Product Recommendation AI
Face Shape & Skin Intelligence System

An advanced AI-powered web application that analyzes face shape, facial dimensions, and skin health using computer vision and machine learning.
The system provides intelligent beauty insights with a modern, professional UI and supports multi-device usage (mobile, tablet, laptop).

Designed as a hackathon-grade, industry-style prototype, inspired by platforms like PerfectCorp and ModiFace.

🚀 Project Overview

Beauty Product Recommendation AI is a full-stack AI system that demonstrates an end-to-end pipeline:

📷 Camera / Image Input → 🧠 AI Processing → 📊 Visualization → 🤖 User Interaction

Core Capabilities

✅ Real-time face shape detection
✅ Facial landmark geometry analysis
✅ Photo-based skin analysis with radar visualization
✅ Live camera skin analysis workflow
✅ AI-powered beauty assistant (chatbot)
✅ Mobile-friendly responsive UI
✅ Multi-device camera support (browser-based capture)
✅ Demo-stable architecture for hackathons and presentations

The system is optimized for accuracy, smooth UX, and scalability readiness.

🎯 Key Features
1️⃣ Face Shape & Dimensions (Live Camera)

Real-time face analysis using MediaPipe Face Landmarker running on backend inference.

Extracts:

468+ facial landmarks

Face geometry metrics

Computes:

Face Shape (Square / Oval / Round)

Face Width & Height (px)

Face Ratio

Facial Balance (Balanced / Elongated)

Stability-based Confidence Score

Highlights:

Browser-based camera capture (works on phone, tablet, laptop)

Stable inference buffer for accurate results

Clean glassmorphism dashboard UI

Animated confidence indicator

Optimized for low latency during demos

2️⃣ Upload Photo Skin Analysis (Completed)

Upload any face image from:

📱 Mobile gallery / camera

💻 Desktop files

AI analyzes multiple skin metrics:

Acne severity

Blackheads

Dark circles

Hair quality

Hydration level

Pore size

Sensitivity

Skin tone

Wrinkles

Outputs:

Structured explainable metrics

Radar (Spider) graph visualization

Clear three-column layout:

Image Preview

Analysis Results

Radar Visualization

UX Enhancements:

Mobile-safe upload behavior

Visual confirmation when image is selected

Clean modern buttons and layout

3️⃣ Live Face Skin Analysis (Camera Workflow)

Real-time camera feed with pose validation before capture.

Pose Validation Rules:

Face centered

Straight gaze

No tilt / rotation

Good lighting

Workflow:

Live camera alignment

Pose stability detection

One-click capture

AI skin analysis

Radar graph visualization

UI Features:

Compact side-panel layout

Preview image

Skin metrics

Radar chart

Optimized for judge testing and demo stability

4️⃣ AI Beauty Assistant

Integrated chatbot powered by Botpress.

Supports:

Skincare guidance

Makeup suggestions

Product advice

Personalized follow-ups based on analysis

Works alongside visual analysis results for a guided experience.

5️⃣ Modern UI / UX

Glassmorphism card design

Responsive layout for all devices

Feature selection dashboard

Animated metrics and confidence indicators

Clean typography and spacing

Optimized for presentations and live demos

🧠 Tech Stack
Frontend

HTML5

CSS3 (Glassmorphism UI)

JavaScript

Chart.js (Radar visualization)

Backend

Python (Flask)

OpenCV

MediaPipe Face Landmarker

NumPy

AI / ML

Facial landmark geometry analysis

Rule-based face shape classification

CNN-based skin analysis (photo upload)

Stability-based confidence logic

📂 Project Structure
beauty-product-recommendation-ai/
│
├── app.py
├── face_shape_live.py
├── your_cnn_model.py
│
├── templates/
│   ├── feature_selection.html
│   ├── face_shape_live.html
│   ├── skin_analysis.html
│   ├── live_skin_analysis.html
│
├── static/
│   ├── face_shape_live.js
│   ├── live_skin_analysis.js
│   ├── script.js
│   ├── style.css
│   ├── img1.jpeg
│   ├── img2.jpeg
│   ├── img3.jpeg
│   ├── img4.jpeg
│
├── requirements.txt
├── README.md
└── .gitignore

▶️ How to Run Locally
1️⃣ Clone Repository
git clone https://github.com/prathameshs2304/beauty-product-recommendation-ai.git
cd beauty-product-recommendation-ai

2️⃣ Create Virtual Environment
python -m venv .venv
.venv\Scripts\activate

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Run Application
python app.py

5️⃣ Open in Browser
http://127.0.0.1:5000/feature_selection.html

🌐 Multi-Device Support

The application uses browser-based camera capture, allowing:

✅ Each device to use its own camera
✅ Mobile, tablet, laptop compatibility
✅ No dependency on host machine camera
✅ Reliable public tunnel demos
✅ Independent judge testing

📸 Screenshots

(Add screenshots here using GitHub drag & drop)

Suggested screenshots:

Feature Selection Dashboard

Face Shape Live Analysis

Upload Skin Analysis + Radar Graph

Live Skin Analysis Camera View

AI Beauty Assistant Chat

🧪 Accuracy & Limitations

Not a medical or dermatology diagnostic tool

Performance depends on lighting and camera quality

Skin analysis is indicative and experimental

Designed for research, education, and prototype demonstrations

🔮 Future Enhancements

True 3D face mesh rendering

Personalized product recommendation engine

User profile history tracking

Cloud deployment (AWS / GCP / Azure)

Mobile performance optimization

Real-time continuous skin tracking (without capture)

Multi-user analytics dashboard

🧑‍💻 Author

Prathamesh Shekade
B.Tech IT | AI & Data Science Enthusiast
Hackathon Finalist | AI Engineer Aspirant

GitHub:
👉 https://github.com/prathameshs2304

📜 License

This project is licensed for educational and demonstration purposes only.
<img width="2047" height="1150" alt="image" src="https://github.com/user-attachments/assets/cd50dd20-d975-414c-b4a8-2fbd8536301b" />
<img width="2047" height="1092" alt="image" src="https://github.com/user-attachments/assets/07b64b45-36d0-4334-b08c-affe4cfc3611" />
<img width="1918" height="981" alt="image" src="https://github.com/user-attachments/assets/132890be-3ab1-454a-b0da-290c16d7b6d3" />


