import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


class Config:
    # Use it to encrypt or decrypt data
    # SECURITY WARNING: keep the secret key used in production secret!
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'ww+izsrpolxcq68l7fgfu&eptyts9sv3_5@1-i&5!e9=o%#s)w'

    # Django security setting, if your disable debug model, you should setting that
    ALLOWED_HOSTS = ['*']

    # Development env open this, when error occur display the full process track, Production disable it
    DEBUG = os.environ.get("DEBUG") or True
    # DEBUG = True

    # DEBUG, INFO, WARNING, ERROR, CRITICAL can set. See https://docs.djangoproject.com/en/2.1/topics/logging/
    LOG_LEVEL = os.environ.get("LOG_LEVEL") or 'DEBUG'
    LOG_DIR = os.path.join(BASE_DIR, 'logs')

    # Database setting, Support sqlite3, mysql, postgres ....
    # See https://docs.djangoproject.com/en/2.1/ref/settings/#databases

    # SQLite setting:
    DB_ENGINE = 'sqlite3'
    DB_NAME = os.path.join(BASE_DIR, 'data', 'db.sqlite3')

    # MySQL or postgres setting like:
    # DB_ENGINE = os.environ.get("DB_ENGINE") or 'mysql'
    # DB_HOST = os.environ.get("DB_HOST") or '127.0.0.1'
    # DB_PORT = os.environ.get("DB_PORT") or 3306
    # DB_USER = os.environ.get("DB_USER") or 'jumpserver'
    # DB_PASSWORD = os.environ.get("DB_PASSWORD") or 'weakPassword'
    # DB_NAME = os.environ.get("DB_NAME") or 'jumpserver'

    # When Django start it will bind this host and port
    # ./manage.py runserver 127.0.0.1:8080
    # HTTP_BIND_HOST = '0.0.0.0'
    # HTTP_LISTEN_PORT = 8080

    # Use Redis as broker for celery and web socket
    # REDIS_HOST = os.environ.get("REDIS_HOST") or '127.0.0.1'
    # REDIS_PORT = os.environ.get("REDIS_PORT") or 6379
    # REDIS_PASSWORD = os.environ.get("REDIS_PASSWORD") or ''
    # REDIS_DB_CELERY = os.environ.get('REDIS_DB') or 3
    # REDIS_DB_CACHE = os.environ.get('REDIS_DB') or 4

    # Use OpenID authorization
    # BASE_SITE_URL = 'http://localhost:8080'
    # AUTH_OPENID = False  # True or False
    # AUTH_OPENID_SERVER_URL = 'https://openid-auth-server.com/'
    # AUTH_OPENID_REALM_NAME = 'realm-name'
    # AUTH_OPENID_CLIENT_ID = 'client-id'
    # AUTH_OPENID_CLIENT_SECRET = 'client-secret'

    def __init__(self):
        pass

    def __getattr__(self, item):
        return None


class DevelopmentConfig(Config):
    pass


class TestConfig(Config):
    pass


class ProductionConfig(Config):
    DEBUG = False


# Default using Config settings, you can write if/else for different env
config = DevelopmentConfig()
