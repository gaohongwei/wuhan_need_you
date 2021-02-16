# coding: utf-8

import requests
from flask import request

def get_json(url):
    r = requests.get(url)
    return r.json()

def get_ip():
    header_list = request.headers.getlist('X-Forwarded-For')
    if header_list:
        return header_list[0]
    else:
        return request.remote_addr
