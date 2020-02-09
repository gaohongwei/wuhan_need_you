# coding: utf-8

from datetime import datetime, timezone, timedelta
from dateutil import tz

def utcnow():
    '''
    return datetime without timezone info, while datetime.utcnow contains timezone info
    '''
    return datetime.now(timezone.utc)

def utc_offset(offset):
    '''
    offset in hours
    '''
    return timezone(timedelta(seconds=offset*3600))

def now_with_timezone_offset(offset):
    '''
    Get current time in a timezone with offset, e.g. in Beijing time: now_with_timezone_offset(8)
    '''
    return datetime.now(utc_offset(offset))

def get_utc_offset(dt):
    '''
    offset in hours
    '''
    if dt.tzinfo == None:
        return 0
    return int(dt.utcoffset().seconds / 3600)

def as_timezone(time, to_zone_name='Asia/ShangHai', from_zone_name='UTC'):
    '''
    Convert a time from a zone to another zone
    time: if time.tzinfo is None, consider it is a UTC time
    '''
    if time == None:
        return None
    from_zone = tz.gettz(from_zone_name)
    to_zone = tz.gettz(to_zone_name)
    if time.tzinfo == None:
        time = time.replace(tzinfo=from_zone)
    return time.astimezone(to_zone)

def format_cn(time):
    if time == None or not isinstance(time, datetime):
        return ''
    year = time.year
    month = time.month
    day = time.day
    hour = time.hour
    minute = time.minute
    second = int(time.second)
    time_str = '{}年{:02d}月{:02d}日{:02d}:{:02d}:{:02d}'.format(year, month, day, hour, minute, second)
    tz_offset = get_utc_offset(time)
    tz_str = '(UTC时间)'
    if tz_offset == 8:
        tz_str = '(北京时间)'
    elif tz_offset > 0:
        tz_str = '(东{}区时间)'.format(tz_offset)
    elif tz_offset < 0:
        tz_str = '(西{}区时间)'.format(-tz_offset)
    return time_str + tz_str

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

