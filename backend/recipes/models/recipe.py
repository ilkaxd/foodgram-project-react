from django.db import models
from django.db.models import Count, Exists, OuterRef, Q, Value
from django.contrib.auth import get_user_model

from config.extensions.models import DefaultQuerySet, TimestampedModel
from recipes.models import Favorite

from tags.models import Tag

User = get_user_model()


class RecipeQuerySet(DefaultQuerySet):

    class Q:
        @classmethod
        def favourites(cls, user):
            return Q(favourites__user=user)

        @classmethod
        def purchases(cls, user):
            return Q(purchases__user=user)

    def favourites(self, user):
        if not user.is_authenticated:
            return self.for_anon()

        return self.filter(self.Q.favourites(user))

    def purchases(self, user):
        if not user.is_authenticated:
            return self.for_anon()

        return self.filter(self.Q.purchases(user))

    def for_detail(self, pk, user):
        return self.for_viewset(user).get(id=pk)

    def for_anon(self):
        return self.annotate(
            is_favorited=Value(False),
            is_in_shopping_cart=Value(False),
        )

    def for_viewset(self, user):
        from recipes.models import ShoppingCart

        if not user.is_authenticated:
            return self.for_anon()

        return self.annotate(
            is_favorited=Exists(
                Favorite.objects.filter(recipe=OuterRef('pk'), user=user),
            ),
            is_in_shopping_cart=Exists(
                ShoppingCart.objects.filter(recipe=OuterRef('pk'), user=user),
            ),
        )

    def for_admin_page(self):
        return self.annotate(count_favorites=Count('favourites__recipe'))

    def create_with_ingredients_and_tags(self, **data):
        from recipes.services import RecipeCreator
        return RecipeCreator(**data)()


class Recipe(TimestampedModel):
    objects = RecipeQuerySet.as_manager()

    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='автор',
    )
    name = models.CharField('название', max_length=256)
    text = models.TextField('описание рецепта')
    image = models.ImageField('изображение', upload_to='recipes/images/')
    cooking_time = models.PositiveSmallIntegerField('время приготовления')
    ingredients = models.ManyToManyField(
        'ingredients.Ingredient',
        through='recipes.RecipeIngredient',
        blank=True,
        verbose_name='ингредиенты',
    )
    tags = models.ManyToManyField(Tag, blank=True, verbose_name='тэги')

    class Meta:
        verbose_name = 'рецепт'
        verbose_name_plural = 'рецепты'
        default_related_name = 'recipes'
        # constraints = (
        #     models.UniqueConstraint(
        #         fields=('author', 'name'),
        #         name='unique_author_recipename',
        #     ),
        # )
        ordering = ('-created', '-modified')

    def update(self, **data):
        from recipes.services import RecipeUpdater
        return RecipeUpdater(self, **data)()
