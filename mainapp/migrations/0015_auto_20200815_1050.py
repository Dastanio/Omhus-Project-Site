# Generated by Django 3.0.8 on 2020-08-15 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0014_auto_20200807_1721'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formtoonec',
            name='kol2',
            field=models.IntegerField(default='', max_length=8),
        ),
        migrations.AlterField(
            model_name='formtoonec',
            name='time2',
            field=models.IntegerField(default='', max_length=8),
        ),
    ]
