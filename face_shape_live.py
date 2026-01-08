import cv2
import math
from statistics import median, pstdev
import numpy as np

import mediapipe as mp
from mediapipe.tasks.python import vision
from mediapipe.tasks.python.core import base_options

MODEL_PATH = "face_landmarker.task"
REQUIRED_FRAMES = 10   # lower for faster response

# =============================
# INIT LANDMARKER (ONCE)
# =============================
options = vision.FaceLandmarkerOptions(
    base_options=base_options.BaseOptions(
        model_asset_path=MODEL_PATH
    ),
    running_mode=vision.RunningMode.IMAGE,
    num_faces=1
)
landmarker = vision.FaceLandmarker.create_from_options(options)

# =============================
# BUFFER STATE PER SESSION
# =============================
result_buffer = []

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
# MAIN PROCESS FUNCTION
# =============================
def analyze_frame(frame):
    """
    frame: OpenCV BGR image from browser
    returns: dict or None
    """
    global result_buffer

    h, w, _ = frame.shape
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    mp_image = mp.Image(
        image_format=mp.ImageFormat.SRGB,
        data=rgb
    )

    result = landmarker.detect(mp_image)

    if not result.face_landmarks:
        return None

    lm = result.face_landmarks[0]

    face_width = dist(lm[LEFT_CHEEK], lm[RIGHT_CHEEK], w, h)
    face_height = dist(lm[FOREHEAD], lm[CHIN], w, h)

    result_buffer.append({"w": face_width, "h": face_height})

    # Keep buffer small
    if len(result_buffer) > REQUIRED_FRAMES:
        result_buffer.pop(0)

    # Wait until buffer fills
    if len(result_buffer) < REQUIRED_FRAMES:
        return None

    w_med = median(x["w"] for x in result_buffer)
    h_med = median(x["h"] for x in result_buffer)

    stability = pstdev(x["h"] for x in result_buffer) / h_med
    confidence = int((1 - min(stability, 0.25)) * 100)

    return {
        "faceShape": classify_face(w_med, h_med),
        "faceWidth": int(w_med),
        "faceHeight": int(h_med),
        "confidence": max(85, min(confidence, 99))
    }
