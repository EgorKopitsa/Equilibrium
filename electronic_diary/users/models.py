from django.contrib.auth.models import AbstractUser
from django.core.validators import FileExtensionValidator
from django.db import models
from django.urls import reverse


class CustomerUser(AbstractUser):
    """
    Модель переопределенного пользователя
    """
    GENDERS = (
        ('М', 'Мужчина'),
        ('Ж', 'Женщина'),
    )
    avatar = models.ImageField(
        verbose_name='Аватар',
        upload_to='images/avatars/%Y/%m/%d/',
        default='images/avatars/default.png',
        blank=True,
        validators=[FileExtensionValidator(allowed_extensions=('png', 'jpg', 'jpeg'))])
    middle_name = models.CharField('Отчество', max_length=130)
    gender = models.CharField('Пол', choices=GENDERS, max_length=7)
    birth_date = models.DateField('Дата рождения')

    def get_absolute_url(self):
        """
        Ссылка на профиль
        """
        return reverse('profile_detail', kwargs={'slug': self.pk})
