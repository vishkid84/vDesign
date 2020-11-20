from django.contrib import admin
from .models import Portfolio


class PortfolioAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'description',
        'category',
        'thumb_image',
    )

    ordering = ('date',)

admin.site.register(Portfolio, PortfolioAdmin)
