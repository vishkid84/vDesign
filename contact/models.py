from django.db import models


class Contact(models.Model):
    full_name = models.CharField(max_length=200, null=False, blank=False)
    email = models.CharField(max_length=200, null=False, blank=False)
    message = models.TextField()

    def __str__(self):
        return self.full_name
