# coding: utf-8

import sys
import os
sys.path.insert(0, '../data')

from flask import render_template, request, send_from_directory, url_for
from flask_login import current_user
from flask_ckeditor import upload_fail, upload_success
from app import app
from app.parameter import *
from app.models import Notice
from app.models import Visitor
from app.db import db
from app.libs.api_utils import get_realtime_overall

@app.route('/')
def index():
    return render_template('pages/index.html', menus = menus, pages_info = index_info)

@app.route('/api/realtime/overall')
def api_realtime_overall():
    return get_realtime_overall()

@app.route('/notices')
def list_notices():
    page = request.args.get('page', 1, type=int)
    if current_user.is_authenticated:
        pagination = db.session.query(Notice).paginate(page, app.config['NOTICES_PER_PAGE'], False)
    else:
        pagination = db.session.query(Notice).filter_by(status=2).paginate(page, 2, False)
    notices = pagination.items
    return render_template('pages/notices.html', menus=menus, notices=notices, pagination=pagination)

@app.route('/notice/<notice_id>')
def get_notice(notice_id):
    notice = db.session.query(Notice).filter_by(id=notice_id).scalar()
    if notice == None:
        return 'not found', 404
    return render_template('pages/notice_detail.html', menus = menus, notice = notice)

@app.route('/favicon.ico')
def get_favicon():
    return send_from_directory('static', 'favicon.ico')

@app.route('/reports')
def test_report():
    return render_template('pages/report_overall.html', menus = menus, pages_info = report_info)

@app.route('/upload/<path:path>')
def get_upload(path):
    return send_from_directory('static/upload', path)

@app.route('/pages/<page_name>')
def menu(page_name):
    pages_info = menus2page.get(page_name, None)
    if pages_info != None:
        return render_template('pages/' + page_name + '.html', menus = menus, pages_info = pages_info)
    else:
        return 'not found', 404

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
    f.save(os.path.join(app.config['IMAGE_FILE_UPLOAD_DIRECTORY'], f.filename))
    url = url_for('uploaded_files', filename=f.filename)
    return upload_success(url=url)  # return upload_success call

@app.after_request
def after_request(response):
    url = request.path
    Visitor.add()
    return response
