# coding: utf-8
from flask import current_app
from app.db import db
from sqlalchemy import func, event
from sqlalchemy.orm import relationship
from app.libs.date_utils import utcnow
import flask_login as login

from app.models.User import User

def get_current_user_id():
    if login.current_user == None:
        return None
    return login.current_user.get_id()
class Status:
    PENDING = 0
    AGREE = 1
    DISAGREE = 2
    OFFLINE = 3


class Type:
    INFORMATION = 0
    ADVERTISEMENT = 1


class Priority:
    LOW = 0
    MEDIUM = 1
    HIGH = 2

class Notice(db.Model):
    STATUS_DESC = {
        Status.PENDING: 'Pending',
        Status.AGREE: 'Agree',
        Status.DISAGREE: 'Disagree',
        Status.OFFLINE: 'Offline'
    }

    TYPE_DESC = {
        Type.INFORMATION: 'Information',
        Type.ADVERTISEMENT: 'Advertisement'
    }

    PRIORITY_DESC = {
        Priority.LOW: 'Low',
        Priority.MEDIUM: 'Medium',
        Priority.HIGH: 'High'
    }

    __tablename__ = 'notices'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(512), nullable=False)
    content = db.Column(db.Text, nullable=False)
    # The time is stored without timezone info in database,
    # They are considered UTC
    # Remember to recover to local time when use them
    created_time = db.Column(db.DateTime, default=utcnow)
    modified_time = db.Column(db.DateTime, default=utcnow, onupdate=utcnow)
    permitted_time = db.Column(db.DateTime) # permit or not permit
    type = db.Column(db.String, nullable=False)
    create_user_id = db.Column(db.Integer, db.ForeignKey('users.id'), default=get_current_user_id)
    permit_user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    create_user = relationship('User', foreign_keys=[create_user_id])
    permit_user = relationship('User', foreign_keys=[permit_user_id])


    priority = db.Column(db.Integer, default=0)
    # comma separated list
    tags = db.Column(db.Text)
    status = db.Column(db.Integer, default=0)

    def get_status(self):
        return self.status

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


@event.listens_for(Notice, 'before_update')
def before_update_notice(mapper, connection, target):
    if target.status == 2:
        target.permit_user_id = get_current_user_id()
        target.permitted_time = utcnow()
    status = db.Column(db.Integer, nullable=False)
    type = db.Column(db.Integer, nullable=False)
    priority = db.Column(db.Integer, default=0)
    creator = db.Column(db.String(256))
    publisher = db.Column(db.String(256))
    created_time = db.Column(db.DateTime, default=func.now())
    modified_time = db.Column(db.DateTime, default=func.now(), onupdate=func.now())


@event.listens_for(Notice, 'before_insert')
def before_insert_notice(mapper, connection, target):
    target.status = Status.PENDING
    target.creator = login.current_user.username

@event.listens_for(Notice, 'before_update')
def before_update_notice(mapper, connection, target):
    if target.status == Status.AGREE:
        target.publisher = login.current_user.username

