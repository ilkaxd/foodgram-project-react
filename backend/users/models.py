# from django.db import models
# from django.contrib.auth.models import AbstractUser

# class CustomUser(AbstractUser):
#     first_name = models.CharField(
#         verbose_name='Имя',
#         max_length=50,
#         blank=False,
#         help_text='Required 50 characters of less'
#     )

#     last_name = models.CharField(
#         verbose_name='Фамилия',
#         max_length=100,
#         blank=False,
#         help_text='Required 10 characters of less'
#     )

#     email = models.EmailField(
#         verbose_name='Email',
#         unique=True,
#         blank=False,
#         help_text='Required email'
#     )

#     class Meta:
#         app_label = 'users'
#         verbose_name = 'Пользователь'
#         verbose_name_plural = 'Пользователи'