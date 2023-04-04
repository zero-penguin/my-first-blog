"""
path関数とblogアプリのすべてのインポート
"""
from django.urls import path
from . import views

#http付きのURLへの対応
urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
]