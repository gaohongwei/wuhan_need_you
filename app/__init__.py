# coding: utf-8

import os
from flask_admin import Admin
from flask_ckeditor import CKEditor
from flask_sqlalchemy import SQLAlchemy
from app.models import User, Notice, register_route_permission, register_model_view_permission
from app.model_views import UserModelView, NoticeModelView, AdminIndexView, init_login, init_sample_users
from app.db import init_app
from app.config import create_app

# Initialize the app, APPLICATION_MODE can be one of 'depolyment', 'development', 'testing'
app = create_app(os.environ.get('APPLICATION_MODE'))

admin = Admin(app=app, name='后台管理', index_view=AdminIndexView(name='主页'))
ckeditor = CKEditor(app)

# Load the views
from app import views

# Load the config file
db = init_app(app)
login_manager = init_login(app)
admin.add_view(UserModelView(User, db.session, name='用户管理'))
admin.add_view(NoticeModelView(Notice, db.session, name='通知管理'))

register_route_permission('/admin/', '普通管理员')
register_route_permission('/admin/login/', '普通管理员')
register_route_permission('/admin/index/', '普通管理员')
register_route_permission('/admin/user/', '系统管理员')
register_route_permission('/admin/notice/', '普通管理员')

register_model_view_permission(UserModelView, '系统管理员')
register_model_view_permission(NoticeModelView, '普通管理员')

init_sample_users(app)

logger = app.logger
