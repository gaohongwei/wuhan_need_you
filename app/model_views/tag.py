from flask_admin.contrib.sqla import ModelView
import flask_login as login
from app.models import Tag, check_permission
from app.db import db

class TagModelView(ModelView):
    def __init__(self, *args, **kwargs):
        super().__init__(Tag, db.session, name='标签管理')
    def is_accessible(self):
        return check_permission(self, login.current_user)
