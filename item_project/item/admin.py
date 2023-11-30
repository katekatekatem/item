from django.contrib import admin

from .models import Item, ItemOrder, Order


class ItemOrderInline(admin.TabularInline):
    model = ItemOrder
    min_num = 1
    extra = 1


@admin.register(Item)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'price', 'currency']
    search_fields = ('name', 'price')
    empty_value_display = '-пусто-'


@admin.register(Order)
class TagAdmin(admin.ModelAdmin):
    list_display = ['id']
    search_fields = ('items',)
    empty_value_display = '-пусто-'


@admin.register(ItemOrder)
class RecipeTagAdmin(admin.ModelAdmin):
    list_display = ['item', 'order']
    list_filter = ('order',)
    empty_value_display = '-пусто-'
