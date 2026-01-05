import cv2
import time
import math
from statistics import median, pstdev

import mediapipe as mp
from mediapipe.tasks.python import vision
from mediapipe.tasks.python.core import base_options

MODEL_PATH = "face_landmarker.task"
REQUIRED_FRAMES = 25

# =============================
# GLOBAL RESULT STATE
# =============================
CURRENT_RESULT = None

# =============================
# UTILS
# =============================
def dist(a, b, w, h):
    return math.dist(
        (a.x * w, a.y * h),
        (b.x * w, b.y * h)
    )

def classify_face(width, height):
    ratio = width / height
    if ratio > 0.88:
        return "Round"
    if ratio < 0.75:
        return "Oval"
    return "Square"

# =============================
# LANDMARK INDEXES
# =============================
FOREHEAD = 10
CHIN = 152
LEFT_CHEEK = 234
RIGHT_CHEEK = 454

# =============================
# STREAM GENERATOR (SAFE)
# =============================
def generate_frames():
    global CURRENT_RESULT

    # ---- RESET STATE EVERY VISIT ----
    CURRENT_RESULT = None
    result_buffer = []

    # ---- CREATE LANDMARKER PER SESSION (IMPORTANT) ----
    options = vision.FaceLandmarkerOptions(
        base_options=base_options.BaseOptions(
            model_asset_path=MODEL_PATH
        ),
        running_mode=vision.RunningMode.VIDEO,
        num_faces=1
    )
    landmarker = vision.FaceLandmarker.create_from_options(options)

    cap = cv2.VideoCapture(0)
    timestamp_ms = 0

    try:
        while True:
            success, frame = cap.read()
            if not success:
                break

            h, w, _ = frame.shape
            rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            mp_image = mp.Image(
                image_format=mp.ImageFormat.SRGB,
                data=rgb
            )

            result = landmarker.detect_for_video(mp_image, timestamp_ms)
            timestamp_ms += 33

            if result.face_landmarks:
                lm = result.face_landmarks[0]

                # ---- DRAW POINTS ----
                for p in lm:
                    cv2.circle(
                        frame,
                        (int(p.x * w), int(p.y * h)),
                        1,
                        (255, 255, 255),
                        -1
                    )

                face_width = dist(lm[LEFT_CHEEK], lm[RIGHT_CHEEK], w, h)
                face_height = dist(lm[FOREHEAD], lm[CHIN], w, h)

                result_buffer.append({"w": face_width, "h": face_height})

                if len(result_buffer) >= REQUIRED_FRAMES and CURRENT_RESULT is None:
                    w_med = median(x["w"] for x in result_buffer)
                    h_med = median(x["h"] for x in result_buffer)

                    stability = pstdev(x["h"] for x in result_buffer) / h_med
                    confidence = int((1 - min(stability, 0.25)) * 100)

                    CURRENT_RESULT = {
                        "faceShape": classify_face(w_med, h_med),
                        "faceWidth": int(w_med),
                        "faceHeight": int(h_med),
                        "confidence": max(85, min(confidence, 99))
                    }

            ret, buffer = cv2.imencode(".jpg", frame)
            yield (
                b"--frame\r\n"
                b"Content-Type: image/jpeg\r\n\r\n"
                + buffer.tobytes()
                + b"\r\n"
            )

    finally:
        # ---- CLEANUP (THIS FIXES BLACK SCREEN) ----
        cap.release()
        landmarker.close()

# =============================
# RESULT API
# =============================
def get_face_shape_result():
    return CURRENT_RESULT
