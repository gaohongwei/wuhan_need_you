# coding: utf-8

import os
from flask import Blueprint, render_template, render_template_string, url_for, current_app, send_from_directory, request

app = Blueprint('files', __name__)

@app.route('/assets/test')
def test_asset():
    return render_template_string('{{_asset("test") | safe}}')

