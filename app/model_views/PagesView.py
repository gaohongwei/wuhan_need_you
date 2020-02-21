from flask_admin.contrib.sqla import ModelView
import flask_login as login
from app.models.Pages import Page, Fragment, Asset
from app.db import db


class PageModelView(ModelView):
    def __init__(self, *args, **kwargs):
        super().__init__(Page, db.session, category="CMS", name="Page")

    def is_accessible(self):
        return True


class FragmentModelView(ModelView):
    def __init__(self, *args, **kwargs):
        super().__init__(Fragment, db.session, category="CMS", name="Fragment")

    def is_accessible(self):
        return True


class AssetModelView(ModelView):
    def __init__(self, *args, **kwargs):
        super().__init__(Asset, db.session, category="CMS", name="Asset")

    def is_accessible(self):
        return True

