from face_blur import blur_faces
from dead_pixel_watermark import add_dead_pixel_watermark
from storage_handler import move_to_permanent_storage
from deepfake_detection import detect_deepfake
import os

def process_media(filepath):
    filename = os.path.basename(filepath)
    base, ext = os.path.splitext(filename)

    blurred_path = filepath.replace(ext, '_blurred' + ext)
    watermarked_path = filepath.replace(ext, '_final' + ext)

    blur_faces(filepath, blurred_path)
    add_dead_pixel_watermark(blurred_path, watermarked_path)
    result = detect_deepfake(watermarked_path)
    move_to_permanent_storage(filepath, watermarked_path)
    print(f"Deepfake Detection Result: {result}")