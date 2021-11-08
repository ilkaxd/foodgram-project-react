from django.core.management.base import BaseCommand

from tags.models import Tag


class Command(BaseCommand):

    help = 'Создаём теги'

    def handle(self, *args, **options):
        for tag_name, color, slug in (
            ('Завтрак', '#4f738e', 'breakfast'),
            ('Обед', '#c87f89', 'lunch'),
            ('Ужин', '#a484ac', 'dinner'),
        ):
            Tag.objects.get_or_create(
                name=tag_name,
                color=color,
                slug=slug
            )
