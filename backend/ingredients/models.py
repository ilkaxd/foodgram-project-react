from django.db import models

from config.extensions.models import DefaultModel


class Ingredient(DefaultModel):
    name = models.CharField(
        'наименование',
        max_length=200,
    )
    measurement_unit = models.CharField(
        'единица изменения',
        max_length=200,
    )

    class Meta:
        verbose_name = 'ингредиент'
        verbose_name_plural = 'ингредиенты'
        constraints = (
            models.UniqueConstraint(
                fields=('name', 'measurement_unit'),
                name='unique_ingredient_unit'
            ),
        )

    def __str__(self):
        return f'{self.name}, {self.measurement_unit}'
