
from flask import url_for, redirect, render_template, request
import flask_admin as admin
import flask_login as login
from flask_admin import helpers, expose
from app.forms import LoginForm, RegistrationForm
from app.models import User
from app.db import db

class AdminIndexView(admin.AdminIndexView):
    @expose('/')
    def index(self):
        if not login.current_user.is_authenticated:
            return redirect(url_for('.login_view'))
        return super(AdminIndexView, self).index()

    @expose('/login/', methods=('GET', 'POST'))
    def login_view(self):
        # handle user login
        form = LoginForm(request.form)
        if helpers.validate_form_on_submit(form):
            user = form.get_user()
            if user == None:
                return redirect(url_for('.login_view'))
            login.login_user(user)

        if login.current_user.is_authenticated:
            return redirect(url_for('.index'))

        link = '<p>没有帐号? 请点击<a href="' + url_for('.register_view') + '">此处</a>注册。</p>'
        self._template_args['form'] = form
        self._template_args['link'] = link
        return super(AdminIndexView, self).index()

    @expose('/register/', methods=('GET', 'POST'))
    def register_view(self):
        form = RegistrationForm(request.form)
        if helpers.validate_form_on_submit(form):
            user = User()

            form.populate_obj(user)
            # we hash the users password to avoid saving it as plaintext in the db,
            # remove to use plain text:
            user.set_password(form.password.data)

            db.session.add(user)
            db.session.commit()

            login.login_user(user)
            return redirect(url_for('.index'))
        link = '<p>已经有帐号？请点击<a href="' + url_for('.login_view') + '">此处</a>登陆。</p>'
        self._template_args['form'] = form
        self._template_args['link'] = link
        return super(AdminIndexView, self).index()

    @expose('/logout/')
    def logout_view(self):
        login.logout_user()
        return redirect(url_for('.index'))

