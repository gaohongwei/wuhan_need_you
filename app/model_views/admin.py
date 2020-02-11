# coding: utf-8

from flask import url_for, redirect, render_template, request, current_app
import flask_admin as admin
import flask_login as login
from flask_admin import helpers, expose
from functools import wraps
from app.forms import LoginForm, RegistrationForm
from app.models import User
from app.models import Visitor 
from app.db import db
from sqlalchemy import func

class AdminIndexView(admin.AdminIndexView):
    @expose('/')
    def index(self):
        print('index')
        if not login.current_user.is_authenticated:
            return redirect(url_for('.login_view'))

        visitor_data = db.session.query(Visitor.url, func.count(Visitor.url)).group_by(Visitor.url).all()
        return self.render('admin/index.html', visitor_data=visitor_data)
        # return super().index()

    @expose('/login/', methods=('GET', 'POST'))
    def login_view(self):
        # handle user login
        print('login')
        current_app.logger.info('login begin...')
        form = LoginForm(request.form)
        if helpers.validate_form_on_submit(form):
            current_app.logger.info('login form validated')
            user = form.get_user()
            if user == None:
                current_app.logger.warn('login failed')
                return redirect(url_for('.login_view'))
            login.login_user(user)
            current_app.logger.info('login success')
        else:
            current_app.logger.warn('login form not validated')

        if login.current_user.is_authenticated:
            return redirect(url_for('.index'))

        # link = '<p>没有帐号? 请点击<a href="' + url_for('.register_view') + '">此处</a>注册。</p>'
        self._template_args['form'] = form
        # self._template_args['link'] = link
        return super().index()

    #@expose('/register/', methods=('GET', 'POST'))
    #def register_view(self):
    #    form = RegistrationForm(request.form)
    #    if helpers.validate_form_on_submit(form):
    #        user = User()

    #        form.populate_obj(user)
    #        # we hash the users password to avoid saving it as plaintext in the db,
    #        # remove to use plain text:
    #        user.set_password(form.password.data)

    #        db.session.add(user)
    #        db.session.commit()

    #        login.login_user(user)
    #        return redirect(url_for('.index'))
    #    link = '<p>已经有帐号？请点击<a href="' + url_for('.login_view') + '">此处</a>登录。</p>'
    #    self._template_args['form'] = form
    #    self._template_args['link'] = link
    #    return super().index()

    @expose('/logout/')
    def logout_view(self):
        login.logout_user()
        return redirect(url_for('.index'))

