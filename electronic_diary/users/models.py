from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomerUser(AbstractUser):
    GENDERS = (
        ('М', 'Мужчина'),
        ('Ж', 'Женщина'),
    )
    middle_name = models.CharField('Отчество', max_length=130, default='')
    gender = models.CharField('Пол', max_length=1, choices=GENDERS, default='')
    birth_date = models.DateField('Дата рождения', default='1000-01-01')
