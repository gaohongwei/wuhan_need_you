from flask import render_template
from app import app
from parameter import *

@app.route('/')
def index():
	return render_template('pages/index.html', menus = menus)

@app.route('/<page_name>')
def menu(page_name):
	return render_template('pages/' + page_name + '.html', menus = menus)

@app.route('/info')
def info():
	# db = app.config["db"]
	#info = db.get_info()
	# a mock info obj list
	info = [
		{
			title: "mock1",
			desc: "something"
		},
		{
			title: "mock 2",
			desc: "something"
		}
	];
	return render_template("info.html", info)

