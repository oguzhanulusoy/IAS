# Generated by Django 2.0.3 on 2018-03-22 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Institute', '0010_auto_20180322_0705'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classes',
            name='className',
            field=models.CharField(choices=[('1', '234'), ('2', '500')], max_length=6, null=True, verbose_name='Class Name'),
        ),
    ]
