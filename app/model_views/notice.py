# coding: utf-8

from flask import Markup
from flask_ckeditor import CKEditorField
from flask_admin.contrib.sqla import ModelView
import flask_login as login
from app.libs.date_utils import as_timezone
from app.models import check_permission


class NoticeModelView(ModelView):

    form_overrides = dict(content=CKEditorField)

    create_template = 'admin/create.html'
    edit_template = 'admin/edit.html'

    page_size = 10
    can_view_details = True

    column_exclude_list = ['content']
    column_searchable_list = ['title', 'status', 'type']
    column_sortable_list = ['title', 'modified_time', 'created_time', 'permitted_time', 'type', 'status']
    column_editable_list = ['title', 'content', 'type', 'priority', 'tags']
    
    form_excluded_columns = ['created_time', 'modified_time', 'permitted_time']
    form_choices = {
            'type': [
                ('信息', '信息'),
                ('广告', '广告')
                ]#,
            #'priority': [     # TODO: need post-processing
            #    ('0', '普通'),
            #    ('1', '优先'),
            #    ('2', '紧急')
            #    ]
            }

    # UTC time to local time
    def _time_formatter(view, content, model, name):
        time = getattr(model, name)
        return as_timezone(time)

    def _content_formatter(view, context, model, name):
        return Markup(model.content)

    column_formatters = {
        'content': _content_formatter,
        'modified_time': _time_formatter,
        'created_time': _time_formatter
    }

    def is_accessible(self):
        return check_permission(self, login.current_user)

