# coding: utf-8

from flask import current_app
from app.db import db
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.ext.hybrid import hybrid_property

from .UserPermission import check_route_permission
from app.libs.date_utils import as_timezone, utcnow

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
    _register_time = db.Column(db.DateTime, default=utcnow)

    @hybrid_property
    def register_time(self):
        return as_timezone(self._register_time)

    @register_time.expression
    def register_time(cls):
        return cls._register_time

    def __repr__(self):
        return '<User %r>' % self.username

    def permitted_role_choices(self):
        if self.role == 1:
            return [(2, '系统管理员'), (3, '普通管理员')]
        elif self.role == 2:
            return [(3, '普通管理员')]
        else:
            return []
    @classmethod
    def role_choices(cls):
        '''
        for wtforms.SelectField, 0 is not supported
        '''
        return [(1, '超级管理员'), (2, '系统管理员'), (3, '普通管理员')]
    def get_role_name(self):
        names = {1: '超级管理员', 2: '系统管理员', 3: '普通管理员'}
        return names.get(self.role)

    def get_role_by_name(self, role_name):
        for role, name in User.role_choices():
            if name == role_name:
                return role
        return 0

    def allow_role_name(self, role_name):
        role = self.get_role_by_name(role_name)
        return self.role <= role and role > 0

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
    def check_password(self, password):
        return check_password_hash(self.password, password)

    # Integration of flask-login
    @property
    def is_authenticated(self):
        return check_route_permission(self)
    @property
    def is_active(self):
        return True

    @property
    def is_admin(self):
        return self.role == 1 # TODO

    @property
    def is_anonymous(self):
        return False
    # required by flask-login
    def get_id(self):
        return self.id

    # Required for administrative interface?
    def __unicode__(self):
        return self.username

