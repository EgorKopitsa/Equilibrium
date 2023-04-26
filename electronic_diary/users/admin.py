from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomerUser


@admin.register(CustomerUser)
class CustomerUserAdmin(UserAdmin):
    """
    Админ-панель модели пользователя
    """
    model = CustomerUser
    list_display = ['username', 'email', 'first_name', 'last_name', 'gender']
    fieldsets = [
        (
            None,
            {
                "fields": ['first_name', 'last_name', 'middle_name', 'email', 'avatar', 'birth_date', 'gender'],
            }
        )
    ]
