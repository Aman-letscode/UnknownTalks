from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog, name='Blog'),
    path('<str:slug>', views.blogPost, name='blogPost'),
]