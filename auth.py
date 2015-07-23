#!/usr/bin/env python
# encoding: utf-8

from flask import request, make_response
from functools import wraps

from config import ADMIN_USERNAME, ADMIN_PASSWORD


def _check_auth(username, password):
    return username == ADMIN_USERNAME and password == ADMIN_PASSWORD


def _authenticate():
    resp = make_response('<h1>403 Forbidden</h1>')
    resp.status_code = 401
    resp.headers['WWW-Authenticate'] = 'Basic realm="j********"'
    return resp


def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kw):
        if '/static/' not in request.url:
            auth = request.authorization
            if not auth:
                return _authenticate()
            elif not _check_auth(auth.username, auth.password):
                return _authenticate()
        return f(*args, **kw)

    return decorated
