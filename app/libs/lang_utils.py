# coding: utf-8

from flask import Flask, jsonify, request, render_template_string, session
from flask_language import Language, current_language
from flask_babelex import Babel
from flask_googletrans import google_translator

__all__ = ['init_babel']

def _init_language(app):
    '''
    flask-language automatically set 'lang' in cookies
    '''
    lang = Language(app)
    @lang.allowed_languages
    def get_allowed_languages():
        return app.config.get('LANGUAGES', ['en', 'zh'])
    @lang.default_language
    def get_default_language():
        return app.config.get('DEFAULT_LANGUAGE', 'en')
    @app.route('/api/language')
    def get_language():
        return jsonify({'language': str(current_language)})
    @app.route('/api/language', methods=['POST'])
    def set_language():
        req = request.json
        print(request)
        print(req)
        language = req.get('language', None)
        lang.change_language(language)
        return jsonify({'language': str(current_language)})
    @app.route('/api/language/test')
    def test_language():
        template = '''
        <a {{'disabled' if lang=='en' else ''}}" href="javascript:setLang('en')">en</a>
        &nbsp;
        <a {{'disabled' if lang=='zh' else ''}} href="javascript:setLang('zh')">涓枃</a>
        </br>
        <div>Cookies.lang: <span id='cookie_lang'></span></div>
        <div>妯℃澘(<code>_('涓婚〉')</code>): {{_('涓婚〉')}}</div>
        <script>
        window.addEventListener('load', () => {
            document.getElementById('cookie_lang').innerText = getCookie('lang');
        });
        function post(url, json) {
            const req = new XMLHttpRequest();
            return new Promise((resolve, reject) => {
                req.onreadystatechange = function () {
                    if (this.readyState === XMLHttpRequest.DONE && this.status === 200) {
                        resolve(JSON.parse(this.responseText)); 
                    }
                };
                req.open('POST', url, true);
                req.setRequestHeader('Content-Type', 'application/json');
                req.send(JSON.stringify(json));
            });
        }
        function setLang(lang) {
            post('/api/language', {language: lang}).then(() => {
                reload();
            });
        }
        function getCookie (name) {
            var match = document.cookie.match(new RegExp('(^| )' + name + '=([^;]+)'));
            if (match) return match[2];
        }
        function reload() {
            location.reload(true);
        }
        </script>
        '''
        return render_template_string(template, lang=str(current_language))
    return lang

def init_babel(app):
    # Use Flask Babel to support multi-languages
    babel = Babel(app)
    lang = _init_language(app)
    @babel.localeselector
    def get_locale():
        language = str(current_language)
        session['lang'] = language
        return language
    return {'babel': babel, 'lang': lang}

def translate(text, src='cn', dest='en'):
    translator = google_translator()
    res = translator.translate(text, src=src, dest=dest)
    return res.text

