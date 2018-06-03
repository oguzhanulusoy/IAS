# Generated by Django 2.0.4 on 2018-05-01 21:27

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('baseapp', '0013_auto_20180421_2300'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='personal_information',
        ),
        migrations.AddField(
            model_name='personalinformation',
            name='user',
            field=models.OneToOneField(default=22, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='personalinformation',
            name='gender',
            field=models.CharField(blank=True, choices=[('F', 'Female'), ('M', 'Male')], max_length=10, verbose_name='Gender'),
        ),
        migrations.AlterField(
            model_name='section',
            name='quota',
            field=models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='Quota'),
        ),
        migrations.AlterField(
            model_name='section',
            name='semester',
            field=models.CharField(choices=[('Summer', 'Summer'), ('Fall', 'Fall'), ('Spring', 'Spring')], max_length=10, verbose_name='Semester'),
        ),
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='media/avatars/'),
        ),
        migrations.AlterUniqueTogether(
            name='completedcourse',
            unique_together={('student', 'ccr_course', 'act_course')},
        ),
    ]
