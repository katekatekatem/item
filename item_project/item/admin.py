from django.contrib import admin

from .models import Coupon, Item, ItemOrder, Order, Tax


class ItemOrderInline(admin.TabularInline):
    model = ItemOrder
    min_num = 1
    extra = 1


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'price', 'currency']
    search_fields = ('name', 'price')
    empty_value_display = '-пусто-'


@admin.register(Coupon)
class CouponAdmin(admin.ModelAdmin):
    list_display = ['amount_off', 'duration', 'currency', 'duration_in_months']
    list_filter = ('amount_off',)
    empty_value_display = '-пусто-'


@admin.register(Tax)
class TaxAdmin(admin.ModelAdmin):
    list_display = ['id', 'percentage', 'display_name', 'inclusive']
    list_filter = ('percentage',)
    empty_value_display = '-пусто-'


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id']
    search_fields = ('items',)
    empty_value_display = '-пусто-'


@admin.register(ItemOrder)
class ItemOrderAdmin(admin.ModelAdmin):
    list_display = ['item', 'order']
    list_filter = ('order',)
    empty_value_display = '-пусто-'
