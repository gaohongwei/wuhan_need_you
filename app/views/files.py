# coding: utf-8

import os
from flask import Blueprint, render_template, url_for, current_app, send_from_directory, request
from flask_ckeditor import upload_fail, upload_success

app = Blueprint('files', __name__)

@app.route('/upload/<path:path>')
def get_upload(path):
    return send_from_directory('static/upload', path)

@app.route('/files/<path:filename>')
def uploaded_files(filename):
    path = 'static/upload'
    return send_from_directory(path, filename)

@app.route('/upload', methods=['POST'])
def upload():
    f = request.files.get('upload')
    # Add more validations here
    extension = f.filename.split('.')[1].lower()
    if extension not in ['jpg', 'gif', 'png', 'jpeg']:
        return upload_fail(message='Image only!')
    f.save(os.path.join(current_app.config['IMAGE_FILE_UPLOAD_DIRECTORY'], f.filename))
    url = url_for('uploaded_files', filename=f.filename)
    return upload_success(url=url)  # return upload_success call

