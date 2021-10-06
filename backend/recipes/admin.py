from django.contrib import admin
from django.db import models
from django.forms import CheckboxSelectMultiple

from recipes.models import Recipe, RecipeIngredient
from recipes.models import (
    Favorite,
    Recipe,
    RecipeIngredient,
    ShoppingCart
)


@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'added_to_favourites')
    fields = ('user', 'recipe')
    readonly_fields = ('user', 'recipe')

    @admin.display(description='добавлено в избранное')
    def added_to_favourites(self, favorite):
        return favorite.created

    def get_readonly_fields(self, request, favorite=None):
        if favorite is not None:
            return ('user', 'recipe')
        return tuple()




class RecipeIngredientInline(admin.StackedInline):
    model = RecipeIngredient
    extra = 1
    min_num = 1


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    inlines = (
        RecipeIngredientInline,
    )
    formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }
    list_display = (
        'name',
        'author',
        'last_update',
        'count_favorites',
    )
    list_filter = (
        'tags',
    )
    fields = (
        'author',
        'name',
        'text',
        'image',
        'cooking_time',
        'tags',
    )

    def get_queryset(self, request):
        return super().get_queryset(
            request,
        ).for_admin_page().with_last_update()

    def get_ordering(self, request):
        return ['-favourites']

    @admin.display(description='последнее обновление')
    def last_update(self, recipe):
        return recipe.last_update

    @admin.display(description='добавлений в избранное')
    def count_favorites(self, recipe):
        return recipe.count_favorites


@admin.register(ShoppingCart)
class ShoppingCartAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'added_to_purchases')
    fields = ('user', 'recipe')
    readonly_fields = ('user', 'recipe')

    @admin.display(description='добавлено в корзину')
    def added_to_purchases(self, purchase):
        return purchase.created

    def get_readonly_fields(self, request, purchase=None):
        if purchase is not None:
            return ('user', 'recipe')
        return tuple()
