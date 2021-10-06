from django.core.validators import RegexValidator
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import Count, Exists, OuterRef, Q, Value
from django.db.models import F

from config.extensions.models import DefaultUserQuerySet


class UserQuerySet(DefaultUserQuerySet):

    class Q:
        @staticmethod
        def user_following(user):
            return Q(following__user=user)

    def for_detail(self, pk, user):
        return self.for_viewset(user).get(id=pk)

    def for_anon(self):
        return self.annotate(
            is_subscribed=Value(False),
            recipes_count=Value(0),
        )

    def for_viewset(self, user):
        from users.models import Subscribe

        if not user.is_authenticated:
            return self.for_anon()

        return self.annotate(
            is_subscribed=Exists(
                Subscribe.objects.filter(user=user, author=OuterRef('pk')),
            ),
            recipes_count=Count('recipes'),
        )

    def for_subscriptions(self, user):
        qs = self.for_viewset(user)

        if not user.is_authenticated:
            return self.for_anon()

        return qs.filter(self.Q.user_following(user))


class CustomUser(AbstractUser):
    objects = UserQuerySet.as_manager()

    first_name = models.CharField(
        verbose_name='Имя',
        max_length=150,
        blank=False,
        help_text='Введите имя'
    )

    last_name = models.CharField(
        verbose_name='Фамилия',
        max_length=150,
        blank=False,
        help_text='Введите фамилию'
    )

    email = models.EmailField(
        verbose_name='Email',
        max_length=254,
        unique=True,
        blank=False,
        help_text='Укажите email',
        error_messages={
            'unique': (
                'Пользователь с таким логином уже существует'
            )
        }
    )

    username = models.CharField(
        verbose_name='логин',
        max_length=150,
        unique=True,
        blank=False,
        validators=[
            RegexValidator(
                regex=r'^[\w.@+-]',
                message='Недопустимые символы.'
            )
        ],
        help_text='Укажите никнейм'
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [
        'username',
        'first_name',
        'last_name',
    ]

    class Meta:
        ordering = ('username',)
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'

    def get_short_name(self):
        return self.first_name

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def subscribe(self, user):
        from users.services import Subscriber
        return Subscriber(self, user)()

    def unsubscribe(self, user):
        from users.services import Unsubscriber
        return Unsubscriber(self, user)()


class Subscribe(models.Model):
    user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='follower',
        verbose_name='подписчик',
    )
    author = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='following',
        verbose_name='автор',
    )

    class Meta:
        verbose_name = 'подписка'
        verbose_name_plural = 'подписки'
        constraints = (
            models.UniqueConstraint(
                fields=('user', 'author'),
                name='unique_user_author',
            ),
            models.CheckConstraint(
                name='user_not_author',
                check=~models.Q(user=F('author'))
            ),
        )

    def __str__(self):
        return f'"{self.user}" подписан на "{self.author}"'
