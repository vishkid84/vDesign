from django.db import models
from django.contrib.auth.models import User
from products.models import Category


class Blog(models.Model):
    category = models.ForeignKey(
               Category, null=True, blank=True, on_delete=models.SET_NULL)
    author = models.ForeignKey(
               User, null=True, blank=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    comment_count = models.IntegerField(default=0)

    class Meta:
        ordering = ['-date']

    @property
    def get_comments(self):
        return self.comments.all().order_by('-date')

    def __str__(self):
        return self.title


class BlogComment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    comment_content = models.TextField()
    blog = models.ForeignKey(
           Blog, related_name='comments', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
        