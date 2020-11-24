from django.contrib import admin
from .models import Blog, BlogComment


class BlogAdmin(admin.ModelAdmin):

    list_display = (
        'author',
        'title',
        'content',
        'date',
    )

admin.site.register(Blog, BlogAdmin)


class BlogCommentAdmin(admin.ModelAdmin):

    list_display = (
        'user',
        'date',
        'comment_content',
        'blog',
    )

admin.site.register(BlogComment, BlogCommentAdmin)
