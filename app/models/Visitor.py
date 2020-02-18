# coding: utf-8

from flask import request, current_app
from sqlalchemy import func
from fnmatch import fnmatch

from app.db import db
from app.libs.date_utils import utcnow
from app.libs.net_utils import get_ip

class Visitor(db.Model):
    __tablename__ = 'visitors'
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(80), nullable=False)
    ip_addr = db.Column(db.String(16), nullable=False)
    visited_time = db.Column(db.DateTime, default=utcnow)

    # optimize
    queue = [] 
    capacity = 10

    exclude_patterns = ['*.jpg', '*.png', '*.jpeg', '*.css', '*.js', '*.ico', '*.map']

    def __str__(self):
        return self.url 

    @classmethod
    def is_excluded(cls, url):
        for pattern in cls.exclude_patterns:
            if fnmatch(url, pattern):
                return True
        return False

    @classmethod
    def add(cls):
        url = request.path
        if Visitor.is_excluded(url):
            current_app.logger.info(url + ' is ignored')
            return False
        ip_addr = get_ip()
        visited_time = utcnow()
        
        current_app.logger.info(url + ' is recorded')
        if len(cls.queue) < cls.capacity: 
            cls.queue.append((url, ip_addr, visited_time))
        else:
            for (url, ip_addr, visited_time) in cls.queue:
                db.session.add(Visitor(url=url, ip_addr=ip_addr, visited_time=visited_time))
                current_app.logger.info('batch recording')
            db.session.commit()
            cls.queue = []
        return True

    @classmethod
    def total(cls):
        return db.session.query(func.count(Visitor.id)).first()[0]

    @classmethod
    def count(cls, url):
        return db.session.query(Visitor.url).filter(Visitor.url == url).count()

    @classmethod
    def statistics(cls, pageNo, pageSize):
        '''
        pageNo: 1-based
        pageSize: size of each page
        return: {total, items}
        '''
        count = func.count(Visitor.url)
        return (db.session.query(Visitor.url, count)
                .group_by(Visitor.url)
                .order_by(count.desc())
                .paginate(pageNo, pageSize, True))

