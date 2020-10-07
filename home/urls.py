from django.contrib import admin
from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
]