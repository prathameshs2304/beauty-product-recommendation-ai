import math
from statistics import median, pstdev

import mediapipe as mp
from mediapipe.tasks.python import vision
from mediapipe.tasks.python.core import base_options


class FaceShapeAnalyzer:
    def __init__(self, model_path, required_frames=25):
        self.required_frames = required_frames
        self.buffer = []
        self.locked_result = None
        self.last_landmarks = None

        self.options = vision.FaceLandmarkerOptions(
            base_options=base_options.BaseOptions(
                model_asset_path=model_path
            ),
            running_mode=vision.RunningMode.VIDEO,
            num_faces=1
        )

        self.landmarker = vision.FaceLandmarker.create_from_options(
            self.options
        )

        # Landmark indices
        self.FOREHEAD = 10
        self.CHIN = 152
        self.LEFT_CHEEK = 234
        self.RIGHT_CHEEK = 454
        self.LEFT_JAW = 172
        self.RIGHT_JAW = 397
        self.LEFT_TEMPLE = 127
        self.RIGHT_TEMPLE = 356

        self.SYMMETRY_PAIRS = [
            (33, 263),
            (133, 362),
            (234, 454),
            (172, 397),
            (127, 356),
        ]

    # -----------------------------
    # Utilities
    # -----------------------------
    def _dist(self, a, b, w, h):
        return math.dist(
            (a.x * w, a.y * h),
            (b.x * w, b.y * h)
        )

    # -----------------------------
    # Face shape classifier
    # -----------------------------
    def _classify(self, m):
        h = m["height"]
        cheek = m["cheek"]
        jaw = m["jaw"]
        forehead = m["forehead"]

        ratio = cheek / h

        if abs(cheek - jaw) < 0.05 * h and ratio > 0.83:
            return "Round"
        if abs(cheek - jaw) < 0.06 * h and ratio >= 0.78:
            return "Square"
        if cheek > jaw and cheek > forehead:
            return "Diamond"
        if forehead > jaw and ratio < 0.75:
            return "Heart"

        return "Oval"

    # -----------------------------
    # Symmetry score (0–100)
    # -----------------------------
    def _symmetry_score(self, landmarks, w):
        xs = [lm.x * w for lm in landmarks]
        center_x = sum(xs) / len(xs)

        deviations = []
        for l, r in self.SYMMETRY_PAIRS:
            lx = landmarks[l].x * w
            rx = landmarks[r].x * w
            mirrored_rx = 2 * center_x - rx
            deviations.append(abs(lx - mirrored_rx))

        avg_dev = sum(deviations) / len(deviations)
        max_allowed = 0.12 * w

        score = max(0, 100 * (1 - avg_dev / max_allowed))
        return int(min(score, 100))

    # -----------------------------
    # Extra characteristics
    # -----------------------------
    def _extra_characteristics(self, m):
        h = m["height"]
        cheek = m["cheek"]
        jaw = m["jaw"]
        forehead = m["forehead"]

        jaw_strength = "Strong" if jaw / cheek > 0.88 else "Soft"
        face_length = "Long" if h / cheek > 1.35 else "Balanced"
        cheekbone = "Prominent" if cheek > forehead else "Subtle"

        return {
            "jawline": jaw_strength,
            "faceLength": face_length,
            "cheekbones": cheekbone
        }

    # -----------------------------
    # MAIN PROCESS
    # -----------------------------
    def process(self, frame, timestamp_ms):
        h, w, _ = frame.shape

        mp_image = mp.Image(
            image_format=mp.ImageFormat.SRGB,
            data=frame
        )

        result = self.landmarker.detect_for_video(
            mp_image, timestamp_ms
        )

        if not result.face_landmarks:
            return self.locked_result

        lm = result.face_landmarks[0]
        self.last_landmarks = lm

        if self.locked_result:
            return self.locked_result

        metrics = {
            "height": self._dist(lm[self.FOREHEAD], lm[self.CHIN], w, h),
            "cheek": self._dist(lm[self.LEFT_CHEEK], lm[self.RIGHT_CHEEK], w, h),
            "jaw": self._dist(lm[self.LEFT_JAW], lm[self.RIGHT_JAW], w, h),
            "forehead": self._dist(lm[self.LEFT_TEMPLE], lm[self.RIGHT_TEMPLE], w, h),
        }

        self.buffer.append(metrics)

        if len(self.buffer) < self.required_frames:
            return None

        heights = [x["height"] for x in self.buffer]
        variance = pstdev(heights)
        median_h = median(heights)

        stability = min(variance / median_h, 0.2)
        confidence = int(max(85, (1 - stability) * 100))

        med = {
            k: median([x[k] for x in self.buffer])
            for k in metrics
        }

        symmetry = self._symmetry_score(lm, w)
        extras = self._extra_characteristics(med)

        face_ratio = round(med["cheek"] / med["height"], 2)

        facial_balance = (
            "Balanced"
            if abs(med["cheek"] - med["forehead"]) < 0.08 * med["height"]
            else "Wide" if med["cheek"] > med["forehead"]
            else "Narrow"
        )

        dominant_zone = (
            "Mid Face"
            if med["cheek"] > med["jaw"] and med["cheek"] > med["forehead"]
            else "Lower Face" if med["jaw"] > med["cheek"]
            else "Upper Face"
        )

        self.locked_result = {
            "faceShape": self._classify(med),
            "faceWidth": int(med["cheek"]),
            "faceHeight": int(med["height"]),
            "faceRatio": face_ratio,
            "facialBalance": facial_balance,
            "shapeConfidence": confidence,
            "confidence": confidence,
            "explanation": "Based on stable facial landmark geometry"
        }

        return self.locked_result
