import os
from flask import request, jsonify
from process_media import process_media

UPLOAD_FOLDER = 'uploads/temp_originals'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def handle_upload():
    file = request.files['file']
    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)

    process_media(filepath)
    return jsonify({"status": "uploaded", "file": file.filename})