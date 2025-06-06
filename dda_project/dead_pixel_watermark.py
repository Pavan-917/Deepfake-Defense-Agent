import cv2
import random

def add_dead_pixel_watermark(image_path, output_path, seed=42):
    random.seed(seed)
    is_video = image_path.endswith(('.mp4', '.avi'))
    if is_video:
        return image_path  # Skip video for now or apply watermarking frame-wise (optional)
    img = cv2.imread(image_path)
    h, w, _ = img.shape
    for _ in range(10):
        x, y = random.randint(0, w-1), random.randint(0, h-1)
        img[y, x] = [0, 0, 0]
    cv2.imwrite(output_path, img)