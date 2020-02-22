# coding: utf-8

from flask import Blueprint, request, render_template, send_from_directory
from flask_login import current_user
from app.models import Notice, Comment
from app.db import db
from app.parameter import menus

app = Blueprint('notices', __name__)

@app.route('/notices')
def list_notices():
    page = request.args.get('page', 1, type=int)
    if current_user.is_authenticated:
        pagination = db.session.query(Notice).paginate(page, app.config['NOTICES_PER_PAGE'], False)
    else:
        # filter_by status should be 2
        pagination = db.session.query(Notice).filter_by(status=0).order_by(Notice._created_time.desc()).paginate(page, 10, False)
    return render_template('pages/notices.html', menus=menus, pagination=pagination)

@app.route('/notices/<notice_id>')
def get_notice(notice_id):
    notice = db.session.query(Notice).filter_by(id=notice_id).scalar()
    comments = Comment.get_comments_by_noticeid(notice_id)
    if notice == None:
        return 'not found', 404
    return render_template('pages/notice_detail.html', menus=menus, notice=notice, comments=comments)

