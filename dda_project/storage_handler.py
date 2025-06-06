import os
import shutil

TEMP_STORAGE = 'uploads/temp_originals'
PROCESSED_STORAGE = 'uploads/processed'

def move_to_permanent_storage(original_path, processed_path):
    if os.path.exists(original_path):
        os.remove(original_path)  # Delete original
    shutil.move(processed_path, os.path.join(PROCESSED_STORAGE, os.path.basename(processed_path)))
