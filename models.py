# coding: utf8

from mongoengine import Document
from mongoengine.fields import *
from datetime import datetime


class User(Document):
    """客户版用户Model"""
    name = StringField(primary_key=True, max_length=32, verbose_name=u'用户名')
    password = StringField(required=True, max_length=32, verbose_name=u'密码')
    nickname = StringField(required=True, max_length=50, verbose_name=u'真实名称')
    mobile = StringField(max_length=20, verbose_name=u'手机号码')
    level = StringField(default=u'穷B', verbose_name=u'等级')
    total_sales_price = FloatField(default=0, verbose_name=u'总销售额')
    total_sales_feedback = FloatField(default=0, verbose_name=u'总佣金')
    total_sales = IntField(default=0, verbose_name=u'总销售个数')
    time = DateTimeField(default=datetime.now(), verbose_name=u'注册时间')


class Merchant(Document):
    """商家版用户Model"""
    name = StringField(primary_key=True, max_length=32, verbose_name=u'用户名')
    password = StringField(required=True, max_length=32, verbose_name=u'密码')
    nickname = StringField(required=True, max_length=50, verbose_name=u'真实名称')
    mobile = StringField(default=0)
    level = StringField(default=u'穷B', verbose_name=u'等级')
    time = DateTimeField(default=datetime.now(), verbose_name=u'添加时间')


class Category(Document):
    """产品类别Model"""
    id = StringField(primary_key=True, verbose_name=u'类别ID')
    name = StringField(required=True, unique=True, max_length=32,
        verbose_name=u'类别名称')
    count = IntField(default=0, verbose_name=u'包含的产品数量')
    time = DateTimeField(default=datetime.now(), verbose_name=u'添加时间')


class Product(Document):
    """产品Model"""
    id = StringField(primary_key=True, verbose_name=u'类别ID')
    name = StringField(required=True, verbose_name=u'产品名称')
    img = URLField(required=True, verbose_name=u'图片链接')
    img_list = ListField(URLField(), required=True, verbose_name=u'图片列表')
    price_fx = FloatField(required=True, verbose_name=u'平台价')
    price_market = FloatField(required=True, verbose_name=u'市场价')
    stock = IntField(required=True, verbose_name=u'库存')
    sold = IntField(verbose_name=u'销量', default=0)
    phtml = StringField(required=True, verbose_name=u'产品介绍内容')
    feedback = FloatField(required=True, verbose_name=u'佣金')
    category_name = StringField(required=True, max_length=32,
        verbose_name=u'类别名称')
    merchant = ReferenceField('Merchant', verbose_name=u'供应商')
    time = DateTimeField(default=datetime.now(), verbose_name=u'添加时间')


class Order(Document):
    """订单Model"""
    id = StringField(primary_key=True, verbose_name=u'订单ID')
    product = ReferenceField('Product', verbose_name=u'产品')
    user = ReferenceField('User', verbose_name=u'推荐人')
    count = IntField(required=True, verbose_name=u'商品个数')
    total_price = FloatField(required=True, verbose_name=u'总价格')
    total_feedback = FloatField(required=True, verbose_name=u'总佣金')
    status = StringField(verbose_name=u'状态', choices=[('unpaid',u'未付款'),
        ('paid',u'已付款'),('done',u'已完成'),('sent', u'已发货')])
    addr = StringField(required=True, verbose_name=u'收货地址')
    name = StringField(required=True, verbose_name=u'收件人')
    tel = StringField(required=True, verbose_name=u'电话')
    tip = StringField(verbose_name=u'备注')
    delivery_id = StringField(max_length=50, verbose_name=u'快递单号')
    delivery_name = StringField(max_length=50, verbose_name=u'快递名称')
    time = DateTimeField(default=datetime.now(), verbose_name=u'添加时间')
