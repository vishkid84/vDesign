from django.urls import path
from . import views


urlpatterns = [
    path('ppt_quote/', views.ppt_quote, name='ppt_quote'),
    path('ppt_quote_out/', views.ppt_quote_out, name='ppt_quote_out'),
    path('ppt_quote_detail/<int:project_id>/', views.ppt_quote_detail, name='ppt_quote_detail'),
    path('web_quote/', views.web_quote, name='web_quote'),
]
