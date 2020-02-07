
from app.db import db

class NoticeTag(db.Model):
    __tablename__ = 'notice_tag'
    notice_id = db.Column(db.Integer, db.ForeignKey('notices.id'), primary_key=True)
    tag_id = db.Column(db.Integer, db.ForeignKey('tags.id'), primary_key=True)

