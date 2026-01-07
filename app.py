from flask import Flask, jsonify, send_from_directory, Response, request
from flask_cors import CORS
import logging
import os

from face_shape_live import generate_frames, get_face_shape_result
from your_cnn_model import analyze   # ✅ REQUIRED for Option-2



app = Flask(__name__)
CORS(app)
logging.basicConfig(level=logging.DEBUG)

BASE_DIR = os.getcwd()

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
# OPTION 1: Face Shape Live Stream
# -----------------------------
@app.route("/face-shape-live")
def face_shape_live():
    return Response(
        generate_frames(),
        mimetype="multipart/x-mixed-replace; boundary=frame"
    )


@app.route("/face-shape-result")
def face_shape_result():
    result = get_face_shape_result()
    if result:
        return jsonify(result)
    return jsonify({"status": "processing"})

@app.route("/face-landmarks")
def face_landmarks():
    from face_shape_live import current_landmarks
    return jsonify(current_landmarks or [])



# -----------------------------
# OPTION 2: Upload Photo Skin Analysis (🔥 FIXED)
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
    app.run(debug=True, use_reloader=False)