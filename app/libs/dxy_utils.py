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
    print(data['updateTime'])
    return data

