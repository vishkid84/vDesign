from . import views
from django.urls import path

urlpatterns = [
    path('', views.products, name='products'),
    path('<int:product_id>/', views.product_detail, name='product_detail'),
]