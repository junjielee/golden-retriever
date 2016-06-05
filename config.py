# coding:utf8


class Config(object):
    SECRET_KEY = 'secret'  # need to change
    DEBUG = True

    MONGODB_SETTINGS = {
        'db': 'golden',
        'host': '127.0.0.1',
        'port': 27017
    }

ADMIN_USERNAME = 'admin'
ADMIN_PASSWORD = 'password'  # need to change
