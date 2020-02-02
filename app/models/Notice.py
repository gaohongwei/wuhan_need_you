
from app.db import db
from sqlalchemy import func

class Notice(db.Model):
    __table_name__ = 'notices'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    content = db.Column(db.Text, nullable=False)
    created_time = db.Column(db.DateTime, default=func.now())
    modified_time = db.Column(db.DateTime, default=func.now(), onupdate=func.now())
    status = db.Column(db.String, nullable=False)
    type = db.Column(db.String, nullable=False)
    creator = db.Column(db.Integer, nullable=False)
    publisher = db.Column(db.Integer, nullable=False)

