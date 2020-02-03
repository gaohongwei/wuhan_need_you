from app.db import db
from sqlalchemy import func, event
import flask_login as login


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
    __table_name__ = 'notices'

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
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(512), nullable=False)
    content = db.Column(db.Text, nullable=False)
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
    target.creator = login.current_user.login

@event.listens_for(Notice, 'before_update')
def before_update_notice(mapper, connection, target):
    if target.status == Status.AGREE:
        target.publisher = login.current_user.login

