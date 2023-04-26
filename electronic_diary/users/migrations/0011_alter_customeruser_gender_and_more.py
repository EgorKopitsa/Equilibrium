# Generated by Django 4.1.7 on 2023-04-26 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_alter_customeruser_birth_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customeruser',
            name='gender',
            field=models.CharField(blank=True, choices=[('М', 'Мужчина'), ('Ж', 'Женщина')], default='', max_length=7, verbose_name='Пол'),
        ),
        migrations.AlterField(
            model_name='customeruser',
            name='middle_name',
            field=models.CharField(blank=True, default='', max_length=130, verbose_name='Отчество'),
        ),
    ]