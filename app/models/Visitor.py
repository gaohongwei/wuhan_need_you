# coding: utf-8

from app.db import db
from app.libs.date_utils import utcnow

class Visitor(db.Model):
	__tablename__ = 'visitors'
	id = db.Column(db.Integer, primary_key=True)
	url = db.Column(db.String(80), nullable=False)
	proxy_ip_addr = db.Column(db.String(16), nullable=False)
	real_ip_addr = db.Column(db.String(16), nullable=False)
	visited_time = db.Column(db.DateTime, default=utcnow, onupdate=utcnow)

	def __str__(self):
		return self.url 