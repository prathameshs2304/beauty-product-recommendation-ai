.

💄 Beauty Product Recommendation AI
Face Shape & Skin Intelligence System

An AI-powered web application that analyzes face shape, facial dimensions, and skin conditions using computer vision and machine learning, and provides intelligent beauty & skincare insights.

🚀 Project Overview

Beauty Product Recommendation AI is a full-stack AI system that combines:

Real-time face shape detection

Facial landmark geometry analysis

Photo-based skin analysis

AI-powered beauty assistant (chatbot)

User-friendly modern UI

The system is designed to simulate industry-grade face & skin analysis platforms (similar to PerfectCorp-style workflows) while remaining hackathon-safe and explainable.

🎯 Key Features
1️⃣ Face Shape & Dimensions (Live Camera)

Real-time face detection using MediaPipe Face Landmarker

Extracts 468+ facial landmarks

Calculates:

Face Shape (Square, Round, Oval, etc.)

Face Width & Height (px)

Face Ratio

Facial Balance (Balanced / Elongated)

Confidence scores

Stable, non-flickering results after landmark stabilization

2️⃣ Upload Photo Skin Analysis

Upload a face image for skin analysis

Detects:

Acne severity

Dark circles

Blackheads

Hydration level

Hair quality indicators

Outputs structured JSON results for explainability

3️⃣ Live Face Skin Analysis (UI Ready)

UI scaffold prepared for future real-time skin analysis

Camera-based architecture already integrated

Clearly marked as Coming Soon

4️⃣ AI Beauty Assistant

Integrated chatbot (Botpress)

Answers skincare & makeup queries

Personalized beauty recommendations

5️⃣ Modern UI / UX

Clean card-based interface

Responsive layout

Feature selection dashboard

Side result panels for live analysis

🧠 Tech Stack
Frontend

HTML5

CSS3 (modern glassmorphism UI)

JavaScript (Fetch API)

Backend

Python (Flask)

OpenCV

MediaPipe Face Landmarker

NumPy

AI / ML

Facial landmark geometry analysis

Rule-based face shape classification

CNN-based skin analysis (photo upload)

Confidence scoring & stabilization logic

📂 Project Structure
beauty-product-recommendation-ai/
│
├── app.py
├── face_shape_live.py
├── face_shape_analyzer.py
├── face_landmarker.task
│
├── templates/
│   ├── feature_selection.html
│   ├── face_shape_live.html
│   ├── skin_analysis.html
│   ├── live_skin_analysis.html
│
├── static/
│   ├── face_shape_live.js
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

4️⃣ Run Flask App
python app.py

5️⃣ Open in Browser
http://127.0.0.1:5000/feature_selection.html

📸 Screenshots

(Add screenshots here in GitHub using drag & drop)

Suggested sections:

Feature Selection Page

Face Shape Live Analysis

Upload Skin Analysis

AI Beauty Assistant Chat

🧪 Accuracy & Limitations

Face shape analysis is based on geometric heuristics, not medical diagnosis

Skin analysis is indicative, not dermatological advice

Lighting & camera quality affect accuracy

Designed for educational & prototype use

🔮 Future Enhancements

True 3D face mesh rendering (AR-style surface mesh)

Personalized product recommendation engine

User profiles & history

Cloud deployment

Mobile-friendly camera optimization

🧑‍💻 Author

Prathamesh Shekade
B.Tech IT | AI & Data Science Enthusiast
Hackathon Finalist | AI Engineer Aspirant

GitHub: https://github.com/prathameshs2304

📜 License

This project is licensed for educational & demonstration purposes.# beauty-product-recommendation-ai
<img width="2047" height="1150" alt="image" src="https://github.com/user-attachments/assets/cd50dd20-d975-414c-b4a8-2fbd8536301b" />
<img width="2047" height="1092" alt="image" src="https://github.com/user-attachments/assets/07b64b45-36d0-4334-b08c-affe4cfc3611" />
<img width="1918" height="981" alt="image" src="https://github.com/user-attachments/assets/132890be-3ab1-454a-b0da-290c16d7b6d3" />


