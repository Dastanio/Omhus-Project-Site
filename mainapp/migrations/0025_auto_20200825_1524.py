# Generated by Django 3.1 on 2020-08-25 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0024_formtoonec_comments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formtoonec',
            name='comments',
            field=models.TextField(blank=True, default='', verbose_name='Comment'),
        ),
    ]
