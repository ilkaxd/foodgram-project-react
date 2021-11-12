from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

from tags.models import Tag

User = get_user_model()

class Command(BaseCommand):

    help = 'Создаём админа'

    def handle(self, *args, **options):
        if User.objects.count() == 0:
            User.objects.create_superuser(
                email='admin@yandex.ru',
                username='admin',
                password='admin'
            )
        else:
            print('Админа можно создать только если нет других пользователей')
