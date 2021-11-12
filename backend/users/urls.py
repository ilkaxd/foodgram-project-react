from django.urls import include, path

from rest_framework.routers import DefaultRouter
from users.views import UserViewSet

router = DefaultRouter()
router.register('', UserViewSet, basename='user')

urlpatterns = [
    path('users/', include(router.urls)),
    path('auth/', include('djoser.urls.authtoken'))

    # path('', include('djoser.urls')),
]
