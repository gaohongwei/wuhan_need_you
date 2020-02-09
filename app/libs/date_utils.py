# coding: utf-8

from datetime import datetime, timezone, timedelta
from dateutil import tz

def utcnow():
    '''
    return datetime without timezone info, while datetime.utcnow contains timezone info
    '''
    return datetime.now(timezone.utc)

def as_timezone(time, to_zone_name='Asia/ShangHai', from_zone_name='UTC'):
    '''
    Convert a time from a zone to another zone
    time: if time.tzinfo is None, consider it is a UTC time
    '''
    from_zone = tz.gettz(from_zone_name)
    to_zone = tz.gettz(to_zone_name)
    if time.tzinfo == None:
        time = time.replace(tzinfo=from_zone)
    return time.astimezone(to_zone)

def set_timezone(time, zone_name='UTC'):
    if time == None:
        return time
    return time.replace(tzinfo = tz.gettz(zone_name))

def datetime_from_seconds(seconds, timezone_name='UTC'):
    dt = datetime(1970, 1, 1, tzinfo=tz.gettz(timezone_name))
    return dt + timedelta(seconds=seconds)

def time_diff_in_seconds(t1, t2):
    '''
    t1 - t2
    '''
    if t1.tzinfo == None:
        t1 = set_timezone(t1, 'UTC')
    if t2.tzinfo == None:
        t2 = set_timezone(t2, 'UTC')
    return (t1 - t2).total_seconds()

