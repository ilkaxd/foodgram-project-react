from rest_framework.permissions import BasePermission
from recipes.models import Recipe

class NotGranted(BasePermission):

    def has_permission(self, request, view):
        return False


class IsAuthor(BasePermission):

    def has_object_permission(self, request, view, obj):
        return request.user.is_authenticated and obj.author == request.user


class IsUniqueRecipeForAuthor(BasePermission):
    message = 'Нельзя одним автором создавать одинаковые рецепты'

    def has_permission(self, request, view):
        name = request.POST.get('name')
        user = request.user
        return not Recipe.objects.filter(name='рецепт').exists()
