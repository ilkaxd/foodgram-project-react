from django.contrib.auth.models import UserManager as _UserManager
from django.db import models
from django.db.models import F
from django.db.models.functions import Coalesce


class DefaultQuerySet(models.QuerySet):
    Q = None

    @classmethod
    def as_manager(cls):
        return DefaultManager.from_queryset(cls)()

    as_manager.queryset_only = True

    def __getattr__(self, name):
        if self.Q is not None and hasattr(self.Q, name):
            return lambda *args: self.filter(getattr(self.Q, name)())

        raise AttributeError()

    def with_last_update(self):
        return self.annotate(last_update=Coalesce(F('modified'), F('created')))

class DefaultManager(models.Manager):
    def __getattr__(self, name):
        if hasattr(self._queryset_class, 'Q') and hasattr(
            self._queryset_class.Q, name,
        ):
            return getattr(self.get_queryset(), name)

        raise AttributeError(
            f'Nor {self.__class__}, nor {self._queryset_class.__name__} or '
            f'{self._queryset_class.__name__}.Q '
            'does not have `{name}` defined.',
        )



class DefaultModel(models.Model):
    objects = DefaultManager()

    class Meta:
        abstract = True

    def __str__(self):
        if hasattr(self, 'name'):
            return str(self.name)

        return super().__str__()


class TimestampedModel(DefaultModel):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class UserManager(_UserManager):
    use_in_migrations = False


class DefaultUserQuerySet(DefaultQuerySet):
    @classmethod
    def as_manager(cls):
        return UserManager.from_queryset(cls)()
