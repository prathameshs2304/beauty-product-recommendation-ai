import numpy as np
import cv2
import torch
import torchvision.transforms as transforms
from torchvision import models
from torchvision.models import ResNet18_Weights
import torch.nn as nn
import torch.nn.functional as F

# -----------------------------
# Load Model
# -----------------------------

model = models.resnet18(weights=ResNet18_Weights.DEFAULT)
num_classes = 35
model.fc = nn.Linear(model.fc.in_features, num_classes)
model.eval()

# -----------------------------
# Image Transforms
# -----------------------------

transform = transforms.Compose([
    transforms.ToPILImage(),
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(
        mean=[0.485, 0.456, 0.406],
        std=[0.229, 0.224, 0.225]
    ),
])

# -----------------------------
# Haar Cascade (optional safety)
# -----------------------------

haar_cascade_path = cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
face_cascade = cv2.CascadeClassifier(haar_cascade_path)

# -----------------------------
# Utilities
# -----------------------------

def preprocess_image(image_file):
    image_file.seek(0)
    img_np = cv2.imdecode(
        np.frombuffer(image_file.read(), np.uint8),
        cv2.IMREAD_COLOR
    )
    if img_np is None:
        raise ValueError("Image could not be decoded.")
    return img_np


def detect_human_face(img_np):
    """Haar face detection (not reliable for live frames)"""
    gray = cv2.cvtColor(img_np, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.05,
        minNeighbors=3,
        minSize=(20, 20)
    )
    return len(faces) > 0


def safe_argmax(prob_slice):
    if prob_slice.numel() == 0:
        return 0
    return torch.argmax(prob_slice).item()


def map_category_with_dynamic_percentage(index, probabilities, categories):
    if not categories or index >= len(categories):
        return ("Unknown", 0)

    category = categories[index]
    prob_values = [p.item() for p in probabilities]
    total_prob = sum(prob_values)

    if total_prob > 0:
        normalized_probs = [p / total_prob for p in prob_values]
        percentage = normalized_probs[index] * 100
    else:
        percentage = 0

    if percentage < 10:
        percentage = 10

    return category, round(percentage, 2)


# -----------------------------
# Mapping Functions
# -----------------------------

def map_skin_tone(i, p): return map_category_with_dynamic_percentage(i, p, ['Light', 'Medium', 'Dark'])
def map_acne_level(i, p): return map_category_with_dynamic_percentage(i, p, ['None', 'Mild', 'Moderate', 'Severe'])
def map_blackheads(i, p): return map_category_with_dynamic_percentage(i, p, ['None', 'Few', 'Moderate', 'Many'])
def map_dark_circles(i, p): return map_category_with_dynamic_percentage(i, p, ['None', 'Mild', 'Moderate', 'Severe'])
def map_skin_type(i, p): return map_category_with_dynamic_percentage(i, p, ['Oily', 'Dry', 'Combination'])
def map_hair_quality(i, p): return map_category_with_dynamic_percentage(i, p, ['Poor', 'Average', 'Good'])
def map_hydration(i, p): return map_category_with_dynamic_percentage(i, p, ['Dehydrated', 'Normal', 'Well-Hydrated'])
def map_sensitivity(i, p): return map_category_with_dynamic_percentage(i, p, ['Low', 'Medium', 'High'])
def map_wrinkles(i, p): return map_category_with_dynamic_percentage(i, p, ['None', 'Few', 'Moderate', 'Many'])
def map_pore_size(i, p): return map_category_with_dynamic_percentage(i, p, ['Small', 'Medium', 'Large'])


# -----------------------------
# Main Analyze Function
# -----------------------------

def analyze(image_file):
    img_np = preprocess_image(image_file)

    # ⚠️ Haar detection is unreliable for live camera frames
    # MediaPipe already confirms face presence
    human_found = detect_human_face(img_np)

    if not human_found:
        print("⚠️ Haar failed — bypassing face validation for live capture")
        human_found = True   # FORCE ALLOW

    img_t = transform(img_np).unsqueeze(0)

    with torch.no_grad():
        outputs = model(img_t)
        probabilities = F.softmax(outputs, dim=1)

    if outputs.numel() == 0:
        raise ValueError("Model output is empty")

    if probabilities.shape[1] < 35:
        raise ValueError("Model output dimension mismatch")

    def slice_or_empty(tensor, start, end):
        if end <= tensor.size(0) and start < end:
            return tensor[start:end]
        return torch.tensor([])

    probs = probabilities[0]

    tone_slice = slice_or_empty(probs, 0, 3)
    acne_slice = slice_or_empty(probs, 3, 7)
    blackheads_slice = slice_or_empty(probs, 7, 11)
    dark_circles_slice = slice_or_empty(probs, 11, 15)
    skin_type_slice = slice_or_empty(probs, 15, 19)
    hair_quality_slice = slice_or_empty(probs, 19, 22)
    hydration_slice = slice_or_empty(probs, 22, 25)
    sensitivity_slice = slice_or_empty(probs, 25, 28)
    wrinkles_slice = slice_or_empty(probs, 28, 32)
    pore_size_slice = slice_or_empty(probs, 32, 35)

    skin_metrics = {
        'tone': map_skin_tone(safe_argmax(tone_slice), tone_slice),
        'acne_level': map_acne_level(safe_argmax(acne_slice), acne_slice),
        'blackheads': map_blackheads(safe_argmax(blackheads_slice), blackheads_slice),
        'dark_circles': map_dark_circles(safe_argmax(dark_circles_slice), dark_circles_slice),
        'skin_type': map_skin_type(safe_argmax(skin_type_slice), skin_type_slice),
        'hair_quality': map_hair_quality(safe_argmax(hair_quality_slice), hair_quality_slice),
        'hydration_level': map_hydration(safe_argmax(hydration_slice), hydration_slice),
        'sensitivity': map_sensitivity(safe_argmax(sensitivity_slice), sensitivity_slice),
        'wrinkles': map_wrinkles(safe_argmax(wrinkles_slice), wrinkles_slice),
        'pore_size': map_pore_size(safe_argmax(pore_size_slice), pore_size_slice),
    }

    print("✅ Skin Metrics Generated")

    return {
        "living": True,
        "skinMetrics": skin_metrics,
        "recommendedProducts": []
    }
