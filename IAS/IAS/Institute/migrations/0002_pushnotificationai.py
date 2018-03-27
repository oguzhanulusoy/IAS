# Generated by Django 2.0.3 on 2018-03-21 18:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Institute', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PushNotificationAI',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=140, null=True, verbose_name='Subject')),
                ('text', models.TextField(max_length=500, null=True, verbose_name='Text')),
                ('grandStudents', models.ManyToManyField(null=True, related_name='receiver', to='Institute.GrandStudent')),
                ('instructor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sender', to='Institute.Instructor')),
            ],
            options={
                'verbose_name_plural': 'Push Notifications from Academic Instructors',
            },
        ),
    ]
