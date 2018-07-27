from django.urls import path

from app import views

app_name = 'app'

urlpatterns = [
    path('case/', views.app_case_manage, name='app_case_manage'),
    path('step/case/', views.app_case_step_manage, name='app_case_step_manage')
]