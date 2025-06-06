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
