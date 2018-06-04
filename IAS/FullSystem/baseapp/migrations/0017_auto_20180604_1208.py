# Generated by Django 2.0.4 on 2018-06-04 09:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('baseapp', '0016_auto_20180502_0028'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExamDate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(max_length=6, null=True, verbose_name='Place')),
                ('date', models.DateField(null=True, verbose_name='Date')),
                ('slot', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3')], max_length=2, null=True, verbose_name='Slot')),
                ('instructor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='baseapp.AcademicStaff')),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='baseapp.Section')),
            ],
            options={
                'verbose_name': 'Exam Date',
                'verbose_name_plural': 'Exam Dates',
            },
        ),
        migrations.CreateModel(
            name='MakeAnnouncement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, null=True, verbose_name='Title')),
                ('description', models.TextField(max_length=500, null=True, verbose_name='Description')),
                ('date', models.DateField(auto_now_add=True)),
                ('sender', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='baseapp.Staff')),
            ],
            options={
                'verbose_name': 'Announcement',
                'verbose_name_plural': 'Announcements',
            },
        ),
        migrations.AlterField(
            model_name='schedule',
            name='slot',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3')], max_length=2, verbose_name='Section Slot'),
        ),
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(blank=True, default='avatars/ppic.png', null=True, upload_to='media/avatars/'),
        ),
    ]