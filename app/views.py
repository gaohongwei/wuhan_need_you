import sys
sys.path.insert(0, '../data')

from flask import render_template, send_from_directory
from app import app
from app.parameter import *
# from app.notices import *

@app.route('/')
def index():
    return render_template('pages/index.html', menus = menus, pages_info = index_info)

@app.route('/notices')
def list_notices():
    total_page =20
    cur_page = 1
    return render_template('pages/notices.html', menus = menus, notices = notices)

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

