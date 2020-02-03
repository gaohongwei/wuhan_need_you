from flask_admin import Admin
from flask_ckeditor import CKEditor
from flask_sqlalchemy import SQLAlchemy
from app.models import User, Notice
from app.model_views import UserModelView, NoticeModelView, AdminIndexView, init_login, init_sample_users
from app.db import init_app
from app.config import create_app
import os

# Initialize the app, APPLICATION_MODE can be one of 'depolyment', 'development', 'testing'
app = create_app(os.environ.get('APPLICATION_MODE'))

admin = Admin(app=app, index_view=AdminIndexView())
ckeditor = CKEditor(app)

# Load the views
from app import views

# Load the config file
db = init_app(app)
login_manager = init_login(app)
admin.add_view(UserModelView(User, db.session))
admin.add_view(NoticeModelView(Notice, db.session))

init_sample_users(app)

logger = app.logger

