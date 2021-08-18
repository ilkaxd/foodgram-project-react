from django.contrib.auth import get_user_model
from django.db.models import fields
from rest_framework import serializers
from djoser.serializers import UserCreateSerializer

from .models import Follow

User = get_user_model()

class CustomUserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = (
            'email',
            'id',
            'username',
            'first_name',
            'last_name'
        )

class UserSerializer(serializers.ModelSerializer):
    is_subscribed = serializers.SerializerMethodField('user_is_subscribed')

    class Meta:
        model = User
        fields = (
            'email',
            'id',
            'username',
            'first_name',
            'last_name',
            'is_subscribed'
        )

    def user_is_subscribed(self, user):
        curr_user = self.context.get('request').user
        if curr_user.is_anonymous:
            return False
        return Follow.objects.filter(user=curr_user, author=user).exists()