# coding: utf-8

from flask import (
    Blueprint,
    render_template,
    render_template_string,
    url_for,
    current_app,
    send_from_directory,
    request,
)
from app.parameter import menus, index_info, menus2page
from app.models.Pages import Page

app = Blueprint("pages", __name__)


@app.route("/")
def index():
    return render_template("pages/index.html", menus=menus, pages_info=index_info)


@app.route("/favicon.ico")
def get_favicon():
    return send_from_directory("static", "favicon.ico")


@app.route("/pages/<page_name>")
def menu(page_name):
    cur_page = Page.query.filter_by(name=page_name).first()
    if cur_page != None:
        return cur_page.render(menus=menus)
    pages_info = menus2page.get(page_name, None)
    if pages_info == None:
        return "not found", 404
    return render_template(
            "pages/" + page_name + ".html", menus=menus, pages_info=pages_info
            )
