# coding: utf-8

from flask import Blueprint, request, render_template, send_from_directory
from flask_login import current_user
from app.models import Notice
from app.db import db
from app.parameter import menus

app = Blueprint('notices', __name__)

@app.route('/notices')
def list_notices():
    page = request.args.get('page', 1, type=int)
    if current_user.is_authenticated:
        pagination = db.session.query(Notice).paginate(page, app.config['NOTICES_PER_PAGE'], False)
    else:
        pagination = db.session.query(Notice).filter_by(status=2).paginate(page, 2, False)
    notices = pagination.items
    return render_template('pages/notices.html', menus=menus, notices=notices, pagination=pagination)

@app.route('/notices/<notice_id>')
def get_notice(notice_id):
    notice = db.session.query(Notice).filter_by(id=notice_id).scalar()
    if notice == None:
        return 'not found', 404
    return render_template('pages/notice_detail.html', menus = menus, notice = notice)

