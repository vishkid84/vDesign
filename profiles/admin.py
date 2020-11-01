from django.contrib import admin
from .models import UserProfile

# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    fields = (
        'user',
        'default_phone_number',
        'default_city',
        'default_country',
    )

    list_display = (
        'user',
        'default_phone_number',
        'default_city',
        'default_country',
    )

admin.site.register(UserProfile, ProfileAdmin)
