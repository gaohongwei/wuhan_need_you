# coding: utf-8

from flask_admin.contrib import sqla
from wtforms import PasswordField, TextField, SelectField, validators
import flask_login as login
from app.models import User
from app.db import db
from app.libs.date_utils import as_timezone
from app.libs.wtforms_utils import select_field

class UserModelView(sqla.ModelView):
    column_labels = {
            'username': '用户名',
            'first_name': '名',
            'last_name': '姓',
            'email': '电子邮件',
            'role': '角色',
            'register_time': '注册时间',
            'password': '密码'
            }
    page_size = 10
    can_view_details = True
    column_details_exclude_list = ['password', 'password_hash']
    column_detail_list = ['username', 'first_name', 'last_name', 'email', 'role', 'register_time']

    column_exclude_list = ['password', 'password_hash']
    column_editable_list = ['username', 'password', 'first_name', 'last_name', 'email', 'role']
    form_excluded_columns = ['register_time']
    form_columns = ['username', 'password', 'first_name', 'last_name', 'email', 'role']
    form_extra_fields = {
            'username': TextField('登陆名', [validators.required()]),
            'first_name': TextField('名', [validators.required()]),
            'last_name': TextField('姓', [validators.required()]),
            'password': PasswordField('密码', [validators.required()]),
            'email': TextField('电子邮件', [validators.required()]),
            'role': SelectField('角色', [validators.required()], choices=User.role_choices(), coerce=int)
            }
    def _time_formatter(view, context, model, name):
        time = getattr(model, name)
        return as_timezone(time)
    def _role_formatter(view, context, model, name):
        return model.get_role_name()
    column_formatters = {
        'register_time': _time_formatter,
        'role': _role_formatter
    }
    def is_accessible(self):
        return login.current_user.is_authenticated

# init flask-login
def init_login(app):
    login_manager = login.LoginManager()
    login_manager.init_app(app)

    # Create user loader function
    @login_manager.user_loader
    def load_user(user_id):
        return db.session.query(User).get(user_id)
    return login_manager

def _init_sample_users():
    import string
    import random

    db.drop_all()
    db.create_all()
    # passwords are hashed, to use plaintext passwords instead:
    # test_user = User(username="test", password="test")
    test_user = User(username="test", role=1, password="test")
    db.session.add(test_user)

    first_names = [
        'Harry', 'Amelia', 'Oliver', 'Jack', 'Isabella', 'Charlie','Sophie', 'Mia',
        'Jacob', 'Thomas', 'Emily', 'Lily', 'Ava', 'Isla', 'Alfie', 'Olivia', 'Jessica',
        'Riley', 'William', 'James', 'Geoffrey', 'Lisa', 'Benjamin', 'Stacey', 'Lucy'
    ]
    last_names = [
        'Brown', 'Smith', 'Patel', 'Jones', 'Williams', 'Johnson', 'Taylor', 'Thomas',
        'Roberts', 'Khan', 'Lewis', 'Jackson', 'Clarke', 'James', 'Phillips', 'Wilson',
        'Ali', 'Mason', 'Mitchell', 'Rose', 'Davis', 'Davies', 'Rodriguez', 'Cox', 'Alexander'
    ]

    for i in range(len(first_names)):
        user = User()
        user.first_name = first_names[i]
        user.last_name = last_names[i]
        user.username = user.first_name.lower()
        user.email = user.username + "@example.com"
        user.role = 1
        user.password = ''.join(random.choice(string.ascii_lowercase + string.digits) for i in range(10))
        db.session.add(user)

    db.session.commit()

def init_sample_users(app):
    with app.app_context():
        _init_sample_users()

