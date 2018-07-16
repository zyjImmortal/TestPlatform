# -*- coding: utf-8 -*-
# @Time    : 2018/7/15 下午12:04
# @Author  : zhouyajun
from django.urls import path

from account import views

app_name = 'account'

urlpatterns = [
    path('login/', views.login, name='login'),
    path('home/', views.home, name='home'),
    path('logout/', views.logout, name='logout')
]