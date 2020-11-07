from django.urls import path
from . import views


urlpatterns = [
    path('', views.blogs, name='blogs'),
    path('<int:blog_id>/', views.blog_detail, name='blog_detail'),
    path('add_blog/', views.add_blog, name='add_blog'),
    path('edit_blog/<int:blog_id>/', views.edit_blog, name='edit_blog'),
    path('delete_blog/<int:blog_id>/', views.delete_blog, name='delete_blog'),
    path('edit_comment/<int:blog_id>/<int:comment_id>/', views.edit_comment, name='edit_comment'),
    path('delete_comment/<int:blog_id>/<int:comment_id>/', views.delete_comment, name='delete_comment'),
]