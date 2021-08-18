from django.shortcuts import render
from rest_framework import filters, permissions, serializers, status, viewsets
from django.contrib.auth import get_user_model
from rest_framework.decorators import action, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.filters import SearchFilter

from .permissions import IsOwnerOrAdminOrReadOnly
from .paginators import CustomPagination
from .serializers import (
    FollowSerializer,
    IngredientSerializer,
    RecipeSerializer,
    TagSerializer,
)
from .models import (
    Ingredient,
    Recipe,
    Tag
)
from users.serializers import UserSerializer
from users.models import Follow


User = get_user_model()

class TagsViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny,]
    serializer_class = TagSerializer
    queryset = Tag.objects.all()
    pagination_class = None


class RecipesViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = Recipe


class IngredientsViewSet(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    permission_classes = (AllowAny,)
    filter_backends = (SearchFilter,)
    search_fields = ('^name',)
    pagination_class = None


class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

    def get_serializer_class(self):
        if self.action in ('create', 'update'):
            return RecipeCreateSerializer
        return self.serializer_class

    def get_permissions(self):
        return get_method_permiss