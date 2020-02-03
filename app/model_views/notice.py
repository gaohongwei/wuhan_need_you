from flask import Markup
from flask_ckeditor import CKEditorField
from flask_admin.contrib.sqla import ModelView
from wtforms import SelectField
import flask_login as login
from flask_login import current_user

from app.models.Notice import Notice, Status, Type, Priority


class NoticeModelView(ModelView):

    form_overrides = dict(
                        content=CKEditorField, 
                        status=SelectField, 
                        type=SelectField, 
                        priority=SelectField
                    )
    form_args = dict(
        status=dict(choices=[
            (Status.PENDING, 'Pending'), (Status.AGREE, 'Agree'), 
            (Status.DISAGREE, 'Disagree'), (Status.OFFLINE, 'Offline')], 
            coerce=int),
        type=dict(choices=[
            (Type.INFORMATION, 'Infomartion'), (Type.ADVERTISEMENT, 'Advertisement')], coerce=int),
        priority=dict(choices=[
            (Priority.LOW, 'Low'), (Priority.MEDIUM, 'Medium'), (Priority.HIGH, 'High')], coerce=int)
    )

    create_template = 'admin/create.html'
    edit_template = 'admin/edit.html'

    page_size = 10
    can_view_details = True

    column_exclude_list = ['content']
    column_searchable_list = ['title', 'status', 'type']
    column_sortable_list = ['modified_time', 'created_time', 'priority']

    form_create_rules = ['title', 'content', 'type', 'priority']
    form_excluded_columns = ['created_time', 'modified_time', 'creator', 'publisher']

    def _content_formatter(view, context, model, name):
        return Markup(model.content)
    
    def _status_formatter(view, context, model, name):
        return Notice.STATUS_DESC[(model.status)]
    
    def _type_formatter(view, context, model, name):
        return Notice.TYPE_DESC[model.type]
    
    def _priority_formatter(view, context, model, name):
        return Notice.PRIORITY_DESC[model.priority]

    column_formatters = {
        'content': _content_formatter,
        'status': _status_formatter,
        'type': _type_formatter,
        'priority': _priority_formatter
    }

    def is_accessible(self):
        return login.current_user.is_authenticated
