from django.core.validators import MinValueValidator
from django.utils.translation import gettext_lazy as _


class GteMinValueValidator(MinValueValidator):
    message = _('Убедитесь, что значение больше чем  %(limit_value)s.')
    code = 'min_value'

    def compare(self, a, b):
        return a <= b
