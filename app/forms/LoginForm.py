# coding: utf-8

from wtforms import form, fields, validators
from app.models import User
from app.db import db

class LoginForm(form.Form):
    username = fields.StringField(label='登录名', validators=[validators.required()])
    password = fields.PasswordField(label='密码', validators=[validators.required()])

    def validate_password(self, field):
        user = self.get_user()

        if user is None:
            raise validators.ValidationError('非法用户')

        # we're comparing the plaintext pw with the the hash from the db
        if not user.check_password(self.password.data):
            raise validators.ValidationError('密码错误')

    def get_user(self):
        return db.session.query(User).filter_by(username=self.username.data).first()
