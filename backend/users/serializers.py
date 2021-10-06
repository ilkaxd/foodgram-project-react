from django.contrib.auth import get_user_model
from djoser.serializers import \
    UserCreateSerializer as DjoserUserCreateSerializer
from djoser.serializers import UserSerializer
from djoser.serializers import UserSerializer as DjoserUserSerializer
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from config.extensions.serializers import ModelSerializer
from users.models import Subscribe

User = get_user_model()


class CustomUserSerializer(DjoserUserSerializer):
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
        return Subscribe.objects.filter(user=curr_user, author=user).exists()

    def to_representation(self, user):
        request = self.context['request']

        qs = self.Meta.model.objects.for_detail(user.pk, request.user)

        return super().to_representation(qs)


class CustomUserCreateSerializer(DjoserUserCreateSerializer):
    class Meta:
        model = User
        fields = (
            'email',
            'id',
            'username',
            'first_name',
            'last_name',
            'password',
        )


class SubscriptionSerializer(CustomUserSerializer):
    recipes = serializers.SerializerMethodField()
    recipes_count = serializers.IntegerField(read_only=True)

    class Meta(CustomUserSerializer.Meta):
        fields = UserSerializer.Meta.fields + ('recipes', 'recipes_count')

    def get_recipes(self, author):
        from recipes.serializers import RecipeSubscriptionSerializer

        limit = self.context['request'].query_params.get('recipes_limit')

        qs = (
            author.recipes.all()[:int(limit)]
            if limit is not None
            else author.recipes.all()
        )

        return RecipeSubscriptionSerializer(qs, many=True).data


class SubscribeSerializer(ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Subscribe
        fields = ('user', 'author')
        validators = (
            UniqueTogetherValidator(
                queryset=Subscribe.objects.all(),
                fields=('user', 'author'),
                message='Подписка уже оформлена',
            ),
        )

    def validate(self, data):
        if data['user'] == data['author']:
            raise serializers.ValidationError(
                'Нельзя подписаться на себя'
            )
        return data

    def create(self, data):
        user, author = data.values()
        return user.subscribe(author)

    def to_representation(self, subscription):
        from users.serializers import SubscriptionSerializer

        qs = User.objects.for_detail(subscription.author.id, subscription.user)
        return SubscriptionSerializer(qs, context=self.context).data


class UnsubscribeSerializer(ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Subscribe
        fields = ('user', 'author')

    def validate(self, data):
        if not Subscribe.objects.filter(**data).exists():
            raise serializers.ValidationError(
                'Указанной подписки не существует'
            )
        return data
