# coding: utf-8

import json
import requests

tx_url = 'https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5'

def get_json(url=tx_url):
    print(requests.get(url).json())
    return json.loads(requests.get(url).json()['data'])

print(get_json())
