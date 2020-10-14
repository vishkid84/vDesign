from . import views
from django.urls import path

urlpatterns = [
    path('', views.view_bag, name='view_bag'),
]