# Generated by Django 4.1.7 on 2023-04-18 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_customeruser_birth_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customeruser',
            name='birth_date',
            field=models.DateField(default='1000-01-01', verbose_name='Дата рождения'),
        ),
    ]
