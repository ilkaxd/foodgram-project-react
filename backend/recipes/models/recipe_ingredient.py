from django.core.validators import MaxValueValidator
from django.db import models

from config.extensions.models import DefaultModel
from config.extensions.validators import GteMinValueValidator
from ingredients.models import Ingredient
from recipes.models import Recipe


class RecipeIngredient(DefaultModel):
    ingredient = models.ForeignKey(
        Ingredient,
        on_delete=models.CASCADE,
        verbose_name='ингредиент',
    )
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        verbose_name='рецепт',
    )
    amount = models.DecimalField(
        'количество',
        decimal_places=1,
        max_digits=5,
        validators=[
            GteMinValueValidator(
                0,
                'Введите число больше нуля или удалите ингредиент.',
            ),
            MaxValueValidator(5000, 'Как-то многовато'),
        ],
    )

    class Meta:
        verbose_name = 'ингредиент'
        verbose_name_plural = 'ингредиенты'
        default_related_name = 'recipeingredients'
        constraints = (
            models.CheckConstraint(
                name='amount_gt_0',
                check=models.Q(amount__gt=0),
            ),
            models.CheckConstraint(
                name='amount_lt_5000',
                check=models.Q(amount__lt=5000),
            ),
            models.UniqueConstraint(
                fields=('recipe', 'ingredient'),
                name='unique_recipe_ingredient',
            ),
        )

    def __str__(self):
        return f'{self.amount} / {self.ingredient}'
