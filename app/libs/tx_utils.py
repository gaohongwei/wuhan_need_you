# coding: utf-8

import json
import requests

tx_url = 'https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5'

def get_tx_json(url=tx_url):
    return json.loads(requests.get(url).json()['data'])

def get_china_provinces_data():
    data = get_tx_json()
    if data == None:
        return []
    areaTree = data.get('areaTree', [])
    if not isinstance(areaTree, list) or len(areaTree) == 0:
        return [] 
    if not isinstance(areaTree[0], dict):
        return []
    return areaTree[0].get('children', [])

