from flask import current_app
from app.db import db
from sqlalchemy import func
from app.libs.date_utils import utcnow

class Notice(db.Model):
    __tablename__ = 'notices'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    content = db.Column(db.Text, nullable=False)
    # The time is stored without timezone info in database,
    # They are considered UTC
    # Remember to recover to local time when use them
    created_time = db.Column(db.DateTime, default=utcnow)
    modified_time = db.Column(db.DateTime, default=utcnow, onupdate=utcnow)
    permitted_time = db.Column(db.DateTime) # permit or not permit
    type = db.Column(db.String, nullable=False)
    create_user = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    permit_user = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

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

