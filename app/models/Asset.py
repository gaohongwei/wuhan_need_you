# coding: utf-8

from flask import current_app
import json
from app.db import db
from sqlalchemy.ext.hybrid import hybrid_property

from app.libs.date_utils import as_timezone, utcnow

class Asset(db.Model):
    __tablename__ = 'assets'
    id = db.Column(db.Integer, primary_key=True)
    key = db.Column(db.String(128), unique=True, nullable=False)
    name = db.Column(db.String(128), nullable=False)
    # html, image, image_list
    type = db.Column(db.String(32), nullable=False)
    value = db.Column(db.Text, nullable=False)
    description = db.Column(db.Text, nullable=False)
    created_time = db.Column(db.DateTime, default=utcnow)
    modified_time = db.Column(db.DateTime, default=utcnow, onupdate=utcnow)

    @hybrid_property
    def content(self):
        return self.get_content()

    @content.expression
    def content(cls):
        return cls.value

    @content.setter
    def content(self, c):
        self.set_content(c)
    
    def get_content(self):
        if self.type == 'html':
            return self.get_as_html()
        elif self.type == 'image':
            return self.get_as_image()
        elif self.type == 'image_list':
            return self.get_as_image_list()
        else:
            current_app.logger.warn('unkown asset type ' + self.type)
            return self.value

    def get_as_html(self):
        return self.value or ''

    @staticmethod
    def _to_image(obj):
        obj = obj or {}
        return {'url': data.get('url', ''), 'title': data.get('title', '')}

    def get_as_image(self):
        data = self.get_as_json() or {}
        return Asset._to_image(data)

    def get_as_image_list(self):
        data = self.get_as_json() or []
        return [Asset._to_image(d) for d in data]

    def get_as_json(self):
        data = self.value or 'null'
        try:
            return json.loads(data)
        except Exception as e:
            current_app.logger.error('get_as_json error:' + e)
            return None

    @classmethod
    def get_content_by_key(cls, key):
        asset = Asset.query.filter_by(key=key).first()
        if asset == None:
            return None
        return asset.content

    @classmethod
    def get_asset_choices(cls):
        return [
                ('html', '网页'),
                ('image', '图片'),
                ('image_list', '图片列表')
                ]

