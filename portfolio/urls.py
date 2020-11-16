from . import views
from django.urls import path


urlpatterns = [
    path('', views.portfolios, name='portfolios'),
    path('<int:portfolio_id>/', views.portfolio_detail, name='portfolio_detail'),
    path('add_portfolio/', views.add_portfolio, name='add_portfolio'),
]