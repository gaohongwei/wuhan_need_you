# coding: utf-8

import os
from flask_admin.contrib.fileadmin import FileAdmin
from app.models import User, check_permission
import flask_login as login

staticPath = os.path.join(os.path.dirname(__file__), '..', 'static/upload')

class MyFileAdmin(FileAdmin):
    def __init__(self):
        if not os.path.exists(staticPath):
            os.mkdir(staticPath)
        super().__init__(staticPath, '/upload/', name='文件管理')
    # required by flask-admin
    def is_accessible(self):
        return check_permission(self, login.current_user)

