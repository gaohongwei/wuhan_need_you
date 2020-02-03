from datetime import datetime, timezone
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

