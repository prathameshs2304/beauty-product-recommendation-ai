💄 Beauty Product Recommendation AI
Face Shape & Skin Intelligence System

An advanced AI-powered web application that analyzes face shape, facial dimensions, skin health (photo + live camera) and provides intelligent beauty insights using computer vision and machine learning.

Designed as a hackathon-grade, industry-style prototype inspired by platforms like PerfectCorp and ModiFace.

🚀 Project Overview

Beauty Product Recommendation AI is a full-stack AI system combining:

✅ Real-time face shape detection
✅ Facial landmark geometry analysis
✅ Photo-based skin analysis with radar visualization
✅ Live camera skin analysis with real-time metrics
✅ AI-powered beauty assistant (chatbot)
✅ Modern professional UI

The system demonstrates end-to-end AI pipeline design from camera capture → landmark processing → ML inference → visualization → user interaction.

🎯 Key Features
1️⃣ Face Shape & Dimensions (Live Camera)

Real-time face detection using MediaPipe Face Landmarker

Extracts 468+ facial landmarks

Computes:

Face Shape (Square, Oval, Round, etc.)

Face Width & Height (px)

Face Ratio

Facial Balance (Balanced / Elongated)

Confidence score

Landmark stabilization prevents flickering

Live mesh visualization with professional UI

2️⃣ Upload Photo Skin Analysis (Completed)

Upload any face image

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

Outputs structured explainable metrics

Radar (Spider) Graph Visualization

Blue / black professional styling

Clear comparative visualization of skin parameters

Clean three-column layout:

Preview image

Analysis results

Radar visualization

Integrated AI Beauty Assistant chatbot

3️⃣ Live Face Skin Analysis (Real-Time Camera) ✅ (New)

Real-time camera feed with facial landmark overlay

Pose validation before capture:

Face centered

Straight gaze

No tilt / rotation

Good lighting

One-click capture workflow

Live skin metrics analysis after capture

Real-time Radar Graph visualization

Compact side-panel UI for:

Preview image

Skin metrics

Radar chart

Designed for demo stability and judge testing

4️⃣ AI Beauty Assistant

Integrated chatbot using Botpress

Handles:

Skincare guidance

Makeup suggestions

Product advice

Works alongside analysis results for personalized assistance

5️⃣ Modern UI / UX

Glassmorphism card design

Responsive layout

Feature selection dashboard

Clean alignment and spacing

Real-time chart visualization

Optimized for live demos and presentations

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

Stability confidence logic

📂 Project Structure
beauty-product-recommendation-ai/
│
├── app.py
├── face_shape_live.py
├── face_shape_analyzer.py
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

📸 Screenshots

(Add screenshots here using GitHub drag & drop)

Suggested:

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

Cloud deployment (AWS / GCP)

Mobile camera optimization

Real-time skin tracking (no capture required)

🧑‍💻 Author

Prathamesh Shekade
B.Tech IT | AI & Data Science Enthusiast
Hackathon Finalist | AI Engineer Aspirant

GitHub: https://github.com/prathameshs2304

📜 License

This project is licensed for educational and demonstration purposes.
This project is licensed for educational & demonstration purposes.# beauty-product-recommendation-ai
<img width="2047" height="1150" alt="image" src="https://github.com/user-attachments/assets/cd50dd20-d975-414c-b4a8-2fbd8536301b" />
<img width="2047" height="1092" alt="image" src="https://github.com/user-attachments/assets/07b64b45-36d0-4334-b08c-affe4cfc3611" />
<img width="1918" height="981" alt="image" src="https://github.com/user-attachments/assets/132890be-3ab1-454a-b0da-290c16d7b6d3" />


