from rest_framework.permissions import BasePermission


class NotGranted(BasePermission):

    def has_permission(self, request, view):
        return False


class IsAuthor(BasePermission):

    def has_object_permission(self, request, view, obj):
        return request.user.is_authenticated and obj.author == request.user


class IsUniqueRecipeForAuthor(BasePermission):
    message = 'Нельзя создавать одинаковые рецепты'

    def has_object_permission(self, request, view, obj):
        return obj.recipe != request.recipe
