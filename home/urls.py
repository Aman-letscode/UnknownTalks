from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='About'),
    path('contact/', views.contact, name='Contact'),
]