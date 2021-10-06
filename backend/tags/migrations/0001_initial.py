# Generated by Django 3.2.7 on 2021-09-30 09:10

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True, verbose_name='название')),
                ('color', models.CharField(max_length=7, unique=True, validators=[django.core.validators.RegexValidator(message='%(value)s is not a HEX color code.', regex='^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$')], verbose_name='цвет в HEX')),
                ('slug', models.SlugField(unique=True)),
            ],
            options={
                'verbose_name': 'тэг',
                'verbose_name_plural': 'тэги',
                'default_related_name': 'tags',
            },
        ),
    ]
