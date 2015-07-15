# coding: utf8

# from flask import Flask
# from flask_admin import Admin

# app = Flask(__name__)

# admin = Admin(app)

# if __name__ == '__main__':
    # app.run()

from flask import Flask
from flask_admin import Admin
from flask.ext import admin
from flask.ext.mongoengine import MongoEngine
from flask.ext.admin.contrib.mongoengine import ModelView
import config
import models

app = Flask(__name__)

ad = Admin(app)

app.config.from_object(config.Config)

db = MongoEngine()
db.init_app(app)


# view
class UserView(ModelView):
    column_searchable_list = ('name', 'mobile')
    column_default_sort = ('time', True)


class MerchantView(ModelView):
    column_default_sort = ('time', True)


class CategoryView(ModelView):
    column_default_sort = ('time', True)


class ProductView(ModelView):
    column_default_sort = ('time', True)


class OrderView(ModelView):
    column_default_sort = ('time', True)


if __name__ == '__main__':
    panel = admin.Admin(app)
    panel.add_view(UserView(models.User))
    panel.add_view(MerchantView(models.Merchant))
    panel.add_view(CategoryView(models.Category))
    panel.add_view(ProductView(models.Product))
    panel.add_view(OrderView(models.Order))

    # app.run(host='127.0.0.1', port=2050)
    app.run()
