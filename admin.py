# coding: utf8

# from flask_admin import Admin
# from flask_admin.contrib.mongoengine import ModelView
from flask import Flask
from flask.ext.admin import Admin, AdminIndexView
from flask.ext.mongoengine import MongoEngine
from flask.ext.admin.contrib.mongoengine import ModelView
from flask.ext.admin import expose

from config import Config
import models

app = Flask(__name__)
app.DEBUG = True

app.config.from_object(Config)

db = MongoEngine()
db.init_app(app)


def time_format(v, c, m, p):
    return m.time.strftime('%Y-%m-%d')


class UserView(ModelView):
    column_exclude_list = ('password')
    column_searchable_list = ('name', 'mobile')
    column_default_sort = ('time', True)
    can_delete = True
    column_labels = dict(
        name=u'用户名',
        nickname=u'姓名',
        mobile=u'手机',
        level=u'等级',
        total_sales_price=u'总销售额',
        total_sales_feedback=u'历史总佣金',
        total_sales=u'总销售个数',
        cur_feedback=u'当前佣金',
        time=u'注册时间',
    )
    column_formatters = dict(
        time=time_format
    )
    form_create_rules = ('name', 'password', 'nickname', 'mobile', 'level')
    # 无反应
    column_choices = {
        'level': models.ORDER_STATUS_CHOICES
    }


class MerchantView(ModelView):
    column_exclude_list = ('password')
    column_searchable_list = ('name', 'mobile')
    column_default_sort = ('time', True)
    can_delete = True
    column_labels = dict(
        name=u'用户名',
        nickname=u'姓名',
        mobile=u'手机',
        level=u'等级',
        time=u'注册时间',
    )
    column_formatters = dict(
        time=time_format
    )


class CategoryView(ModelView):
    column_searchable_list = ('name',)
    column_default_sort = ('time', True)
    can_delete = True
    column_labels = dict(
        name=u'类别名称',
        count=u'类别数量',
        time=u'添加时间',
    )
    column_formatters = dict(
        time=time_format
    )


class ProductView(ModelView):
    column_exclude_list = ('img_list', 'phtml',)
    column_searchable_list = ('name',)
    column_default_sort = ('time', True)
    can_delete = True
    column_labels = dict(
        name=u'产品名称',
        img=u'图片',
        price_fx=u'平台价',
        price_market=u'市场价',
        stock=u'库存',
        sold=u'销量',
        feedback=u'佣金',
        category=u'类别',
        merchant=u'供应商',
        time=u'添加时间',
    )
    column_formatters = dict(
        time=time_format
    )


class OrderView(ModelView):
    column_exclude_list = ('addr', 'tip', 'delivery_id', 'delivery_name',)
    column_searchable_list = ('tel',)
    column_default_sort = ('time', True)
    can_delete = True
    column_labels = dict(
        product=u'产品',
        user=u'推荐人',
        count=u'数量',
        total_price=u'总金额',
        total_feedback=u'总佣金',
        status=u'状态',
        name=u'收件人',
        tel=u'手机',
        merchant=u'供应商',
        time=u'添加时间',
    )
    column_formatters = dict(
        time=time_format
    )


class IndexView(AdminIndexView):
    @expose('/', methods=['GET', 'POST'])
    def index(self):
        return self.render('index.html')


panel = Admin(app, name='Golden', index_view=IndexView(name=u'主页'))
panel.add_view(UserView(models.User, name=u'用户'))
panel.add_view(MerchantView(models.Merchant, name=u'商家'))
panel.add_view(CategoryView(models.Category, name=u'类别'))
panel.add_view(ProductView(models.Product, name=u'产品'))
panel.add_view(OrderView(models.Order, name=u'订单'))

if __name__ == '__main__':
    # app.run(host='127.0.0.1', port=2050)
    app.run()
