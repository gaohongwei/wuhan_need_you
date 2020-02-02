from flask import Flask
from flask_admin import Admin
from flask_ckeditor import CKEditor
from flask_sqlalchemy import SQLAlchemy

from app.model_views.notice import NoticeModelView

# Initialize the app
app = Flask(__name__, instance_relative_config=True)
admin = Admin(app=app)
ckeditor = CKEditor(app)

# Load the views
from app import views

# Load the config file
app.config.from_object('config')

db = SQLAlchemy(app)
from app.models import User, Notice
db.create_all()
admin.add_view(NoticeModelView(Notice, db.session))
