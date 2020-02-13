# coding: utf-8

from flask_admin.contrib.sqla import ModelView
import flask_login as login
from app.models import Visitor, check_permission
from app.db import db
from app.libs.date_utils import format_cn

class VisitorModelView(ModelView):

    can_create = False
    can_edit = False
    can_delete = False
    page_size = 10
    column_searchable_list = ['url', 'ip_addr', 'visited_time']
    column_filters = ['url', 'ip_addr', 'visited_time']

    column_labels = {
            'url': 'URL',
            'ip_addr': 'IP地址',
            'visited_time': '访问时间'
            }

    def _time_formatter(view, context, model, name):
        return format_cn(getattr(model, name))
    column_formatters = {
        'visited_time': _time_formatter
        }

    def __init__(self, *args, **kwargs):
        super().__init__(Visitor, db.session, name='监控管理')

    def is_accessible(self):
        return check_permission(self, login.current_user)

