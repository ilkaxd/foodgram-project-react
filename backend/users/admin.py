from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from rest_framework.authtoken.models import TokenProxy

from users.models import Subscribe

User = get_user_model()

admin.site.unregister(TokenProxy)
admin.site.unregister(Group)


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = (
        'pk',
        'email',
        'username',
        'first_name', 'last_name',
        'is_superuser',
    )
    search_fields = ('username', 'email', 'first_name', 'last_name')
    list_filter = ('email', 'username')
    readonly_fields = ('date_joined', 'last_login')

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (
            'Персональные данные',
            {'fields': ('email', 'first_name', 'last_name')}
        ),
        (
            'Права',
            {
                'fields': (
                    'is_active',
                    'is_staff',
                    'is_superuser',
                    'groups',
                    'user_permissions'
                )
            }
        ),
        (
            'Ключевые даты',
            {'fields': ('last_login', 'date_joined')}
        )
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email',
                'username',
                'first_name', 'last_name',
                'password1', 'password2'
            ),
        }),
    )
    search_fields = ('username',)
    ordering = ('id',)
    empty_value_display = '-'


@admin.register(Subscribe)
class SubscribeAdmin(admin.ModelAdmin):
    list_display = ('__str__',)
    fields = ('user', 'author')
    readonly_fields = ('user', 'author')

    def get_readonly_fields(self, request, subscribe=None):
        if subscribe is not None:
            return ('user', 'author')
        return tuple()
