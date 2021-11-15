from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

from tags.models import Tag

User = get_user_model()

users = (
    ('Иван', 'Иванов', 'ivanov@yandex.ru', 'ivan', '353114ra'),
    ('Ирина', 'Аллегрова', 'allegrova@yandex.ru', 'irina', '353114ra'),
    ('Василий', 'Пупкин', 'vaska@yandex.ru', 'vaska', 'superVaska'),
    ('Турбо', 'Улиточник', 'turbo@yandex.ru', 'turbo', 'megaTurbo'),
    ('Тренер', 'Тренеровочный', 'trener@yandex.ru', 'trener', 'useLess1')
)

class Command(BaseCommand):

    help = 'Создаём пользователей'

    def handle(self, *args, **options):
        for (first_name, last_name, email, username, password) in users:
            User.objects.get_or_create(
                first_name=first_name,
                last_name=last_name,
                email=email,
                username=username,
                password=password
            )
