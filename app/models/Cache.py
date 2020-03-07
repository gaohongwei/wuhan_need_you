# coding: utf-8

import json
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
            cache = cls(key=key, value=value)
            db.session.add(cache)
        else:
            cache.value = value
        db.session.commit()
        return cache

    @classmethod
    def get_latest(cls, key_prefix=None, timeout_in_seconds=None):
        if key_prefix == None:
            cache = cls.query.order_by(cls.timestamp.desc()).limit(1).first()
        else :
            cache = cls.query.filter(cls.key.like( '{}%'.format(key_prefix))).order_by(cls.timestamp.desc()).limit(1).first()
        if cache == None:
            return None
        if timeout_in_seconds != None and cache.is_outdated(timeout_in_seconds):
            return None
        return cache


    @classmethod
    def get_latest_or_update(cls, key_prefix, timeout_in_seconds, producer):
        '''
        key_prefix: used to identify the type of a cache
        producer: generate an object {key, value}, both key and value are strings, the value may be object
        '''
        key_prefix = key_prefix or ''
        cache = cls.get_latest(key_prefix, timeout_in_seconds)
        if cache != None:
            return cache
        result = producer()
        if result != None:
            key = key_prefix + result['key']
            value = result['value']
            if not isinstance(value, str):
                value = json.dumps(value)
            cache = cls.set(key, value)
            return cache
        return None

    @classmethod
    def try_get_latest_or_update(cls, key_prefix, timeout_in_seconds, producer):
        '''
        call get_latest_or_update first()
        if return None: return get_latest()
        '''
        cache = cls.get_latest_or_update(key_prefix, timeout_in_seconds, producer)
        if cache == None:
            return cls.get_latest(key_prefix, timeout_in_seconds)
        else:
            return cache

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
        db.session.query(cls).delete()
        db.session.commit()

    @classmethod
    def get(cls, key):
        '''
        get a cache item
        '''
        cache = db.session.query(cls).filter_by(key=key).first()
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
        elif cache.is_outdated(timeout_in_seconds):
            cache.value = value
        db.session.commit()

    def is_outdated(self, timeout_in_seconds):
        return time_diff_in_seconds(utcnow(), self.timestamp) > timeout_in_seconds

    def get_value_as_json(self):
        return json.loads(self.value)

    @classmethod
    def update_timestamp(cls, key):
        '''
        update an existed cache item's timestamp
        '''
        cache = cls.get(key)
        if cache != None:
            cache.timestamp = utcnow()
            db.session.commit()

