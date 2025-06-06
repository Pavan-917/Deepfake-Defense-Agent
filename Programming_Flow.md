## 🧠 Deepfake Defense Agent – Programming Flow

---

### 🔁 **Step 1: Media Upload Interception**

Intercept file uploads from a front-end application and send them to the server.

#### 📂 `upload_handler.py`

```python
from flask import Flask, request, jsonify
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads/temp_originals'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/upload', methods=['POST'])
def handle_upload():
    file = request.files['file']
    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)
    
    # Trigger next steps (Face blurring, watermarking)
    process_media(filepath)
    
    return jsonify({"status": "uploaded", "file": file.filename})
```

---

### 🧑‍💻 **Step 2: Face Detection and Blurring**

Use OpenCV or a pretrained model (like Dlib or Mediapipe) for face detection, then apply blurring.

#### 📂 `face_blur.py`

```python
import cv2

def blur_faces(image_path, output_path):
    image = cv2.imread(image_path)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        face = image[y:y+h, x:x+w]
        face = cv2.GaussianBlur(face, (99, 99), 30)
        image[y:y+h, x:x+w] = face

    cv2.imwrite(output_path, image)
```

---

### 🧬 **Step 3: Dead Pixel Watermarking**

Introduce imperceptible modifications using a watermarking approach.

#### 📂 `dead_pixel_watermark.py`

```python
import cv2
import numpy as np
import random

def add_dead_pixel_watermark(image_path, output_path, seed=42):
    random.seed(seed)
    img = cv2.imread(image_path)
    h, w, _ = img.shape

    # Add few "dead pixels"
    for _ in range(10):
        x, y = random.randint(0, w-1), random.randint(0, h-1)
        img[y, x] = [0, 0, 0]  # Set to black (dead pixel)

    cv2.imwrite(output_path, img)
```

---

### 🔐 **Step 4: Store Temporarily + Secure Copy**

Keep original image only for a short time and move processed media to permanent store.

#### 📂 `storage_handler.py`

```python
import os
import shutil

TEMP_STORAGE = 'uploads/temp_originals'
PROCESSED_STORAGE = 'uploads/processed'

def move_to_permanent_storage(original_path, processed_path):
    if os.path.exists(original_path):
        os.remove(original_path)  # Delete original
    shutil.move(processed_path, os.path.join(PROCESSED_STORAGE, os.path.basename(processed_path)))
```

---

### 🔒 **Step 5: Screen Capture Prevention (Browser)**

#### 📂 `frontend/prevent_capture.js`

```javascript
document.addEventListener("keydown", function(e) {
    // Block Print Screen
    if (e.key === "PrintScreen") {
        navigator.clipboard.writeText("");
        alert("Screenshot blocked!");
        e.preventDefault();
    }
});

// Disable right click
document.addEventListener("contextmenu", function(e) {
    e.preventDefault();
});

// Blur when tab is inactive
document.addEventListener("visibilitychange", function() {
    if (document.hidden) {
        document.body.style.filter = "blur(10px)";
    } else {
        document.body.style.filter = "none";
    }
});
```

📝 **Note**: These methods can be bypassed by advanced users. On mobile, platform-specific SDKs offer more secure screen recording control.

---

### 🧩 **Step 6: Combine Workflow**

#### 📂 `process_media.py`

```python
from face_blur import blur_faces
from dead_pixel_watermark import add_dead_pixel_watermark
from storage_handler import move_to_permanent_storage

def process_media(filepath):
    blurred_path = filepath.replace(".jpg", "_blurred.jpg")
    watermarked_path = filepath.replace(".jpg", "_final.jpg")

    blur_faces(filepath, blurred_path)
    add_dead_pixel_watermark(blurred_path, watermarked_path)
    move_to_permanent_storage(filepath, watermarked_path)
```

---

## 📂 Folder Structure

```
dda_project/
├── app.py                  # Main Flask app
├── upload_handler.py       # Upload API
├── face_blur.py            # Face blurring logic
├── dead_pixel_watermark.py # Watermarking logic
├── storage_handler.py      # Handles storage logic
├── process_media.py        # Main pipeline
├── uploads/
│   ├── temp_originals/
│   └── processed/
└── frontend/
    └── prevent_capture.js  # Anti-screenshot frontend
```