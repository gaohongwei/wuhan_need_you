import os
import logging
from flask import Flask
from .libs.AlchemyEncoder import AlchemyEncoder

basedir = os.path.abspath(os.path.dirname(__file__))
logPath = os.environ.get('LOG_DIR') or os.path.join(basedir, '..', 'logs')

DEV_DATABASE_URL = os.environ.get('DEV_DATABASE_URL') \
        or 'postgres://postgres:12345678@127.0.0.1:5432/wuhan_need_you'
TEST_DATABASE_URL = os.environ.get('TEST_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data-test.sqlite')

class InfoFilter(logging.Filter):
    '''
    Only use INFO log
    '''
    def filter(self, record):
        if logging.INFO <= record.levelno < logging.ERROR:
            return super().filter(record)
        else:
            return 0

class Config:
    DEBUG = True
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    SSL_DISABLE = False
    SQLALCHEMY_RECORD_QUERIES = True

    FLASK_ADMIN_SWATCH = 'cerulean'
 
    LOG_PATH = logPath
    LOG_PATH_ERROR = os.path.join(LOG_PATH, 'error.log')
    LOG_PATH_INFO = os.path.join(LOG_PATH, 'info.log')
    LOG_FILE_MAX_BYTES = 100 * 1024 * 1024
    # 轮转数量是 10 个
    LOG_FILE_BACKUP_COUNT = 10

    NOTICES_PER_PAGE = 20
 
    @staticmethod
    def init_app(app):
        pass
 
class DeploymentConfig(Config):
    DEBUG = False
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SQLALCHEMY_DATABASE_URI = DEV_DATABASE_URL
 
    @classmethod
    def init_app(cls, app):
        Config.init_app(app)
 
        # email errors to the administrators
        import logging
        from logging.handlers import RotatingFileHandler
        # Formatter
        formatter = logging.Formatter(
            '%(asctime)s %(levelname)s %(process)d %(thread)d '
            '%(pathname)s %(lineno)s %(message)s')
 
 
        # FileHandler Info
        file_handler_info = RotatingFileHandler(filename=cls.LOG_PATH_INFO)
        file_handler_info.setFormatter(formatter)
        file_handler_info.setLevel(logging.INFO)
        info_filter = InfoFilter()
        file_handler_info.addFilter(info_filter)
        app.logger.addHandler(file_handler_info)
 
        # FileHandler Error
        file_handler_error = RotatingFileHandler(filename=cls.LOG_PATH_ERROR)
        file_handler_error.setFormatter(formatter)
        file_handler_error.setLevel(logging.ERROR)
        app.logger.addHandler(file_handler_error)
 
class DevelopmentConfig(Config):
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SQLALCHEMY_DATABASE_URI = DEV_DATABASE_URL
 
    @classmethod
    def init_app(cls, app):
        Config.init_app(app)
 
        # email errors to the administrators
        import logging
        from logging.handlers import RotatingFileHandler
        # Formatter
        formatter = logging.Formatter(
            '%(asctime)s %(levelname)s %(process)d %(thread)d '
            '%(pathname)s %(lineno)s %(message)s')
 
 
        # FileHandler Info
        file_handler_info = RotatingFileHandler(filename=cls.LOG_PATH_INFO)
        file_handler_info.setFormatter(formatter)
        file_handler_info.setLevel(logging.INFO)
        info_filter = InfoFilter()
        file_handler_info.addFilter(info_filter)
        app.logger.addHandler(file_handler_info)
 
        # FileHandler Error
        file_handler_error = RotatingFileHandler(filename=cls.LOG_PATH_ERROR)
        file_handler_error.setFormatter(formatter)
        file_handler_error.setLevel(logging.ERROR)
        app.logger.addHandler(file_handler_error)
 
 
class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = TEST_DATABASE_URL
    WTF_CSRF_ENABLED = False
    SQLALCHEMY_ECHO = True


config = {
    'depolyment': DeploymentConfig,
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'default': TestingConfig
    }

# use TestingConfig by default
def create_app(config_name):
    try:
        os.mkdir(logPath)
    except Exception as e:
        pass
    app = Flask(__name__, instance_relative_config=True)
    app.json_encoder = AlchemyEncoder
    conf = config.get(config_name, config['default'])
    app.config.from_object(conf)
    conf.init_app(app)
    app.logger.info('Application is running in {} mode'.format(conf.__name__))
    return app

