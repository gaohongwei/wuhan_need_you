# coding: utf-8

from sqlalchemy import func
from flask_admin.contrib import sqla
from flask_admin.contrib.sqla.filters import BaseSQLAFilter
from wtforms import PasswordField, TextField, SelectField, validators
from flask_ckeditor import CKEditorField
import flask_login as login
from app.models import Asset, check_permission
from app.db import db
from app.libs.date_utils import format_cn

class AssetModelView(sqla.ModelView):

    create_template = 'admin/assets/create_asset.html'

    column_labels = {
            'key': 'Key',
            'name': '名称',
            'type': '类型',
            'value': '内容',
            'description': '描述',
            'created_time': '创建时间',
            'modified_time': '修改时间'
            }

    form_excluded_columns = ['created_time', 'modified_time']

    def __init__(self, *args, **kwargs):
        super().__init__(Asset, db.session, name='资源管理')

    def is_accessible(self):
        return check_permission(self, login.current_user)

    def create_form(self):
        form = super().create_form()
        print(form)
        print(dir(form))
        print(form.data)
        print(form._fields)
        return form

    form_extra_fields = {
            'type': SelectField('类型', [validators.required()],
                choices=Asset.get_asset_choices()
                )
            }

