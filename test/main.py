#!/usr/bin/env python
# encoding: utf-8

from flask import Flask

application = Flask(__name__)


@application.route('/')
def index():
    return 'Hello, my name is lijunjie.'

if __name__ == '__main__':
    application.debug = True
    application.run()
