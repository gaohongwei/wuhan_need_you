import os
import os.path as op
from flask import url_for
from flask_admin.contrib.sqla import ModelView
import flask_login as login
from flask_ckeditor import CKEditorField
from flask_admin.actions import action
from flask_admin import form
from jinja2 import Markup
from app.models.Pages import Page, Fragment, Asset
from app.db import db

# Create directory for file fields to use
UPLOAD_DIR = op.join(op.dirname(__file__), "../static")
try:
    os.mkdir(UPLOAD_DIR)
except OSError:
    pass


class MyView(ModelView):
    can_view_details = True
    create_template = "admin/create_notice.html"
    edit_template = "admin/edit_notice.html"
    list_template = "admin/list_notice.html"


class PageModelView(MyView):
    column_labels = {
            'name': '名称',
            'description': '描述',
            'fragments': '段落',
            'assets': '资源',
            'layout': '布局',
            'rendered': '渲染结果'
            }
    column_list = ["name", "description", "fragments", "assets", "layout"]
    column_editable_list = ["name", "description"]
    form_columns = column_list + ["layout"]
    form_widget_args = {"layout": {"rows": 10, "columns": 60, "style": "color: black"}}

    # form_overrides = {layout: '<div class="row"> {framnet1} </div>'}

    def _format_layout(view, context, model, name):
        html = '<a href="/pages/{}">预览</a>'.format(model.name)
        return Markup(html)

    column_formatters = {"layout": _format_layout}

    def __init__(self, *args, **kwargs):
        super().__init__(Page, db.session, category="CMS", name="Page")

    def is_accessible(self):
        return True

    @action("layout_3columns", "Layout_3_columns")
    def layout_3columns(self):
        return "Layout_3_columns"


class FragmentModelView(MyView):
    column_labels = {
            'name': '名称',
            'pages': '页面',
            'content': '内容'
            }
    form_overrides = dict(content=CKEditorField)
    column_list = ["name", "pages", "content"]

    def __init__(self, *args, **kwargs):
        super().__init__(Fragment, db.session, category="CMS", name="Fragment")

    def is_accessible(self):
        return True


class AssetModelView(MyView):
    column_labels = {
            'name': '名称',
            'path': '缩略图',
            'file_type': '文件类型'
            }
    def __init__(self, *args, **kwargs):
        super().__init__(Asset, db.session, category="CMS", name="Asset")

    def is_accessible(self):
        return True

    def _list_thumbnail(view, context, model, name):
        if not model.path:
            return ""

        return Markup(
            '<img src="%s">'
            % url_for("static", filename=form.thumbgen_filename(model.path))
        )

    column_formatters = {"path": _list_thumbnail}
    # Alternative way to contribute field is to override it completely.
    # In this case, Flask-Admin won't attempt to merge various parameters for the field.
    form_extra_fields = {
        "path": form.ImageUploadField(
            "Image2", base_path=UPLOAD_DIR, thumbnail_size=(100, 100, True)
        )
    }
