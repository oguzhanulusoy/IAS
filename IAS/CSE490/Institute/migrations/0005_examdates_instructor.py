# Generated by Django 2.0.4 on 2018-06-03 20:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Institute', '0004_examdates_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='examdates',
            name='instructor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Institute.AcademicStaff'),
            preserve_default=False,
        ),
    ]
