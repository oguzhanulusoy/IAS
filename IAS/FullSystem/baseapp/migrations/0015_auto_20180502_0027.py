# Generated by Django 2.0.4 on 2018-05-01 21:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('baseapp', '0014_auto_20180502_0027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personalinformation',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
