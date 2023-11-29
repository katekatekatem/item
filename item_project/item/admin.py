from django.contrib import admin

from .models import Item


@admin.register(Item)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'price']
    search_fields = ('name', 'price')
    empty_value_display = '-пусто-'
