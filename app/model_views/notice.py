from flask import Markup
from flask_ckeditor import CKEditorField
from flask_admin.contrib.sqla import ModelView


class NoticeModelView(ModelView):

    form_overrides = dict(content=CKEditorField)

    create_template = 'admin/create.html'
    edit_template = 'admin/edit.html'

    page_size = 10
    can_view_details = True

    column_exclude_list = ['content']
    column_searchable_list = ['title', 'status', 'type']
    column_sortable_list = ['modified_time', 'created_time']
    
    form_excluded_columns = ['created_time', 'modified_time']

    def _content_formatter(view, context, model, name):
        return Markup(model.content)

    column_formatters = {
        'content': _content_formatter
    }


