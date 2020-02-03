
from app.db import db
from app.libs.date_utils import utcnow

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(80), unique=True, nullable=False)
    username = db.Column(db.String(80), unique=True)
    first_name = db.Column(db.String(80))
    last_name = db.Column(db.String(80))
    email = db.Column(db.String(120), unique=True)
    role = db.Column(db.Integer, nullable=False)
    password = db.Column(db.String, nullable=False)
    # The time is stored without timezone info in database,
    # They are considered UTC
    # Remember to recover to local time when use them
    register_time = db.Column(db.DateTime, default=utcnow)

    def __repr__(self):
        return '<User %r>' % self.username

    def get_role_name(self):
        names = ['超级管理员', '系统管理员', '普通管理员']
        if role < 0:
            return names[0]
        if role > len(names):
            return names[-1]
        return names[role]

    # Integration of flask-login
    @property
    def is_authenticated(self):
        return True
    @property
    def is_active(self):
        return True
    @property
    def is_anonymous(self):
        return False
    # required by flask-login
    def get_id(self):
        return self.id

    # Required for administrative interface?
    def __unicode__(self):
        return self.username

