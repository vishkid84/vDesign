from django.urls import path
from . import views


urlpatterns = [
    path('ppt_quote/', views.ppt_quote, name='ppt_quote'),
]