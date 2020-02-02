# config.py

# Enable Flask's debugging features. Should be False in production
DEBUG = True

# SQLALCHEMY_DATABASE_URI = 'postgresql://localhost/whu'
SQLALCHEMY_DATABASE_URI = 'sqlite:///./test2.db'

FLASK_ADMIN_SWATCH = 'cerulean'

SECRET_KEY = 'dev' # production env should be different