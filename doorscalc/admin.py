from django.contrib import admin
from .models import Door, Discount, Order
admin.site.register(Door)
admin.site.register(Discount)


class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'customer', 'door', 'measures', 'data', 'price_euro', 'status', )
# Register your models here.
admin.site.register(Order, OrderAdmin)