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
    match = re.search('window.' + name + ' = (.*?)}catch', raw_html)
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
    print('abc')
    raw_html = raw_html or get_html()
    print('def')
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
        res['lastUpdateTime'] = parse_timestamp(country['modifyTime'])
        for i in country:
            res[i] = country[i]
        return res
    provinces = [parseItem(i) for i in get_json('getListByCountryTypeService1')]
    chinaTotal = {
            'confirm': sum([p['total']['confirm'] for p in provinces]),
            'suspect': sum([p['total']['suspect'] for p in provinces]),
            'heal': sum([p['total']['heal'] for p in provinces]),
            'dead': sum([p['total']['dead'] for p in provinces])
            }
    chinaUpdatedTime = max([p['lastUpdateTime'] for p in provinces])
    china = {
            'name': '涓浗',
            'lastUpdateTime': chinaUpdatedTime,
            'total': chinaTotal,
            'children': provinces
            }
    data = [china] + [parseItem(country) for country in data]
    utcTime = max([i['lastUpdateTime'] for i in data])
    for country in data:
        country['lastUpdateTime'] = country['lastUpdateTime'].isoformat()
        for province in country.get('children', []):
            province['lastUpdateTime'] = province['lastUpdateTime'].isoformat()
    return {'data': data, 'lastUpdateTime': utcTime.isoformat()}

def get_dxy_json(raw_html=None):
    return get_world_reports_dxy(raw_html)

