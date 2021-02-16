# coding: utf-8

from flask import url_for, redirect, render_template, request, current_app
import flask_admin as admin
import flask_login as login
from flask_admin import helpers, expose
from app.forms import LoginForm, RegistrationForm
from app.models import Visitor 
from app.db import db
from sqlalchemy import func

class AdminIndexView(admin.AdminIndexView):
    @expose('/')
    def index(self):
        print('index')
        if not login.current_user.is_authenticated:
            return redirect(url_for('.login_view'))

        data = Visitor.statistics(1, 10)
        return self.render('admin/index.html', visitor_data=data.items)

    @expose('/login/', methods=('GET', 'POST'))
    def login_view(self):
        # handle user login
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

        self._template_args['form'] = form
        return super().index()

    @expose('/logout/')
    def logout_view(self):
        login.logout_user()
        return redirect(url_for('.index'))

