from django.contrib import admin

from order.models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('boat', 'email', )
    list_filter = ('boat',)
