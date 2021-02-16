# coding: utf-8

from flask import request
from app.models import Visitor

def log_visitor(response):
    url = request.path
    Visitor.add()
    return response

