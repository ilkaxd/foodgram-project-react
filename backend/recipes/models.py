from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, RegexValidator


User = get_user_model()

class Tag(models.Model):
    name = models.CharField(
        verbose_name='Название',
        max_length=200,
        unique=True,
        blank=False,
        db_index=True,
        help_text='Введите название тега',
    )
    color = models.CharField(
        verbose_name='Цвет в HEX',
        max_length=200,
        null=True,
        help_text='Введите цвет тега в HEX',
    )
    slug = models.SlugField(
        verbose_name='Cлаг',
        max_length=200,
        unique=True,
        validators=[
            RegexValidator(
                regex='^[-a-zA-Z0-9_]+$',
                message='Slug содержит недопустимые символы'
            )
        ]
    )

    class Meta:
        verbose_name = 'тег'
        verbose_name_plural = 'теги'

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    name = models.CharField(
        verbose_name='Название',
        max_length=200,
        help_text='Введите название ингредиента',
    )
    measurement_unit = models.CharField(
        verbose_name='Единица измерения',
        max_length=200,
        help_text='Введите единицу измерения',
    )

    class Meta:
        ordering = ('name', )
        verbose_name = 'ингредиент'
        verbose_name_plural = 'ингредиенты'

    def __str__(self):
        return f'{self.name}, {self.measurement_unit}'


class Recipe(models.Model):
    author = models.ForeignKey(
        User,
        verbose_name='Автор',
        on_delete=models.CASCADE,
        related_name='recipes',
        help_text='Укажите автора рецепта'
    )
    ingredients = models.ManyToManyField(
        Ingredient,
        through='IngredientInRecipe',
        verbose_name='Ингредиенты',
        help_text='Укажите ингредиенты и их количество',
    )
    tags = models.ManyToManyField(
        Tag,
        related_name='recipes',
        verbose_name='Теги',
        help_text='Выберите один или несколько тегов',
    )
    image = models.ImageField(
        verbose_name='Изображение',
        upload_to='recipes/',
        help_text='Выберете изображение'
    )
    name = models.CharField(
        verbose_name='Название',
        max_length=200,
        help_text='Введите название рецепта',
    )
    text = models.TextField(
        verbose_name='Описание',
        help_text='Опишите рецепт',
    )
    cooking_time = models.PositiveIntegerField(
        verbose_name='Время приготовления',
        validators=[MinValueValidator(
            limit_value=1,
            message='Значение не может быть меньше 1'
        )],
        help_text='Укажите время приготовления в минутах',
    )
    pub_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата публикации',
    )

    class Meta:
        ordering = ('-pub_date',)
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'

    def __str__(self):
        return self.name


class IngredientInRecipe(models.Model):
    ingredient = models.ForeignKey(
        Ingredient,
        on_delete=models.CASCADE,
        verbose_name='Ингредиент',
    )
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
    )
    amount = models.PositiveIntegerField(
        verbose_name='Количество ингредиента',
    )

    def __str__(self):
        return f'{self.ingredient}, {self.amount}'

    class Meta:
        verbose_name = 'Рецепт-ингредиент'
        verbose_name_plural = 'Рецепты-ингредиенты'
        unique_together = ('ingredient', 'recipe')
        ordering = ('recipe__name',)


class Favorite(models.Model):
    user = models.ForeignKey(
        User,
        verbose_name='Пользователь',
        on_delete=models.CASCADE,
        related_name='favorite_subscriber',
    )
    recipe = models.ForeignKey(
        Recipe,
        verbose_name='Рецепт',
        on_delete=models.CASCADE,
        related_name='favorite_recipe',
    )
    date_added = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата добавления',
    )

    class Meta:
        verbose_name = 'Избранное'
        verbose_name_plural = 'Избранное'
        ordering = ('recipe__name',)
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'recipe'],
                name='favorite_user_recept_unique'
            )
        ]

    def __str__(self):
        return f'Рецепт {self.recipe} в избранном у {self.user}'


class Purchase(models.Model):
    user = models.ForeignKey(
        User,
        verbose_name='Пользователь',
        on_delete=models.CASCADE,
        related_name='purchase_list',
    )
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='customers',
    )
    date_added = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата добавления',
    )

    class Meta:
        ordering = ('-date_added',)
        verbose_name = 'Покупка'
        verbose_name_plural = 'Покупки'
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'recipe'], name='purchase_user_recipe_unique'
            )
        ]

    @classmethod
    def get_purchase_list(cls, purchase_queryset):
        purchase_list = {}
        for purchase in purchase_queryset:
            ingredients = IngredientInRecipe.objects.filter(
                recipe=purchase.recipe
            ).prefetch_related('ingredient')

            for ingredient in ingredients:
                name = ingredient.ingredient.name
                measurement_unit = ingredient.ingredient.measurement_unit
                amount = ingredient.amount
                if name in purchase_list.keys():
                    purchase_list[name]['amount'] += amount
                else:
                    purchase_list[name] = {
                        'measurement_unit': measurement_unit,
                        'amount': amount
                    }
        return purchase_list

    def __str__(self):
        return f'Рецепт {self.recipe} в списке покупок {self.user}'