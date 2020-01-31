
from flask import render_template
from app import app


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/donate')
def donate():
    return render_template('donate.html')

@app.route('/supply')
def supply():
    return render_template('supply.html')

@app.route('/info')
def info():
    return render_template('info.html')

@app.route('/info_request', methods=['POST'])
def info_request():
	if request.method == 'POST':
		file_name = request.form['title'] + ".json"
		root = os.path.realpath(os.path.dirname(__file__))
		json_url = os.path.join(root, "data", file_name)
		data = json.load(open(json_url))
		return data