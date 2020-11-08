from django.contrib import admin
from .models import PowerPointProject, PowerPointQuote


# Register your models here.
class PowerPointProjectAdmin(admin.ModelAdmin):
    
    list_display = (
        'client',
        'project_name',
        'project_description',
        'requirements',
    )

admin.site.register(PowerPointProject, PowerPointProjectAdmin)

class PowerPointQuoteAdmin(admin.ModelAdmin):
    
    list_display = (
        'user',
        'project',
    )

admin.site.register(PowerPointQuote, PowerPointQuoteAdmin)
