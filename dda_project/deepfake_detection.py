# deepfake_detection.py

from my_model import load_model, predict

model = load_model()

def detect_deepfake(media_path):
    score = predict(model, media_path)
    return "Deepfake" if score > 0.5 else "Authentic"
