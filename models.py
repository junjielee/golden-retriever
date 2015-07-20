# coding: utf8

from flask.ext.mongoengine import MongoEngine
from datetime import datetime

db = MongoEngine()


class User(db.Document):
    """客户版用户Model"""
    name = db.StringField(primary_key=True, max_length=32, verbose_name=u'用户名')
    password = db.StringField(required=True, max_length=32, verbose_name=u'密码')
    nickname = db.StringField(required=True, max_length=50, verbose_name=u'真实名称')
    mobile = db.StringField(max_length=20, verbose_name=u'手机号码')
    level = db.StringField(default=u'穷B', verbose_name=u'等级')
    total_sales_price = db.FloatField(default=0, verbose_name=u'总销售额')
    total_sales_feedback = db.FloatField(default=0, verbose_name=u'总佣金')
    total_sales = db.IntField(default=0, verbose_name=u'总销售个数')
    time = db.DateTimeField(default=datetime.now(), verbose_name=u'注册时间')


class Merchant(db.Document):
    """商家版用户Model"""
    name = db.StringField(primary_key=True, max_length=32, verbose_name=u'用户名')
    password = db.StringField(required=True, max_length=32, verbose_name=u'密码')
    nickname = db.StringField(required=True, max_length=50, verbose_name=u'真实名称')
    mobile = db.StringField(default=0)
    level = db.StringField(default=u'穷B', verbose_name=u'等级')
    time = db.DateTimeField(default=datetime.now(), verbose_name=u'添加时间')


class Category(db.Document):
    """产品类别Model"""
    id = db.StringField(primary_key=True, verbose_name=u'类别ID')
    name = db.StringField(required=True, unique=True, max_length=32,
                          verbose_name=u'类别名称')
    count = db.IntField(default=0, verbose_name=u'包含的产品数量')
    time = db.DateTimeField(default=datetime.now(), verbose_name=u'添加时间')


class Product(db.Document):
    """产品Model"""
    id = db.StringField(primary_key=True, verbose_name=u'类别ID')
    name = db.StringField(required=True, verbose_name=u'产品名称')
    img = db.URLField(required=True, verbose_name=u'图片链接')
    img_list = db.ListField(db.URLField(), required=True, verbose_name=u'图片列表')
    price_fx = db.FloatField(required=True, verbose_name=u'平台价')
    price_market = db.FloatField(required=True, verbose_name=u'市场价')
    stock = db.IntField(required=True, verbose_name=u'库存')
    sold = db.IntField(verbose_name=u'销量', default=0)
    phtml = db.StringField(required=True, verbose_name=u'产品介绍内容')
    feedback = db.FloatField(required=True, verbose_name=u'佣金')
    category_name = db.StringField(required=True, max_length=32,
                                   verbose_name=u'类别名称')
    merchant = db.ReferenceField('Merchant', verbose_name=u'供应商')
    time = db.DateTimeField(default=datetime.now(), verbose_name=u'添加时间')


class Order(db.Document):
    """订单Model"""
    id = db.StringField(primary_key=True, verbose_name=u'订单ID')
    product = db.ReferenceField('Product', verbose_name=u'产品')
    user = db.ReferenceField('User', verbose_name=u'推荐人')
    count = db.IntField(required=True, verbose_name=u'商品个数')
    total_price = db.FloatField(required=True, verbose_name=u'总价格')
    total_feedback = db.FloatField(required=True, verbose_name=u'总佣金')
    status = db.StringField(verbose_name=u'状态',
                            choices=[('unpaid', u'未付款'),
                                     ('paid', u'已付款'),
                                     ('done', u'已完成'),
                                     ('sent', u'已发货')])
    addr = db.StringField(required=True, verbose_name=u'收货地址')
    name = db.StringField(required=True, verbose_name=u'收件人')
    tel = db.StringField(required=True, verbose_name=u'电话')
    tip = db.StringField(verbose_name=u'备注')
    delivery_id = db.StringField(max_length=50, verbose_name=u'快递单号')
    delivery_name = db.StringField(max_length=50, verbose_name=u'快递名称')
    time = db.DateTimeField(default=datetime.now(), verbose_name=u'添加时间')
