# coding: utf-8

import re
import json
import requests
from bs4 import BeautifulSoup
from .date_utils import datetime_from_seconds

dxy_url = 'https://ncov.dxy.cn/ncovh5/view/pneumonia'

def get_html(url=dxy_url):
    return requests.get(url).content.decode('utf-8')

def parse_timestamp(timestamp):
    '''
    parse timestamp in milliseconds since 1970-01-01 00:00:00 Beijing Time
    '''
    return datetime_from_seconds(timestamp * 0.001, 'Asia/Shanghai')

def get_timestamp(raw_html=None):
    '''
    milliseconds since 1970-01-01 00:00:00 Beijing Time
    '''
    raw_html = raw_html or get_html()
    match = re.search('window.timeStamp=([0-9]*)<', raw_html) 
    if match == None:
        return None
    return int(match.group(1))

def get_json(name, raw_html=None):
    raw_html = raw_html or get_html()
    match = re.search('window.' + name + '[a-z]* = (.*?)}catch', raw_html)
    if match == None:
        return None
    raw_json = match.group(1)
    return json.loads(raw_json, encoding='utf-8')

service_names = [
        'getListByCountryTypeService1',
        'getListByCountryTypeService2',
        'getIndexRecommendList',
        'fetchGoodsGuide',
        'getIndexRumorList',
        'getWikiList',
        'getAreaStat',
        'getPV',
        'getTimelineService',
        'getStatisticsService',
        'getEntries'
        ]

def get_overall(raw_html=None):
    raw_html = raw_html or get_html()
    data = get_json('getStatisticsService', raw_html)
    if data == None:
        return None
    data['updateTime'] = get_timestamp(raw_html)
    return data

def get_world_reports_dxy(raw_html=None):
    raw_html = raw_html or get_html()
    data = get_json('getListByCountryTypeService2', raw_html)
    if data == None:
        return None
    def parseItem(country):
        res = {}
        res['name'] = country['provinceName']
        res['total'] = {
                'confirm': country['confirmedCount'],
                'suspect': country['suspectedCount'],
                'heal': country['curedCount'],
                'dead': country['deadCount']
                }
        modifyTime = country.get('modifyTime', None)
        res['lastUpdateTime'] = parse_timestamp(country.get('modifyTime', None)) if modifyTime else None
        for i in country:
            res[i] = country[i]
        return res
    provinces = (get_json('getListByCountryTypeService1', raw_html) \
            or get_json('getAreaStat', raw_html)
            or []
            )
    if len(provinces) == 0:
        print('Error: parse china data from dxy failed')
    provinces = [parseItem(i) for i in provinces]
    chinaTotal = {
            'confirm': sum([p['total']['confirm'] for p in provinces]),
            'suspect': sum([p['total']['suspect'] for p in provinces]),
            'heal': sum([p['total']['heal'] for p in provinces]),
            'dead': sum([p['total']['dead'] for p in provinces])
            }
    def maxByKey(d, key):
        items = [i.get(key, None) for i in d if i != None]
        items = [i for i in items if i != None]
        if len(items) == 0:
            return None
        return max(items)
    def isoformat(date):
        return date.isoformat() if date != None else 'null'
    provincesUpdateTimes = [p['lastUpdateTime'] for p in provinces if p['lastUpdateTime'] != None]
    chinaUpdatedTime = maxByKey(provinces, 'lastUpdateTime')
    china = {
            'name': '中国',
            'lastUpdateTime': chinaUpdatedTime,
            'total': chinaTotal,
            'children': provinces
            }
    data = [china] + [parseItem(country) for country in data]
    utcTime = maxByKey(data, 'lastUpdateTime')
    for country in data:
        country['lastUpdateTime'] = isoformat(country['lastUpdateTime'])
        for province in country.get('children', []):
            province['lastUpdateTime'] = isoformat(province['lastUpdateTime'])
    return {'data': data, 'lastUpdateTime': isoformat(utcTime)}

def get_dxy_json(raw_html=None):
    return get_world_reports_dxy(raw_html)

if __name__ == '__main__':
    print(get_dxy_json())
