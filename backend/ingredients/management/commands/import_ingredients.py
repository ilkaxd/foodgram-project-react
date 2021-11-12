import os
import json

from django.core.management.base import BaseCommand

from ingredients.models import Ingredient


class Command(BaseCommand):

    help = 'Импортируем ингредиенты'

    def handle(self, *args, **options):
        path_to_json = os.path.join('data', 'ingredients.json')
        print('!!!!!!!!!!', os.getcwd(), path_to_json)
        with open(path_to_json, 'r', encoding='utf-8') as read_file:
            ingredients = json.load(read_file)
            data = []
            for ingredient in ingredients:
                data.append(
                    Ingredient(
                        name=ingredient['name'],
                        measurement_unit=ingredient['measurement_unit']
                    )
                )
            Ingredient.objects.bulk_create(
                data,
                ignore_conflicts=True
            )
