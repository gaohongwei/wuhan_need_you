from flask import render_template
from app import app
from parameter import *

@app.route('/')
def index():
	return render_template('pages/index.html', menus = menus)

@app.route('/<page_name>')
def menu(page_name):
	return render_template('pages/' + page_name + '.html', menus = menus)


