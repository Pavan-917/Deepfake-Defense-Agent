from flask import Flask, request, jsonify, render_template, send_from_directory
from upload_handler import handle_upload
import os

app = Flask(__name__)
app.add_url_rule('/upload', 'upload', handle_upload, methods=['POST'])

@app.route('/')
def dashboard():
    files = os.listdir('uploads/processed')
    return render_template('dashboard.html', files=files)

@app.route('/uploads/processed/<filename>')
def uploaded_file(filename):
    return send_from_directory('uploads/processed', filename)

if __name__ == '__main__':
    app.run(debug=True)
