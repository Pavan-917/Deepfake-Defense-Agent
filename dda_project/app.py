from flask import Flask, request, jsonify
from upload_handler import handle_upload

app = Flask(__name__)
app.add_url_rule('/upload', 'upload', handle_upload, methods=['POST'])

if __name__ == '__main__':
    app.run(debug=True)