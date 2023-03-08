from django.contrib import admin
from django.contrib.auth.models import Group

from qoyliq_proj.settings import DEBUG
from .models import *


class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'user_name', 'tg_id', 'user_lang', 'user_phone', 'created_date']
    list_filter = ['id', 'user_name', 'tg_id', 'user_lang', 'user_phone', 'created_date']
    search_fields = ['id',  'user_name',  'tg_id',  'user_lang',  'user_phone',  'created_date']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'created_date']
    list_filter = ['id', 'name', 'created_date']
    list_editable = ['name']
    search_fields = ['id', 'name', 'created_date']
    fields = ['name', 'created_date']
    readonly_fields = ['created_date']


class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'cat', 'price', 'measure', 'created_date']
    list_filter = ['id', 'name', 'cat', 'price', 'measure', 'created_date']
    list_editable = ['name', 'cat', 'price', 'measure']
    search_fields = ['id', 'name', 'cat', 'price', 'measure', 'created_date']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'pay_type', 'total_price', 'created_date']
    list_filter = ['id', 'user', 'pay_type', 'total_price', 'created_date']
    search_fields = ['id', 'user', 'pay_type', 'total_price', 'created_date']


class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'order', 'product', 'quantity']


class CallsAdmin(admin.ModelAdmin):
    list_display = ['id', 'phone']
    list_editable = ['phone']


class DeliveryPriceAdmin(admin.ModelAdmin):
    list_display = ['id', 'price', 'update_date']
    list_editable = ['price']


admin.site.unregister(Group)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
admin.site.register(DeliveryPrice, DeliveryPriceAdmin)
admin.site.register(Calls, CallsAdmin)

if DEBUG:
    admin.site.register(Cart)

admin.site.site_title = 'Admin panel'
admin.site.site_header = 'Admin panel'
