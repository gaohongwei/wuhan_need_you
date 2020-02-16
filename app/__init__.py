# coding: utf-8

import os
from flask_admin import Admin
from flask_wtf.csrf import CSRFProtect
from flask_ckeditor import CKEditor
from app.models import Tag, User, Notice, register_route_permission, register_model_view_permission, recreate_database
from app.model_views import TagModelView, UserModelView, NoticeModelView, AdminIndexView, VisitorModelView, init_login, init_sample_users
from app.model_views import MyFileAdmin
from app.db import init_app
from app.config import create_app
from app.filters import register_filters, register_processors
from app.views import register_blueprints
from app.listeners import register_after_requests, register_before_requests

# Load the config file
# Initialize the app, APPLICATION_MODE can be one of 'depolyment', 'development', 'testing'
app = create_app(os.environ.get('APPLICATION_MODE'))

admin = Admin(app=app, name='后台管理', index_view=AdminIndexView(name='主页'))
ckeditor = CKEditor(app)
csrf = CSRFProtect(app)

# Load the views
from app import views

db = init_app(app)

login_manager = init_login(app)
admin.add_view(UserModelView())
admin.add_view(NoticeModelView())
admin.add_view(TagModelView())
admin.add_view(VisitorModelView())
admin.add_view(MyFileAdmin(app))

register_blueprints(app)
register_after_requests(app)
register_before_requests(app)
register_filters(app)
register_processors(app)

register_route_permission('/admin/', '普通管理员')
register_route_permission('/admin/login/', '普通管理员')
register_route_permission('/admin/index/', '普通管理员')
register_route_permission('/admin/user/', '系统管理员')
register_route_permission('/admin/user/details/', '普通管理员')
register_route_permission('/admin/user/edit/', '普通管理员')
register_route_permission('/admin/user/new/', '普通管理员')
register_route_permission('/admin/user/delete/', '系统管理员')
register_route_permission('/admin/notice/', '普通管理员')
register_route_permission('/admin/notice/new/', '普通管理员')
register_route_permission('/admin/notice/edit/', '普通管理员')
register_route_permission('/admin/notice/delete/', '普通管理员')
register_route_permission('/admin/notice/details/', '普通管理员')
register_route_permission('/admin/notice/action/', '系统管理员')
register_route_permission('/admin/notice/preview', '普通管理员')
register_route_permission('/admin/notice/ajax/lookup/', '普通管理员')
register_route_permission('/admin/tag/', '系统管理员')
register_route_permission('/admin/tag/edit/', '系统管理员')
register_route_permission('/admin/tag/details/', '系统管理员')
register_route_permission('/admin/tag/new/', '系统管理员')
register_route_permission('/admin/tag/delete/', '系统管理员')
register_route_permission('/admin/myfileadmin/', '普通管理员')
register_route_permission('/admin/myfileadmin/*/*', '普通管理员')
register_route_permission('/admin/visitor/', '系统管理员')

register_model_view_permission(UserModelView, '系统管理员')
register_model_view_permission(NoticeModelView, '普通管理员')
register_model_view_permission(TagModelView, '系统管理员')
register_model_view_permission(MyFileAdmin, '普通管理员')
register_model_view_permission(VisitorModelView, '系统管理员')

recreate_database(app)

logger = app.logger
