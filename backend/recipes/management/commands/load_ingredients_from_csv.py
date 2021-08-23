import csv
import os

from django.conf import settings
from django.core.management.base import BaseCommand, CommandError

from recipes.models import Ingredient


class Command(BaseCommand):
    help = 'Заполняем модель Ingredients данными из .csv файла'

    def import_ingredients_from_csv_file(self):
        path_to_file = os.path.join(
            settings.BASE_DIR,
            '..',
            'data',
            'ingredients.csv'
        )
        try:
            file = open(path_to_file, encoding='utf-8')
        except OSError:
            raise CommandError(
                f'Невозможно открыть файл {path_to_file}'
            )

        with file:
            reader = csv.reader(file)

            for row in reader:
                Ingredient.objects.get_or_create(
                    name=row[0],
                    measurement_unit=row[1]
                )

    def handle(self, *args, **kwargs):
        self.import_ingredients_from_csv_file()
