# coding: utf-8

from flask_admin.contrib.sqla import ModelView
import flask_login as login
from app.models import Comment, check_permission
from app.db import db
from app.libs.date_utils import format_cn

class CommentModelView(ModelView):
	can_create = False
	can_edit = False 
	can_delete = True 
	page_size = 10
	column_searchable_list = ['name', 'notice_title', 'comment', 'created_time']
	column_filters = ['name', 'notice_title', 'comment', 'created_time']

	column_labels = {
		'name': '姓名',
		'email': '邮箱',
		'notice_title': '新闻标题',
		'comment': '评论',
		'created_time': '创建时间'
	}

	def _time_formatter(view, context, model, name):
		return format_cn(getattr(model, name))
	column_formatters = {
		'created_time': _time_formatter
	}

	def __init__(self, *args, **kwargs):
		super().__init__(Comment, db.session, name='评论管理')

	def is_accessible(self):
		return check_permission(self, login.current_user)
