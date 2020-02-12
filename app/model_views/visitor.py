# coding: utf-8

from flask_admin.contrib.sqla import ModelView
import flask_login as login
from app.models import Visitor, check_permission
from app.db import db

class VisitorModelView(ModelView):

	can_create = False
	can_edit = False
	can_delete = False
	page_size = 10
	column_searchable_list = ['url', 'ip_addr', 'visited_time']
	column_filters = ['url', 'ip_addr', 'visited_time']

	def __init__(self, *args, **kwargs):
		super().__init__(Visitor, db.session, name='监控管理')
		
	def is_accessible(self):
		return check_permission(self, login.current_user)