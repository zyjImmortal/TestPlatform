# -*- coding: utf-8 -*-
# @Time    : 2018/7/22 下午2:27
# @Author  : zhouyajun
from django.urls import path
from bug import views

app_name = 'bug'

urlpatterns = [
    path('manage/', views.bug_manage, name='bug_manage')
]