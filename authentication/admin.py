from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


class UserAdminCustom(UserAdmin):
    date_hierarchy = 'date_joined'
    list_display = ('username', 'email', 'nickname', 'first_name', 'last_name',
                    'date_joined')


admin.site.register(User, UserAdminCustom)
