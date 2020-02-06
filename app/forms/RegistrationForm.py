
from wtforms import form, fields, validators
from app.db import db
from app.models import User

class RegistrationForm(form.Form):
    username = fields.StringField(label='登录名', validators=[validators.required()])
    password = fields.PasswordField(label='密码', validators=[validators.required()])
    email = fields.StringField(label='邮箱')

    def validate_username(self, field):
        if db.session.query(User).filter_by(username=self.username.data).count() > 0:
            raise validators.ValidationError('用户名冲突')
