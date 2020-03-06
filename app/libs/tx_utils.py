# coding: utf-8

import json
import requests
from .date_utils import parse_datetime

tx_url = 'https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5'

def parse_time(s):
    return parse_datetime(s, '%Y-%m-%d %H:%M:%S', 'Asia/Shanghai')

def get_tx_json(url=tx_url):
    return json.loads(requests.get(url).json()['data'])

def get_china_provinces_data(data=None):
    data = data or get_tx_json()
    if data == None:
        return []
    areaTree = data.get('areaTree', [])
    if not isinstance(areaTree, list) or len(areaTree) == 0:
        return [] 
    if not isinstance(areaTree[0], dict):
        return []
    provinces = areaTree[0].get('children', [])
    lastUpdateTime = parse_time(data['lastUpdateTime']).isoformat()
    return {'lastUpdateTime': lastUpdateTime, 'data': provinces}

def get_world_data(data=None):
    data = data or get_tx_json()
    if data == None:
        return []
    areaTree = data.get('areaTree', [])
    return {'lastUpdateTime': parse_time(data.get('lastUpdateTime')).isoformat(), 'data': areaTree}

