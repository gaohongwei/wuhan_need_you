# coding: utf-8

import os
from flask_admin.contrib.fileadmin import FileAdmin
import flask_login as login
from flask import current_app
from app.models import User, check_permission

class MyFileAdmin(FileAdmin):
    def __init__(self, app):
        staticPath = app.config['IMAGE_FILE_UPLOAD_DIRECTORY']
        if not os.path.exists(staticPath):
            os.mkdir(staticPath)
        super().__init__(staticPath, '/files/', name='文件管理')
    # required by flask-admin
    def is_accessible(self):
        return check_permission(self, login.current_user)

