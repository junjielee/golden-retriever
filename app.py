#!/usr/bin/env python
# encoding: utf-8

from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('app/index.html')


@app.route('/login')
def login():
    return 'Login Page'


@app.route('/logout')
def logout():
    return 'Logout Page'


@app.route('/signup')
def signup():
    return 'Index Page'


@app.route('/order')
def order():
    return render_template('app/order.html')


@app.route('/order/detail')
def order_detail():
    return 'Order detail page'


@app.route('/product')
def product():
    return render_template('app/product.html')


@app.route('/product/detail')
def product_detail():
    return 'Product detail page'

if __name__ == '__main__':
    app.debug = True
    app.run(host='127.0.0.1', port=8000)
