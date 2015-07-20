# coding: utf8

# from flask_admin import Admin
# from flask_admin.contrib.mongoengine import ModelView
from flask import Flask
from flask.ext.admin import Admin, AdminIndexView
from flask.ext.mongoengine import MongoEngine
from flask.ext.admin.contrib.mongoengine import ModelView
from flask.ext.admin import expose
import config
import models

app = Flask(__name__)

app.config.from_object(config.Config)

db = MongoEngine()
db.init_app(app)


class UserView(ModelView):
    column_searchable_list = ('name', 'mobile')
    column_default_sort = ('time', True)


class MerchantView(ModelView):
    pass


class CategoryView(ModelView):
    pass


class ProductView(ModelView):
    pass


class OrderView(ModelView):
    pass


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
