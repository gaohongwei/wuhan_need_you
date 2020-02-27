# coding: utf-8

from flask import current_app
from app.db import db
from sqlalchemy import func, event
from sqlalchemy.orm import relationship
from sqlalchemy.ext.hybrid import hybrid_property
from app.libs.date_utils import utcnow
import flask_login as login

from app.models.User import User
from app.libs.date_utils import as_timezone

def get_current_user_id():
    if login.current_user == None:
        return None
    return login.current_user.get_id()

class Notice(db.Model):
    __tablename__ = 'notices'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    content = db.Column(db.Text, nullable=False)
    # The time is stored without timezone info in database,
    # They are considered UTC
    # Remember to recover to local time when use them
    _created_time = db.Column(db.DateTime, default=utcnow)
    _modified_time = db.Column(db.DateTime, default=utcnow, onupdate=utcnow)
    _permitted_time = db.Column(db.DateTime) # permit or not permit
    type = db.Column(db.String, nullable=False)
    create_user_id = db.Column(db.Integer, db.ForeignKey('users.id'), default=get_current_user_id)
    permit_user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    create_user = relationship('User', foreign_keys=[create_user_id])
    permit_user = relationship('User', foreign_keys=[permit_user_id])


    priority = db.Column(db.Integer, default=0)
    status = db.Column(db.Integer, default=0)

    tags = db.relationship('Tag', secondary='notice_tag')

    @hybrid_property
    def created_time(self):
        return as_timezone(self._created_time)

    @created_time.expression
    def created_time(cls):
        return cls._created_time

    # add timezone info for utc time
    @hybrid_property
    def modified_time(self):
        return as_timezone(self._modified_time)

    # for sqlalchemy expression
    @modified_time.expression
    def modified_time(cls):
        return cls._modified_time

    @hybrid_property
    def permitted_time(self):
        return as_timezone(self._permitted_time)

    @permitted_time.expression
    def permitted_time(cls):
        return cls._permitted_time

    @permitted_time.setter
    def permitted_time(self, utctime):
        self._permitted_time = utctime

    @hybrid_property
    def tag_names(self):
        return [tag.name for tag in self.tags]

    def get_status(self):
        return self.status

    @classmethod
    def list_latest_alumni_action_notices(cls, num):
        return (cls.query.join(Notice.tags)
                            .filter_by(name="校运会在行动")
                            .limit(num))

    def get_status_name(self):
        maps = ['草稿', '已提交', '已审核', '未批准']
        if self.status < 0:
            current_app.logger.warn('negative status: ', self.status)
            return maps[0]
        if self.status >= len(maps):
            current_app.logger.warn('too large status: ', self.status)
            return maps[-1]
        return maps[self.status]
    
    def get_priority_name(self):
        priority_desc = {
            0: '普通',
            1: '优先',
            2: '紧急'
        }
        return priority_desc.get(self.priority, None) or self.priority
