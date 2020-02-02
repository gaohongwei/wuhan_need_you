import sys
sys.path.insert(0, '../data')

from flask import render_template
from app import app
from app.parameter import *
# from app.notices import *

@app.route('/')
def index():
	return render_template('pages/index.html', menus = menus, pages_info = pages_info)

@app.route('/favicon.ico')
def favicon():

	# Add favicon
	return ''

@app.route('/notices')
def list_notices():
	total_page =20
	cur_page = 1


	return render_template('pages/notices.html', menus = menus, pages_info = pages_info, notices = notices)

@app.route('/<page_name>')
def menu(page_name):
	return render_template('pages/' + page_name + '.html', menus = menus, pages_info = pages_info)



