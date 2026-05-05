from flask import Blueprint, request, jsonify
import os
from config import UPLOAD_FOLDER

upload_bp = Blueprint('upload', __name__)

@upload_bp.route('/', methods=['POST'])
def upload():
    file = request.files['file']
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
    path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(path)
    return jsonify({'msg':'Uploaded', 'file': file.filename})
