# my_model.py

import torch
import torch.nn as nn
from torchvision import transforms
from PIL import Image
import cv2
import os

# Example CNN architecture (match it to your trained model)
class SimpleCNN(nn.Module):
    def __init__(self):
        super(SimpleCNN, self).__init__()
        self.features = nn.Sequential(
            nn.Conv2d(3, 16, 3, padding=1),  # input: RGB
            nn.ReLU(),
            nn.MaxPool2d(2),
            nn.Conv2d(16, 32, 3, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(2),
        )
        self.classifier = nn.Sequential(
            nn.Flatten(),
            nn.Linear(32 * 64 * 64, 100),
            nn.ReLU(),
            nn.Linear(100, 1),  # Binary output
            nn.Sigmoid()
        )

    def forward(self, x):
        x = self.features(x)
        return self.classifier(x)

# Load model
def load_model(model_path="models/deepfake_model.pth"):
    model = SimpleCNN()
    if not os.path.exists(model_path):
        raise FileNotFoundError(f"Model file not found at: {model_path}")
    model.load_state_dict(torch.load(model_path, map_location=torch.device('cpu')))
    model.eval()
    return model

# Preprocessing
transform = transforms.Compose([
    transforms.Resize((256, 256)),
    transforms.CenterCrop((128, 128)),
    transforms.ToTensor()
])

# Extract first frame from video or image
def extract_frame(media_path):
    if media_path.endswith(('.mp4', '.avi', '.mov')):
        cap = cv2.VideoCapture(media_path)
        ret, frame = cap.read()
        cap.release()
        if ret:
            temp_path = "temp_frame.jpg"
            cv2.imwrite(temp_path, frame)
            return temp_path
    return media_path

# Predict using model
def predict(model, media_path):
    frame_path = extract_frame(media_path)
    img = Image.open(frame_path).convert("RGB")
    img_tensor = transform(img).unsqueeze(0)  # Add batch dimension
    with torch.no_grad():
        output = model(img_tensor)
    score = output.item()
    if frame_path == "temp_frame.jpg":
        os.remove(frame_path)
    return score  # Closer to 1 = deepfake, closer to 0 = real

model = load_model(r'D:\Pavan Kumar\Deepfake Defense\dda_project\models\deepfake_model.pth')
