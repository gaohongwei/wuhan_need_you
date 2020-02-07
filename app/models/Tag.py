
from app.db import db
from app.libs.date_utils import utcnow

class Tag(db.Model):
    __tablename__ = 'tags'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False, unique=True)
    created_time = db.Column(db.DateTime, default=utcnow, onupdate=utcnow)

    def __str__(self):
        return self.name

