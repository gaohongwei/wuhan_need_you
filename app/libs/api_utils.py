# coding: utf-8

import json
from app.libs.date_utils import utcnow, datetime_from_seconds, time_diff_in_seconds
from app.libs.net_utils import get_json
from flask import jsonify, current_app
from app.models import Cache
from app.libs.dxy_utils import get_overall


def get_realtime_overall_from_server():
    current_app.logger.info('get overall from server')
    data = get_json('https://lab.isaaclin.cn/nCoV/api/overall')
    if data == None:
        return None
    return data['results'][0];

def get_realtime_overall_from_cache():
    current_app.logger.info('get overall from cache')
    cache = Cache.get_latest()
    if cache == None:
        return None, None
    data = json.loads(cache.value)
    return data, cache
def get_realtime_overall():
    server_timeout = 3600 * 3 #  3 hour
    load_timeout = 3600
    data, cache = get_realtime_overall_from_cache()
    if data == None:
        data = get_overall()
        if data == None:
            return 'fail to get data, no data exist', 404
        Cache.set(str(data['updateTime']), json.dumps(data))
        return jsonify({'results': [data]})
    else:
        seconds = data['updateTime'] * 0.001 - 8*3600 # Beijing -> UTC
        dataTime = datetime_from_seconds(seconds)  # UTC
        current_app.logger.info('last update time: ' + str(cache.timestamp))
        current_app.logger.info('last server update time: ' + str(dataTime))
        now = utcnow()
        current_app.logger.info('current time: ' + str(now))
        if time_diff_in_seconds(now, dataTime) >= server_timeout or time_diff_in_seconds(now, cache.timestamp) >= load_timeout:
            current_app.logger.info('checkout the server')
            data2 = get_overall()
            Cache.set(str(data2['updateTime']), json.dumps(data2))
            return jsonify({'results': [data2]})
        else:
            return jsonify({'results': [data]})

