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
        # admin account for test and development only, but deploy would be changed!
        db.session.add(User(username="admin", role=1, password="admin"))
        for name in ['广告', '信息', '置顶', '紧急', '通知与公告', '校运会在行动']:
            db.session.add(Tag(name=name))
            try:
                db.session.commit()
            except IntegrityError as e:
                db.session.rollback()
