# Generated by Django 2.0.4 on 2018-06-03 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Institute', '0003_examdates'),
    ]

    operations = [
        migrations.AddField(
            model_name='examdates',
            name='date',
            field=models.DateTimeField(null=True, verbose_name='Date'),
        ),
    ]
