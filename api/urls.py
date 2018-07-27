# -*- coding: utf-8 -*-
# @Time    : 2018/7/15 下午12:10
# @Author  : zhouyajun
from django.urls import path
from api import views

app_name = 'api'

urlpatterns = [
    path('cases/', views.api_test_manage, name='api_manage'),
    path('step/', views.api_step_manage, name='step_manage'),
    path('manage/', views.api_manage, name='api_manage')
]