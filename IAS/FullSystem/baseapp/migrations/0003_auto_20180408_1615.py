# Generated by Django 2.0.3 on 2018-04-08 13:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('baseapp', '0002_auto_20180408_1613'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='program',
            unique_together={('code', 'type', 'thesis')},
        ),
    ]
