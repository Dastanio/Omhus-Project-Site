# Generated by Django 3.0.8 on 2020-07-23 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useronec',
            name='passwordforonec',
            field=models.CharField(max_length=64, verbose_name='Пароль пользователя 1С'),
        ),
        migrations.AlterField(
            model_name='useronec',
            name='userid',
            field=models.CharField(max_length=64, verbose_name='Id пользователя'),
        ),
        migrations.AlterField(
            model_name='useronec',
            name='usernameforonec',
            field=models.CharField(max_length=64, verbose_name='Имя пользователя 1С'),
        ),
        migrations.AlterField(
            model_name='useronec',
            name='wayforbd',
            field=models.CharField(max_length=64, verbose_name='Путь к базе данных'),
        ),
    ]
