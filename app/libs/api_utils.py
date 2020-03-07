# coding: utf-8

import json
from app.libs.date_utils import utcnow, datetime_from_seconds, time_diff_in_seconds, parse_datetime
from app.libs.net_utils import get_json
from flask import jsonify, current_app
from app.models import Cache 
from app.libs.dxy_utils import get_overall, get_dxy_json
from app.libs.tx_utils import get_china_provinces_data, get_world_data, get_tx_json

def get_realtime_overall():
    load_timeout = 1800
    def load_from_remote():
        data = get_overall()
        if data == None:
            return None
        return {'key': str(data['updateTime']), 'value': data}

    cache = Cache.try_get_latest_or_update('dxy-overall-', load_timeout, load_from_remote)
    if cache == None:
        return ('not found', 404)
    data = cache.get_value_as_json()
    return {'results': [data]}

def get_cached_tx_json():
    load_timeout = 1800
    def load_from_remote():
        data = get_tx_json()
        if data == None:
            return None
        return {'key': str(data['lastUpdateTime']), 'value': data}

    cache = Cache.try_get_latest_or_update('tx-', load_timeout, load_from_remote)
    if cache == None:
        return 'not found', 404
    data = cache.get_value_as_json()
    return data

def get_cached_dxy_json():
    load_timeout = 1800
    def load_from_remote():
        data = get_dxy_json()
        if data == None:
            return None
        return {'key': str(data['lastUpdateTime']), 'value': data}

    cache = Cache.try_get_latest_or_update('dxy-world-', load_timeout, load_from_remote)
    if cache == None:
        return 'not found', 404
    data = cache.get_value_as_json()
    return data

def get_china_provinces_reports():
    data = get_cached_tx_json()
    return jsonify(get_china_provinces_data(data))

def get_world_reports():
    #return jsonify(get_world_data(get_cached_tx_json()))
    return jsonify(get_cached_dxy_json())

def get_reports_daily():
    data = get_cached_tx_json()
    return jsonify(data)

