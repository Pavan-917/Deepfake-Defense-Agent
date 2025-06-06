import os
import shutil

TEMP_STORAGE = 'uploads/temp_originals'
PROCESSED_STORAGE = 'uploads/processed'
os.makedirs(PROCESSED_STORAGE, exist_ok=True)

def move_to_permanent_storage(original_path, processed_path):
    if os.path.exists(original_path):
        os.remove(original_path)
    shutil.move(processed_path, os.path.join(PROCESSED_STORAGE, os.path.basename(processed_path)))