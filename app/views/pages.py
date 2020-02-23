# coding: utf-8

from flask import Blueprint, render_template, url_for, current_app, send_from_directory, request
from app.parameter import menus, index_info, menus2page
from app.models import Notice
from app.db import db

app = Blueprint('pages', __name__)

@app.route('/')
def index():
	pages_info = menus2page.get('index', None)
	notices = db.session.query(Notice).filter_by(status=2).order_by(Notice._created_time.desc()).limit(5)
	pages_info['notices'] = notices
	return render_template('pages/index.html', menus = menus, pages_info = pages_info)

@app.route('/favicon.ico')
def get_favicon():
    return send_from_directory('static', 'favicon.ico')

@app.route('/pages/<page_name>')
def menu(page_name):
	pages_info = menus2page.get(page_name, None)
	if pages_info != None:
		if page_name == 'index':
			notices = db.session.query(Notice).filter_by(status=2).order_by(Notice._created_time.desc()).limit(5)
			pages_info['notices'] = notices
		return render_template('pages/' + page_name + '.html', menus = menus, pages_info = pages_info)
	else:
		return 'not found', 404

