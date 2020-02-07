# coding: utf-8

from flask import Markup
from flask_ckeditor import CKEditorField
from flask_admin import expose
from flask_admin.contrib.sqla import ModelView
import flask_login as login
from wtforms.fields import SelectField
from app.libs.date_utils import as_timezone
from app.models import check_permission, Notice

class NoticeModelView(ModelView):

    create_template = 'admin/create.html'
    edit_template = 'admin/edit.html'

    page_size = 10
    can_view_details = True

    column_exclude_list = ['content']
    column_searchable_list = ['title', 'status', 'type']
    column_sortable_list = ['title', 'modified_time', 'created_time', 'permitted_time', 'type', 'status']
    column_editable_list = ['title', 'content', 'type', 'tags']

    form_create_rules = ['title', 'content', 'type', 'priority', 'tags']
    form_excluded_columns = ['created_time', 'modified_time', 'permitted_time', 'create_user', 'permit_user']

    form_overrides = dict(
            content = CKEditorField,
            priority = SelectField,
            status = SelectField
            )
    form_choices = {
            'type': [ ('信息', '信息'), ('广告', '广告') ]
            }
    form_args = dict(
            priority = dict(choices=[(0, '普通'), (1, '优先'), (2, '紧急')], coerce=int, label='优先级'),
            status = dict(choices=[(0, '草稿'), (1, '已提交'), (2, '已审核'), (3, '未批准')], coerce=int, label='状态')
            )

    # UTC time to local time
    def _time_formatter(view, content, model, name):
        time = getattr(model, name)
        return as_timezone(time)

    def _content_formatter(view, context, model, name):
        return Markup(model.content)
    
    def _status_formatter(view, context, model, name):
        return model.get_status_name()
    
    def _priority_formatter(view, context, model, name):
        return model.get_priority_name()
    
    def _create_user_formatter(view, context, model, name):
        return model.create_user.username
    
    def _permit_user_formatter(view, context, model, name):
        if model.permit_user:
            return model.permit_user.username
        return None

    column_formatters = {
        'content': _content_formatter,
        'status': _status_formatter,
        'create_user': _create_user_formatter,
        'permit_user': _permit_user_formatter,
        'modified_time': _time_formatter,
        'created_time': _time_formatter,
        'priority': _priority_formatter
    }

    def is_accessible(self):
        # return True # For debug
        return check_permission(self, login.current_user)

    @expose('/preview')
    def index(self):
        notices = Notice.query.all()
        return self.render('pages/notices.html', notices = notices)
