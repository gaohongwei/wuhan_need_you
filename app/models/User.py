
from app import db

class User(db.Model):
    __table_name__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    role = db.Column(db.String, nullable=False)
    password_hash = db.Column(db.String, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username
