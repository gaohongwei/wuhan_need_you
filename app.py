# coding=utf-8

import os
from flask import *
from flask_sqlalchemy import SQLAlchemy

print(__name__)
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/whu'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

# db.create_all()
# admin = User(username='admin', email='admin@example.com')
# guest = User(username='guest', email='guest@example.com')
# db.session.add(admin)
# db.session.add(guest)
# db.session.commit()


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