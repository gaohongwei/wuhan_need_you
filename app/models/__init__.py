# coding: utf-8

from app.db import db
from sqlalchemy.exc import IntegrityError
from .User import User
from .Notice import Notice
from .Tag import Tag
from .Cache import Cache
from .NoticeTag import NoticeTag
from .Visitor import Visitor
from .Comment import Comment
from .UserPermission import register_route_permission
from .UserPermission import register_model_view_permission
from .UserPermission import check_route_permission
from .UserPermission import check_model_view_permission

from .UserPermission import check_permission

def recreate_database(app):
    with app.app_context():
        # db.drop_all()
        db.create_all()
        db.session.add(User(username="admin", role=1, password="admin"))
        db.session.add(User(username="test", role=1, password="test"))
        db.session.add(User(username="test2", role=2, password="test2"))
        db.session.add(User(username="test3", role=3, password="test3"))
        for name in ['广告', '信息', '置顶', '紧急', '通知与公告', '校运会在行动']:
            db.session.add(Tag(name=name))
            try:
                db.session.commit()
            except IntegrityError as e:
                db.session.rollback()
