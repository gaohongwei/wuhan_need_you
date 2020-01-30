# coding=utf-8

import os
from flask import *


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/info_request', methods=['POST'])
def info_request():
	if request.method == 'POST':
		file_name = request.form['title'] + ".json"
		root = os.path.realpath(os.path.dirname(__file__))
		json_url = os.path.join(root, "data", file_name)
		data = json.load(open(json_url))
		return data

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)