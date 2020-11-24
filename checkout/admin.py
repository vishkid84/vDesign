from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)

    readonly_fields = ('order_number', 'date',
                       'total', 'original_bag',
                       'stripe_pid',)

    fields = ('order_number', 'user_profile', 'date', 'name',
              'email', 'phone_number', 'country',
              'postcode', 'city', 'street_address1',
              'street_address2', 'county_or_state',
              'total',)

    list_display = ('order_number', 'date',
                    'name', 'total')

    ordering = ('-date',)

admin.site.register(Order, OrderAdmin)
