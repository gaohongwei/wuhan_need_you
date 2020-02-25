from app.db import db
from app.libs.date_utils import utcnow
from jinja2 import Markup
from flask import url_for, render_template_string


class Page(db.Model):
    __tablename__ = "pages"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False, unique=True)
    description = db.Column(db.String(255))
    layout = db.Column(db.Text)
    fragments = db.relationship("Fragment", secondary="page_fragment")
    assets = db.relationship("Asset", secondary="page_asset")

    def __str__(self):
        return self.name

    def parsed(self):
        layout = self.layout
        fragments = self.fragments
        assets = self.assets
        data_dic = {}
        for fragment in fragments:
            data_dic[fragment.name] = fragment.content
        for asset in assets:
            asset_markup = Markup(
                '<img src="%s">' % url_for("static", filename=asset.path)
            )
            data_dic[asset.name] = asset_markup

        # to avoid affect {{...}} and {%...%}
        for key in data_dic:
            layout = layout.replace('{' + key + '}', data_dic[key])
        return layout

    def render(self, **kwargs):
        template = '''
{% extends "base.html" %}
{% block title %}Preview{% endblock %}
{% block body %}
''' + self.parsed() + '{% endblock %}'
        print(template)
        return render_template_string(template, **kwargs)

# Text paragraphs
class Fragment(db.Model):
    __tablename__ = "fragments"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False, unique=True)
    content = db.Column(db.Text, nullable=False)
    pages = db.relationship("Page", secondary="page_fragment")

    def __str__(self):
        return self.name


# img, video etc
# Should be uploaded from admin ui
class Asset(db.Model):
    __tablename__ = "assets"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False, unique=True)
    path = db.Column(db.String(128))
    file_type = db.Column(db.String(10), nullable=False)
    pages = db.relationship("Page", secondary="page_asset")

    def __str__(self):
        return self.name


class PageFragment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    page_id = db.Column(db.Integer, db.ForeignKey("pages.id"), nullable=False)
    fragment_id = db.Column(db.Integer, db.ForeignKey("fragments.id"), nullable=False)


class PageAsset(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    page_id = db.Column(db.Integer, db.ForeignKey("pages.id"), nullable=False)
    asset_id = db.Column(db.Integer, db.ForeignKey("assets.id"), nullable=False)
