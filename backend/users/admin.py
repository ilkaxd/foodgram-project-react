# from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
# from django.contrib.auth.models import Group
# from django.contrib.auth import get_user_model


# User = get_user_model()

# @admin.register(User)
# class CustomUserAdmin(UserAdmin):
#     list_display = (
#         'pk',
#         'email',
#         'username',
#         'first_name', 'last_name',
#         'is_staff',
#     )
#     search_fields = ('username', 'email', 'first_name', 'last_name')
#     list_filter = ('email', 'username')
#     readonly_fields = ('date_joined', 'last_login')

#     fieldsets = (
#         (None, {'fields': ('username', 'password')}),
#         ('Personal info', {'fields': ('email', 'first_name', 'last_name')}),
#         ('Permissions', {
#             'fields': ('is_active', 'is_staff', 'is_superuser', 'groups')
#         }),
#         ('Important dates', {'fields': ('last_login', 'date_joined')})
#     )

#     add_fieldsets = (
#         (None, {
#             'classes': ('wide',),
#             'fields': (
#                 'email',
#                 'username',
#                 'first_name', 'last_name',
#                 'password1', 'password2'
#             ),
#         }),
#     )
#     search_fields = ('username',)
#     ordering = ('username',)

#     def get_form(self, request, obj=None, **kwargs):
#         form = super().get_form(request, obj=obj, **kwargs)
#         is_superuser = request.user.is_superuser
#         disabled_fields = set()
#         if not is_superuser:
#             disabled_fields.add([
#                 'username',
#                 'is_superuser',
#                 'user_permissions',
#             ])
#             if (
#                 obj is not None
#                 and
#                 obj == request.user
#             ):
#                 disabled_fields.add([
#                     'is_active',
#                     'is_staff',
#                     'is_superuser',
#                     'groups',
#                     'user_permissions',
#                 ])
#         for field in disabled_fields:
#             if field in form.base_fields:
#                 form.base_fields[field].disabled = True
#         return form