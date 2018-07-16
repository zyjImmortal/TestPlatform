# -*- coding: utf-8 -*-
# @Time    : 2018/7/15 下午12:10
# @Author  : zhouyajun
from django.urls import path
from apitest import views

app_name = 'apitest'

urlpatterns = [
    path('apicases/', views.api_test_manage, name='api_manage'),
    path('apistep/', views.api_step_manage, name='step_manage'),
    path('apimanage/', views.api_manage, name='api_manage')
]