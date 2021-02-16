# coding: utf-8

from .after_request import log_visitor

def register_after_requests(app):
    app.after_request(log_visitor)

def register_before_requests(app):
    pass
