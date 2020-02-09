# coding: utf-8

from app.db import db
from app.libs.date_utils import utcnow, time_diff_in_seconds
from sqlalchemy import func

class Cache(db.Model):
    '''
    A database based cache
    '''
    __tablename__ = 'caches'
    key = db.Column(db.String(80), primary_key=True, nullable=False)
    value = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, default=utcnow, onupdate=utcnow)

    @classmethod
    def set(cls, key, value):
        '''
        insert or update a cache item
        '''
        cache = cls.get(key)
        if cache == None:
            db.session.add(Cache(key=key, value=value))
        else:
            cache.value = value
        db.session.commit()

    @classmethod
    def get_latest(cls):
        return Cache.query.order_by(Cache.timestamp.desc()).limit(1).first()

    @classmethod
    def delete(cls, key):
        '''
        delete a cache item if exists
        '''
        cache = cls.get(key)
        if cache == None:
            return
        db.session.remove(cache)
        db.session.commit()

    @classmethod
    def clear(cls):
        '''
        delete all
        '''
        db.session.query(Cache).delete()
        db.session.commit()

    @classmethod
    def get(cls, key):
        '''
        get a cache item
        '''
        cache = db.session.query(Cache).filter_by(key=key).first()
        if cache == None:
            return None
        return cache

    @classmethod
    def get_value(cls, key):
        '''
        get the value of a cache item
        '''
        cache = cls.get(key)
        if cache == None:
            return None
        return cache.value

    @classmethod
    def get_timestamp(cls, key):
        '''
        get the timestamp of a cache item
        '''
        cache = cls.get(key)
        if cache == None:
            return None
        return cache.timestamp

    @classmethod
    def update_outdated(cls, key, value, timeout_in_seconds):
        '''
        insert a cache item if not exist, or
        update a cache item if outdated
        '''
        cache = cls.get(key)
        if cache == None:
            db.session.add(cache)
        elif time_diff_in_seconds(utcnow(), cache.timestamp) <= timeout_in_seconds:
            cache.value = value
        db.session.commit()

    @classmethod
    def update_timestamp(cls, key):
        '''
        update an existed cache item's timestamp
        '''
        cache = cls.get(key)
        if cache != None:
            cache.timestamp = utcnow()
            db.session.commit()

