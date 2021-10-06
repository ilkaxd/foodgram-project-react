from django.contrib.auth import get_user_model
from django.db import models

from config.extensions.models import TimestampedModel
from recipes.models import Recipe

User = get_user_model()


class ShoppingCart(TimestampedModel):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='пользователь',
    )
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        verbose_name='рецепт',
    )

    class Meta:
        verbose_name = 'покупка'
        verbose_name_plural = 'покупки'
        default_related_name = 'purchases'
        constraints = (
            models.UniqueConstraint(
                fields=('user', 'recipe'),
                name='unique_purchase_user_recipe',
            ),
        )

    def __str__(self):
        return f'{self.user} / {self.recipe}'
