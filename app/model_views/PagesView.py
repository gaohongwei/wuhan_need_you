from flask_admin.contrib.sqla import ModelView
import flask_login as login
from app.models.Pages import Page, Fragment, Asset
from app.db import db
from flask_ckeditor import CKEditorField
from flask_admin.actions import action


class MyView(ModelView):
    can_view_details = True
    create_template = "admin/create_notice.html"
    edit_template = "admin/edit_notice.html"
    list_template = "admin/list_notice.html"


class PageModelView(MyView):
    column_list = ["name", "description", "fragments"]
    form_columns = column_list + ["layout"]
    form_widget_args = {"layout": {"rows": 10, "columns": 60, "style": "color: black"}}

    # form_overrides = {layout: '<div class="row"> {framnet1} </div>'}

    def _format_layout(view, context, model, name):
        return '<div class="row"> {framnet1} </div>'

    column_formatters = {"layout": "_format_layout"}

    def __init__(self, *args, **kwargs):
        super().__init__(Page, db.session, category="CMS", name="Page")

    def is_accessible(self):
        return True

    @action("layout_3columns", "Layout_3_columns")
    def layout_3columns(self):
        return "Layout_3_columns"


class FragmentModelView(MyView):
    form_overrides = dict(content=CKEditorField)
    column_list = ["name", "pages", "content"]

    def __init__(self, *args, **kwargs):
        super().__init__(Fragment, db.session, category="CMS", name="Fragment")

    def is_accessible(self):
        return True


class AssetModelView(MyView):
    def __init__(self, *args, **kwargs):
        super().__init__(Asset, db.session, category="CMS", name="Asset")

    def is_accessible(self):
        return True

