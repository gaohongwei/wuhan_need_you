# coding: utf-8

import requests

def get_json(url):
    r = requests.get(url)
    return r.json()

