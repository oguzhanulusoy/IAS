# Generated by Django 2.0.3 on 2018-03-22 08:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Institute', '0017_auto_20180322_0759'),
    ]

    operations = [
        migrations.AddField(
            model_name='ccr',
            name='program',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='GrandStudent.program+', to='Institute.GrandStudent'),
        ),
        migrations.AddField(
            model_name='ccr',
            name='studentID',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='GrandStudent.studentID+', to='Institute.GrandStudent'),
        ),
        migrations.AddField(
            model_name='ccr',
            name='takenCourses',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='CCR.takenCourses+', to='Institute.TakenCourse'),
        ),
    ]
