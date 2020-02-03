
from app.db import db

class User(db.Model):
    __table_name__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(80), unique=True, nullable=False)
    username = db.Column(db.String(80), unique=True)
    first_name = db.Column(db.String(80))
    last_name = db.Column(db.String(80))
    email = db.Column(db.String(120), unique=True)
    role = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

    # Integration of flask-login
    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True
    
    @property
    def is_admin(self):
        return self.role == 'admin'

    @property
    def is_anonymous(self):
        return False

    # required by flask-login
    def get_id(self):
        return self.id

    # Required for administrative interface?
    def __unicode__(self):
        return self.username

