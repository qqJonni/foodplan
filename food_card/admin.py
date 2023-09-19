from django.contrib import admin
from food_card import models


class RecipeItemsInline(admin.TabularInline):
    extra = 1
    model = models.RecipeItems


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    fields = ['title', 'calories']
    list_display = ['title', 'calories']
    search_fields = ['title', ]
    search_help_text = 'Поиск по названию'


@admin.register(models.RecipeItems)
class RecipeItemsAdmin(admin.ModelAdmin):
    fields = ['product', 'quantity']
    list_display = ['product', 'quantity']


@admin.register(models.Recipe)
class RecipeAdmin(admin.ModelAdmin):
    fields = ['title', 'recipe_items']
    inline = [RecipeItemsInline]
    search_fields = ['title', ]
    search_help_text = 'Поиск по названию'
