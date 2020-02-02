
from wtforms import form, fields, validators
from app.db import db
from app.models import User

class RegistrationForm(form.Form):
    login = fields.StringField(label='登陆名', validators=[validators.required()])
    email = fields.StringField(label='邮箱')
    password = fields.PasswordField(label='密码', validators=[validators.required()])

    def validate_login(self, field):
        if db.session.query(User).filter_by(login=self.login.data).count() > 0:
            raise validators.ValidationError('Duplicate username')
