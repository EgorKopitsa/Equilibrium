from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomerUser


@admin.register(CustomerUser)
class CustomerUserAdmin(UserAdmin):
    model = CustomerUser
    list_display = ['username', 'email', 'first_name', 'last_name', 'gender']
