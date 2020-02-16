# coding: utf-8

from flask import Blueprint, render_template
from app.libs.api_utils import get_realtime_overall, get_china_provinces_reports
from app.parameter import menus, report_info

app = Blueprint('reports', __name__)

@app.route('/api/reports/overall')
def api_realtime_overall():
    return get_realtime_overall()

@app.route('/api/reports/provinces')
def api_get_china_provinces_reports():
    return get_china_provinces_reports()


@app.route('/reports')
def test_report():
    return render_template('pages/report_overall.html', menus = menus, pages_info = report_info)

