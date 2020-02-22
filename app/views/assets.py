# coding: utf-8

import re
import os
from os.path import join, dirname, abspath
from flask import Blueprint, jsonify, render_template, render_template_string, url_for, current_app, send_from_directory, request
from app.libs.file_utils import match_files
from app.libs.cache_utils import cache_it 

app_dir = join(dirname(abspath(__file__)), '..')
image_dir = join(app_dir, 'static')

@cache_it(timeout=60)
def get_image_files():
    images = match_files(image_dir, ['png', 'jpg', 'jpeg', 'gif'])
    return [f.replace(image_dir, '/static') for f in images]


app = Blueprint('assets', __name__)

@app.route('/assets/test')
def test_asset():
    return render_template_string('{{_asset("test") | safe}}')

@app.route('/api/assets/images', methods=['GET'])
def get_images():
    '''
    /assets/images?page_no=1&page_size=3
    '''
    page_no = (int)(request.args.get('page_no') or 1)
    page_size = (int)(request.args.get('page_size') or 10)
    images = get_image_files()
    urls = images[(page_no-1)*page_size:page_no*page_size]
    return jsonify({'urls': urls, 'total': len(images)})

@app.route('/api/assets/images/<int:id>', methods=['GET'])
def get_image(id):
    images = get_image_files()
    if len(images) > id:
        return images[id]
    else:
        return 'Not found', 404

@app.route('/api/assets/image_select', methods=['GET'])
def render_image_select():
    images = get_image_files()
    page_no = (int)(request.args.get('page_no') or 1)
    page_size = (int)(request.args.get('page_size') or 10)
    div_id = request.args.get('div_id')
    return render_template('admin/assets/image_select.html',
            images = images,
            page_no = page_no,
            page_size = page_size,
            div_id = div_id
            )

@app.route('/assets/test_image_select')
def test_image_select():
    images = get_image_files()
    page_no = (int)(request.args.get('page_no') or 1)
    page_size = (int)(request.args.get('page_size') or 10)
    template = '{% extends "base.html" %} {% block body %} {% include "admin/assets/image_select.html" %} {% endblock body %}'
    return render_template_string(template, images=images, page_no=page_no, page_size=page_size)

