# Generated by Django 2.0.3 on 2018-03-19 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('InstituteStaff', '0004_pushnotification'),
    ]

    operations = [
        migrations.AddField(
            model_name='pushnotification',
            name='senderID',
            field=models.CharField(default='null', max_length=10, verbose_name='Sender ID'),
        ),
        migrations.AlterField(
            model_name='personalinformation',
            name='ssn',
            field=models.CharField(default='null', max_length=11, unique=True, verbose_name='SSN'),
        ),
    ]
