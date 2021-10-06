from django.contrib import admin
from import_export.admin import ImportMixin

from ingredients.resources import IngredientResource
from ingredients.models import Ingredient


@admin.register(Ingredient)
class IngredientAdmin(ImportMixin, admin.ModelAdmin):
    list_display = ('name', 'measurement_unit')
    search_fields = ('name',)
    resource_class = IngredientResource
    from_encoding = "utf-8"
