from django.urls import path
from django.urls.conf import include
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

urlpatterns = [
    path('', include(router.urls)),
    path(
        'users/subscriptions/',
        views.ListFollowViewSet.as_view(),
        name='subscriptions'
    ),

    path(
        'users/<int:author_id>/subscribe/',
        views.FollowViewSet.as_view(),
        name='subscribe'
    ),
    path(
        'recipes/download_shopping_cart/',
        views.download_shopping_cart,
        name='download'
    ),
    path(
        'recipes/<int:recipe_id>/shopping_cart/',
        views.ShoppingListViewSet.as_view(),
        name='shopping_cart'
    ),
    path(
        'recipes/<int:recipe_id>/favorite/',
        views.FavoriteViewSet.as_view(),
        name='favorite'
    ),
]
