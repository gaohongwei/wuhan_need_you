from flask import render_template
from app import app
from app.menus import *
from app.info import *

@app.route('/')
def index():
	return render_template('pages/index.html', menus = menus)

@app.route('/<page_name>')
def menu(page_name):
	print(info)
	return render_template('pages/' + page_name + '.html', menus = menus, info = info)


