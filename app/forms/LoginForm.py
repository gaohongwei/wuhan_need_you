
from wtforms import form, fields, validators
from werkzeug.security import check_password_hash
from app.models import User
from app.db import db

class LoginForm(form.Form):
    login = fields.StringField(label='登陆名', validators=[validators.required()])
    password = fields.PasswordField(label='密码', validators=[validators.required()])

    def validate_login(self, field):
        user = self.get_user()

        if user is None:
            raise validators.ValidationError('非法用户')

        # we're comparing the plaintext pw with the the hash from the db
        if not check_password_hash(user.password, self.password.data):
        # to compare plain text passwords use
        # if user.password != self.password.data:
            raise validators.ValidationError('密码错误')

    def get_user(self):
        return db.session.query(User).filter_by(login=self.login.data).first()
