
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('blogcomments',views.blogComments,name="blogcomments"),
    path('', views.blog, name='Blog'),
    path('addblog', views.addblog,name="addBlog"),
    path('<str:slug>', views.blogPost, name='blogPost'),
]