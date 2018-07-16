# -*- coding: utf-8 -*-
# @Time    : 2018/7/15 下午2:40
# @Author  : zhouyajun
from django.urls import path
from product import views
app_name = 'product'

urlpatterns = [
    path('manage/', views.product_manage, name='manage')
]