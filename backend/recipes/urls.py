from django.urls import path
from django.urls.conf import include
from rest_framework import routers
from rest_framework.routers import DefaultRouter

from recipes import views

router = DefaultRouter()
router.register(
    'tags',
    views.TagsViewSet,
    basename='tags'
)
router.register(
    'recipes',
    views.RecipesViewSet,
    basename='recipes'
)
router.register(
    'ingredients',
    views.IngredientsViewSet,
    basename='ingredients'
)
# router.register('users', views.SubscriptionViewSet, basename='users')

urlpatterns = [path('', include(router.urls))]

