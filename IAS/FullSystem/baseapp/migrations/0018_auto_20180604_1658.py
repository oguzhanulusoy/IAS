# Generated by Django 2.0.4 on 2018-06-04 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baseapp', '0017_auto_20180604_1208'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='st_id',
            field=models.CharField(blank=True, max_length=9, null=True, verbose_name='Student ID'),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='slot',
            field=models.CharField(choices=[('1', '9-10'), ('2', '10-11'), ('3', '11-12'), ('4', '12-13'), ('5', '13-14'), ('6', '14-15'), ('7', '15-16'), ('8', '16-17'), ('9', '17-18'), ('10', '18-19'), ('11', '19-20'), ('12', '20-21'), ('13', '21-22')], max_length=2, verbose_name='Section Slot'),
        ),
    ]