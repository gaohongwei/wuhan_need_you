# coding: utf-8

from flask import request, current_app
from sqlalchemy import func
from app.libs.date_utils import utcnow

from app.db import db

class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120))
    notice_title = db.Column(db.String(150), nullable=False)
    notice_id = db.Column(db.Integer, db.ForeignKey('notices.id'), nullable=False)
    comment = db.Column(db.String(1024), nullable=False)
    created_time = db.Column(db.DateTime, default=utcnow)

    @classmethod
    def add(cls):
        notice_title = request.form.get('notice_title')
        notice_id = request.form.get('notice_id')
        name = request.form.get('name') 
        email = request.form.get('email')
        comment = request.form.get('comment') 

        c = Comment(name=name,
                email=email,
                comment=comment,
                notice_title=notice_title,
                notice_id=notice_id)
        db.session.add(c)
        try:
            db.session.commit()
        except:
            db.session.rollback()
        current_app.logger.info(comment + ' is recorded')
        return True

    @classmethod
    def get_comments_by_noticeid(cls, notice_id):
        return (db.session.query(Comment)
                .filter_by(notice_id=notice_id)
                .order_by(Comment.created_time.desc())
                .all())

