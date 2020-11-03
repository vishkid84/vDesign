from django.db import models
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from products.models import Category


class Blog(models.Model):
    categories = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL)
    author = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    comment_count = models.IntegerField(default=0)

    def __str__(self):
        return self.title
