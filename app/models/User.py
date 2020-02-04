
from app.db import db
from app.libs.date_utils import utcnow
from werkzeug.security import generate_password_hash
from sqlalchemy.ext.hybrid import hybrid_property

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String, nullable=False)
    first_name = db.Column(db.String(80))
    last_name = db.Column(db.String(80))
    email = db.Column(db.String(120), unique=True)
    role = db.Column(db.Integer, nullable=False)
    # The time is stored without timezone info in database,
    # They are considered UTC
    # Remember to recover to local time when use them
    register_time = db.Column(db.DateTime, default=utcnow)

    def __repr__(self):
        return '<User %r>' % self.username

    @classmethod
    def role_choices(cls):
        '''
        for wtforms.SelectField, 0 is not supported
        '''
        return ((1, '超级管理员'), (2, '系统管理员'), (3, '普通管理员'))
    def get_role_name(self):
        names = {1: '超级管理员', 2: '系统管理员', 3: '普通管理员'}
        return names.get(self.role)

    @hybrid_property
    def password(self):
        '''
        return hashed password
        '''
        return self.password_hash

    # not set password directly
    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

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

