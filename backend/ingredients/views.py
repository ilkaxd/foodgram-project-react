from django_filters import filterset
import rest_framework
from rest_framework import permissions
from ingredients.serializers import IngredientSerializer
from ingredients.filters import IngredientFilter
from ingredients.models import Ingredient

from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ReadOnlyModelViewSet


class IngredientViewSet(ReadOnlyModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    permission_classes = (AllowAny,)
    filterset_class = IngredientFilter
    pagination_class = None
