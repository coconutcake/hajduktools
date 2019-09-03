from django.contrib import admin
from .models import Door, Discount, Order
admin.site.register(Door)
admin.site.register(Discount)





class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'customer', 'door', 'measures', 'data', 'price_euro', 'status', )
# Register your models here.

admin.site.site_header = 'Dcalc'                    # default: "Django Administration"
admin.site.index_title = 'Dcalc'                 # default: "Site administration"
admin.site.site_title = 'Dcalc'


admin.site.register(Order, OrderAdmin)