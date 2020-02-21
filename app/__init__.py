# coding: utf-8

import os
from flask_admin import Admin
from flask import request
from flask_babelex import Babel
from flask_wtf.csrf import CSRFProtect
from flask_ckeditor import CKEditor
from app.models import Tag, User, Notice, register_route_permission, register_model_view_permission, recreate_database
from app.model_views import TagModelView, UserModelView, NoticeModelView, AdminIndexView, VisitorModelView, CommentModelView, init_login, init_sample_users
from app.model_views import MyFileAdmin
from app.db import init_db
from app.config import app_from_config
from app.filters import register_filters, register_processors
from app.views import register_blueprints
from app.listeners import register_after_requests, register_before_requests
from app.cli import register_commands

def init_management(app):
    admin = Admin(app=app, name='后台管理', index_view=AdminIndexView(name='主页'))
    ckeditor = CKEditor(app)
    csrf = CSRFProtect(app)
    login_manager = init_login(app)
    admin.add_view(UserModelView())
    admin.add_view(NoticeModelView())
    admin.add_view(TagModelView())
    admin.add_view(VisitorModelView())
    admin.add_view(MyFileAdmin(app))
    admin.add_view(CommentModelView())

    return {'admin': admin, 'ckeditor': ckeditor, 'csrf': csrf, 'login_manager': login_manager}

def init_i8n(app):
    # Use Flask Babel to support multi-languages
    babel = Babel(app)
    @babel.localeselector
    def get_locale():
        return request.accept_languages.best_match(app.config['LANGUAGES'])
    return {'babel': babel}

def init_views(app):
    # Load the views
    from app import views
    register_blueprints(app)

route_permissions = [
        ('/admin/', '普通管理员'),
        ('/admin/login/', '普通管理员'),
        ('/admin/index/', '普通管理员'),
        ('/admin/user/', '系统管理员'),
        ('/admin/user/details/', '普通管理员'),
        ('/admin/user/edit/', '普通管理员'),
        ('/admin/user/new/', '普通管理员'),
        ('/admin/user/delete/', '系统管理员'),
        ('/admin/notice/', '普通管理员'),
        ('/admin/notice/new/', '普通管理员'),
        ('/admin/notice/edit/', '普通管理员'),
        ('/admin/notice/delete/', '普通管理员'),
        ('/admin/notice/details/', '普通管理员'),
        ('/admin/notice/action/', '系统管理员'),
        ('/admin/notice/preview', '普通管理员'),
        ('/admin/notice/ajax/lookup/', '普通管理员'),
        ('/admin/tag/', '系统管理员'),
        ('/admin/tag/edit/', '系统管理员'),
        ('/admin/tag/details/', '系统管理员'),
        ('/admin/tag/new/', '系统管理员'),
        ('/admin/tag/delete/', '系统管理员'),
        ('/admin/myfileadmin/', '普通管理员'),
        ('/admin/myfileadmin/*/*', '普通管理员'),
        ('/admin/visitor/', '系统管理员'),
        ('/admin/comment/', '普通管理员'),
        ('/admin/comment/delete/', '普通管理员')
        ]
modelview_permissions = [
        (UserModelView, '系统管理员'),
        (NoticeModelView, '普通管理员'),
        (TagModelView, '系统管理员'),
        (MyFileAdmin, '普通管理员'),
        (VisitorModelView, '系统管理员'),
        (CommentModelView, '普通管理员')
        ]

def init_permissions():
    for route,role in route_permissions:
        register_route_permission(route, role)
    for modelview,role in modelview_permissions:
        register_model_view_permission(modelview, role)

def init_database(app):
    db = init_db(app)
    recreate_database(app)

def init_flask(app):
    register_after_requests(app)
    register_before_requests(app)
    register_filters(app)
    register_processors(app)

class Application:
    def __init__(self):
        # Load the config file
        # Initialize the app, APPLICATION_MODE can be one of 'depolyment', 'development', 'testing'
        self.app = app_from_config(os.environ.get('APPLICATION_MODE'))
        register_commands(self.app)
    def init(self):
        self._merge_dict(init_management(self.app))
        self._merge_dict(init_i8n(self.app))
        self._merge_dict(init_views(self.app))
        self._merge_dict(init_permissions())
        self._merge_dict(init_database(app))
        self._merge_dict(init_flask(app))
    def _merge_dict(self, d):
        if d == None:
            return
        for k in d:
            self.__dict__[k] = d[k]
    def run(self, *args, **kwargs):
        self.init()
        self.app.run(*args, **kwargs)

application = Application()
app = application.app

