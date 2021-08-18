from django.contrib import admin
from import_export.admin import ImportMixin

from recipes import models
from .resources import IngredientResource

@admin.register(models.Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'color', 'slug')


@admin.register(models.Ingredient)
class IngredientAdmin(ImportMixin, admin.ModelAdmin):
    list_display = ('name', 'measurement_unit')
    search_fields = ('name',)
    resource_class = IngredientResource
    from_encoding = "utf-8"


@admin.register(models.Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('author', 'name', 'favorited')
    list_filter = ('author', 'name', 'tags')

    def favorited(self, obj):
        return models.Favorite.objects.filter(recipe=obj).count()
    
    favorited.short_description = 'В избранном'


@admin.register(models.IngredientInRecipe)
class IngredientInRecipeAdmin(admin.ModelAdmin):
    list_display = ('recipe', 'ingredient', 'amount')


@admin.register(models.Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    list_display = ('user', 'recipe', 'date_added')


@admin.register(models.Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    list_display = ('user', 'recipe', 'date_added')








