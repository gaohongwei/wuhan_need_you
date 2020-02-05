import sys
sys.path.insert(0, '../data')

from flask import render_template, request, send_from_directory
from flask_login import current_user
from app import app
from app.parameter import *
from app.models.Notice import Notice
from app.db import db

@app.route('/')
def index():
    return render_template('pages/index.html', menus = menus, pages_info = index_info)

@app.route('/notices')
def list_notices():
    page = request.args.get('page', 1, type=int)
    if current_user.is_authenticated:
        pagination = db.session.query(Notice).paginate(page, app.config['NOTICES_PER_PAGE'], False)
    else:
        pagination = db.session.query(Notice).filter_by(status=2).paginate(page, 2, False)
    notices = pagination.items
    return render_template('pages/notices.html', menus=menus, pages_info=pages_info, notices=notices, pagination=pagination)

@app.route('/notice/<notice_id>')
def get_notice(notice_id):
    notice = db.session.query(Notice).filter_by(id=notice_id).scalar()
    return render_template('pages/notice_detail.html', menus = menus, pages_info = pages_info, notice = notice)

@app.route('/favicon.ico')
def get_favicon():
    return send_from_directory('static', 'favicon.ico')

@app.route('/<page_name>')
def menu(page_name):
    pages_info = menus2page.get(page_name, None)
    if pages_info:
        return render_template('pages/' + page_name + '.html', menus = menus, pages_info = pages_info)
    else:
        return 'not found', 404
