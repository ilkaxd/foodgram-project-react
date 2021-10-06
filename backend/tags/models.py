import matplotlib._color_data as mcd
from django.core.validators import RegexValidator
from django.db import models

from config.extensions.models import DefaultModel

HEX_RE = '^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$'


class Tag(DefaultModel):
    name = models.CharField('название', unique=True, max_length=200)
    color = models.CharField(
        'цвет в HEX',
        unique=True,
        max_length=7,
        validators=[
            RegexValidator(
                regex=HEX_RE,
                message='%(value)s is not a HEX color code.',
            ),
        ],
    )
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = 'тэг'
        verbose_name_plural = 'тэги'
        default_related_name = 'tags'

    @property
    def color_name(self):
        for name, color_hex in mcd.XKCD_COLORS.items():
            if self.color.lower() == color_hex:
                return name.split(':')[1]
        return 'Наименование цвета не найдено в реестре'
