from flask import Flask, jsonify, send_from_directory, request
from flask_cors import CORS
import logging
import os
import cv2
import numpy as np

from face_shape_live import analyze_frame
from your_cnn_model import analyze   # Skin analysis


app = Flask(__name__)
CORS(app)
logging.basicConfig(level=logging.DEBUG)

BASE_DIR = os.getcwd()

# -----------------------------
# ✅ Disable Browser Cache (Prevents stale JS)
# -----------------------------
@app.after_request
def add_no_cache_headers(response):
    response.headers["Cache-Control"] = "no-store"
    return response


# -----------------------------
# Home Page
# -----------------------------
@app.route("/")
def home():
    return send_from_directory(BASE_DIR, "index.html")


# -----------------------------
# Serve all HTML / CSS / JS / Images
# -----------------------------
@app.route("/<path:filename>")
def serve_static(filename):
    return send_from_directory(BASE_DIR, filename)


# -----------------------------
# Face Shape Frame Analyzer (Browser Camera)
# -----------------------------
@app.route("/analyze-frame", methods=["POST"])
def analyze_frame_api():
    if "image" not in request.files:
        return jsonify({"error": "No image uploaded"}), 400

    file = request.files["image"]
    img_bytes = file.read()

    np_img = np.frombuffer(img_bytes, np.uint8)
    frame = cv2.imdecode(np_img, cv2.IMREAD_COLOR)

    if frame is None:
        return jsonify({"error": "Invalid image"}), 400

    try:
        result = analyze_frame(frame)
        return jsonify(result or {"status": "processing"})
    except Exception as e:
        logging.exception("Frame analysis failed")
        return jsonify({"error": str(e)}), 500


# -----------------------------
# Skin Analysis (UNCHANGED)
# -----------------------------
@app.route("/analyze-skin", methods=["POST"])
def analyze_skin():
    if "image" not in request.files:
        return jsonify({"error": "No image uploaded"}), 400

    image_file = request.files["image"]

    try:
        result = analyze(image_file)
        return jsonify(result)
    except Exception as e:
        logging.exception("Skin analysis failed")
        return jsonify({"error": str(e)}), 500


# -----------------------------
# Run App
# -----------------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True, use_reloader=False)
