# coding: utf-8

from flask_admin.contrib import sqla
from wtforms import PasswordField, TextField, SelectField, validators
import flask_login as login
from app.models import User, check_permission
from app.db import db
from app.libs.date_utils import as_timezone
from app.libs.wtforms_utils import select_field

def get_choices():
    if login.current_user == None:
        return []
    return login.current_user.permitted_role_choices()

class UserModelView(sqla.ModelView):
    list_template = 'admin/list_user.html'
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
    column_editable_list = ['username', 'first_name', 'last_name', 'email']
    form_excluded_columns = ['register_time']
    form_columns = ['username', 'password', 'first_name', 'last_name', 'email', 'role']
    form_extra_fields = {
            'username': TextField('登陆名', [validators.required()]),
            'first_name': TextField('名', [validators.required()]),
            'last_name': TextField('姓', [validators.required()]),
            'password': PasswordField('密码', [validators.required()]),
            'email': TextField('电子邮件', [validators.required()]),
            'role': SelectField('角色', [validators.required()],
                choices=[],
                coerce=int)
            }
    # override to dynamically create choices
    def create_form(self):
        form = super().create_form()
        choices = get_choices()
        form.role.choices = choices
        return form
    def _time_formatter(view, context, model, name):
        time = getattr(model, name)
        return as_timezone(time)
    def _role_formatter(view, context, model, name):
        return model.get_role_name()
    column_formatters = {
        'register_time': _time_formatter,
        'role': _role_formatter
    }
    # required by flask-admin
    def is_accessible(self):
        return check_permission(self, login.current_user)

# init flask-login
def init_login(app):
    login_manager = login.LoginManager()
    login_manager.init_app(app)

    # Create user loader function
    @login_manager.user_loader
    def load_user(user_id):
        return db.session.query(User).get(user_id)
    return login_manager

def init_admin_user(app):
    with app.app_context():
        db.drop_all()
        db.create_all()
        admin_user = User(username="admin", role=1, password="admin")
        db.session.add(admin_user)
        db.session.commit()

def init_sample_users(app):
    with app.app_context():
        db.drop_all()
        db.create_all()
        test_user = User(username="test", role=1, password="test")
        db.session.add(test_user)
        test_user = User(username="test2", role=2, password="test2")
        db.session.add(test_user)
        test_user = User(username="test3", role=3, password="test3")
        db.session.add(test_user)
        db.session.commit()
