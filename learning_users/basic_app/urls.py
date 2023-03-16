from django.contrib import admin
from django.conf.urls import url
from django.urls import path, include
from basic_app import views

app_name = 'basic_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path(r'^user_login/$', views.user_login, name='user_login')
]