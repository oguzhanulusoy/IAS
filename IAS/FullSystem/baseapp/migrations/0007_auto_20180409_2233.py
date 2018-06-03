# Generated by Django 2.0.3 on 2018-04-09 19:33

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baseapp', '0006_auto_20180409_2225'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='curriculum',
        ),
        migrations.AlterField(
            model_name='curriculum',
            name='year',
            field=models.PositiveIntegerField(default=2018, validators=[django.core.validators.MinValueValidator(2000), django.core.validators.MaxValueValidator(2019)], verbose_name='Year'),
        ),
    ]