from django.db import models
from datetime import datetime
from products.models import Category

# Create your models here.
class Portfolio(models.Model):
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=250)
    description = models.TextField()
    paragraph = models.TextField(default='paragraph')
    thumb_image_url = models.URLField(max_length=1024, null=True, blank=True)
    thumb_image = models.ImageField(null=True, blank=True)
    image_one_url = models.URLField(max_length=1024, null=True, blank=True)
    image_one = models.ImageField(null=True, blank=True)
    image_two_url = models.URLField(max_length=1024, null=True, blank=True)
    image_two = models.ImageField(null=True, blank=True)
    image_three_url = models.URLField(max_length=1024, null=True, blank=True)
    image_three = models.ImageField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name