# Generated by Django 2.0.4 on 2018-06-03 20:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Institute', '0008_auto_20180603_2013'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ExamDates',
            new_name='ExamDate',
        ),
    ]