# coding: utf-8

import json
from app.libs.date_utils import utcnow, datetime_from_seconds, time_diff_in_seconds, parse_datetime
from app.libs.net_utils import get_json
from flask import jsonify, current_app
from app.models import Cache, TXCache
from app.libs.dxy_utils import get_overall
from app.libs.tx_utils import get_china_provinces_data, get_world_data, get_tx_json


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
    server_timeout = 3600 * 1 #  3 hour
    load_timeout = 1800
    data, cache = get_realtime_overall_from_cache()
    def checkout_server():
        data = get_overall()
        if data == None:
            return 'fail to get data, no data exist', 404
        Cache.set(str(data['updateTime']), json.dumps(data))
        return jsonify({'results': [data]})
    if data == None:
        return checkout_server()
    else:
        updateTime = data['updateTime']
        if updateTime == None:
            current_app.logger.error('updateTime is None')
            return checkout_server()
        seconds = updateTime * 0.001 - 8*3600 # Beijing -> UTC
        dataTime = datetime_from_seconds(seconds)  # UTC
        current_app.logger.info('last update time: ' + str(cache.timestamp))
        current_app.logger.info('last server update time: ' + str(dataTime))
        now = utcnow()
        current_app.logger.info('current time: ' + str(now))
        if time_diff_in_seconds(now, dataTime) >= server_timeout and time_diff_in_seconds(now, cache.timestamp) >= load_timeout:
            return checkout_server()
        else:
            return jsonify({'results': [data]})

def get_tx_json_from_cache():
    cache = TXCache.get_latest()
    if cache == None:
        current_app.logger.info('no cache for tx data')
        return None, None
    data = json.loads(cache.value)
    current_app.logger.info('get tx data from cache')
    return data, cache

def get_cached_tx_json():
    # UTC
    def getLastUpdateTimeSeconds(data):
        if data == None:
            return None
        lastUpdateTime = data.get('lastUpdateTime', None)
        if lastUpdateTime == None:
            current_app.logger.error('lastUpdateTime is None')
            return None
        t = parse_datetime(lastUpdateTime, '%Y-%m-%d %H:%M:%S', 'Asia/Shanghai')
        return int(t.timestamp())
    def addCache(data):
        if data == None:
            current_app.logger.error('fail to add None cache')
            return
        current_app.logger.info('add cache for tx-data with Beigjin time ' + data['lastUpdateTime'])
        TXCache.set(data['lastUpdateTime'], json.dumps(data))
    server_timeout = 3600 * 1 #  3 hour
    load_timeout = 1800
    data, cache = get_tx_json_from_cache()
    if data == None:
        data = get_tx_json()
        if data == None:
            return 'fail to get data, no data exist', 404
        addCache(data)
        return data
    else:
        seconds = getLastUpdateTimeSeconds(data)
        dataTime = datetime_from_seconds(seconds)
        current_app.logger.info('last tx-data update time: ' + str(cache.timestamp))
        current_app.logger.info('last tx-data server update time: ' + str(dataTime))
        now = utcnow()
        current_app.logger.info('current time: ' + str(now))
        if time_diff_in_seconds(now, dataTime) >= server_timeout and time_diff_in_seconds(now, cache.timestamp) >= load_timeout:
            current_app.logger.info('checkout the server')
            data2 = get_tx_json()
            addCache(data2)
            return data2
        else:
            return data

def get_china_provinces_reports():
    data = get_cached_tx_json()
    return jsonify(get_china_provinces_data(data))

def get_world_reports():
    data = get_cached_tx_json()
    return jsonify(get_world_data(data))

def get_reports_daily():
    data = get_cached_tx_json()
    return jsonify(data)

