# coding: utf-8

from .user import register_user_filters, register_user_processors
from .notice import register_notice_filters, register_notice_processors
from .asset import register_asset_processors

from app.libs.date_utils import format_cn
import math
import random

def register_filters(app):
    '''
    global filters for template
    '''
    register_user_filters(app)
    register_notice_filters(app)

    @app.template_filter('datetime_format_cn')
    def datetime_format_cn(datetime):
        return format_cn(datetime)

def register_processors(app):
    '''
    global functions/variables for template
    '''
    register_user_processors(app)
    register_notice_processors(app)
    register_asset_processors(app)

    @app.context_processor
    def inject_common_processors():
        return {
                'math': math,
                'len': len,
                'random': random,
                'str': str
                }

