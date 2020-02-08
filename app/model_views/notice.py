# coding: utf-8

from gettext import ngettext
from flask import Markup, flash
from flask_ckeditor import CKEditorField
from flask_admin import expose
from flask_admin.actions import action
from flask_admin.contrib.sqla import ModelView
import flask_login as login
from wtforms.fields import SelectField
from app.libs.date_utils import as_timezone, utcnow, format_cn
from app.models import check_permission, Notice, Tag
from app.models.Notice import get_current_user_id
from app.db import db

class NoticeModelView(ModelView):

    create_template = 'admin/create_notice.html'
    edit_template = 'admin/edit_notice.html'
    list_template = 'admin/list_notice.html'

    column_list = [
            'title',
            'content',
            'created_time',
            'modified_time',
            'create_user',
            'permit_user',
            'type',
            'status',
            'tags'
            ]
    column_labels = {
            'title': '标题',
            'content': '正文',
            'created_time': '创建时间',
            'modified_time': '最后编辑时间',
            'permitted_time': '审批时间',
            'permit_user': '审批人',
            'type': '类型',
            'create_user': '创建者',
            'status': '审批状态',
            'tags.name': '标签',
            'tags': '标签',
            'priority': '优先级'
            }
    column_filters = [
            'title',
            'created_time',
            'modified_time',
            'permitted_time',
            'type',
            'create_user',
            'status',
            'tags',
            'priority'
            ]

    form_ajax_refs = {
            'tags': {
                'fields': (Tag.name, ),
                'minimum_input_length': 0, # show suggestions, even before any user input
                'placeholder': '请选择',
                'page_size': 5
                }
            }

    page_size = 10
    can_view_details = True

    column_exclude_list = ['content']
    column_searchable_list = ['title', 'status', 'type']
    column_sortable_list = ['title', 'modified_time', 'created_time', 'permitted_time', 'type', 'status', 'tags.name']
    column_editable_list = ['title', 'content', 'type']

    form_create_rules = ['title', 'content', 'type', 'priority', 'tags']
    form_edit_rules = ['title', 'content', 'type', 'priority', 'tags']

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

    def __init__(self, *args, **kwargs):
        super().__init__(Notice, db.session, name='通知管理')

    def _content_formatter(view, context, model, name):
        return Markup(model.content)

    def _time_formatter(view, context, model, name):
        value = getattr(model, name)
        return format_cn(value)
    
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
        'priority': _priority_formatter,
        'modified_time': _time_formatter,
        'permitted_time': _time_formatter
    }

    def is_accessible(self):
        return check_permission(self, login.current_user)

    @expose('/preview')
    def preview(self):
        notices = Notice.query.all()
        return self.render('pages/notices.html', notices = notices)

    
    @action('approve', 'Approve', 'Are you sure you want to approve selected notices?')
    def action_approve(self, ids):
        try:
            rows = Notice.query.filter(Notice.id.in_(ids)).\
                                filter(Notice.status != 2).\
                                update(
                                    {
                                        'status': 2,
                                        'permit_user_id': get_current_user_id(),
                                        'permitted_time': utcnow()
                                    }, 
                                synchronize_session=False)
            db.session.commit()

            message = '{} notices have been successfully approved'.format(rows)
            flash(message, 'success')

        except Exception as ex:
            if not self.handle_view_exception(ex):
                raise
            
            flash(gettext('Failed to approve notices. %(error)s', error=str(ex)), 'error')
    
    @action('disapprove', 'Disapprove', 'Are you sure you want to disapprove selected notices?')
    def action_disapprove(self, ids):
        try:
            rows = Notice.query.filter(Notice.id.in_(ids)).\
                                filter(Notice.status != 3).\
                                update(
                                    {
                                        'status': 3,
                                        'permit_user_id': get_current_user_id(),
                                        'permitted_time': utcnow()
                                    }, 
                                synchronize_session=False)
            db.session.commit()

            message = '{} notices have been successfully disapproved'.format(rows)
            flash(message, 'success')

        except Exception as ex:
            if not self.handle_view_exception(ex):
                raise
            
            flash(gettext('Failed to disapprove notices. %(error)s', error=str(ex)), 'error')
