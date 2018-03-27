# Generated by Django 2.0.3 on 2018-03-21 18:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Institute', '0002_pushnotificationai'),
    ]

    operations = [
        migrations.CreateModel(
            name='PushNotificationAItoStudents',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=140, null=True, verbose_name='Subject')),
                ('text', models.TextField(max_length=500, null=True, verbose_name='Text')),
                ('grandStudents', models.ManyToManyField(null=True, related_name='receiverFromInstructors', to='Institute.GrandStudent')),
                ('instructor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sender2students', to='Institute.Instructor')),
            ],
            options={
                'verbose_name_plural': 'Push Notifications from Academic Instructors to Students',
            },
        ),
        migrations.CreateModel(
            name='PushNotificationIStoInstructors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=140, null=True, verbose_name='Subject')),
                ('text', models.TextField(max_length=500, null=True, verbose_name='Text')),
                ('institute', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sender2instructors', to='Institute.InstituteStaff')),
                ('instructors', models.ManyToManyField(null=True, related_name='receiverFromInstitute', to='Institute.Instructor')),
            ],
            options={
                'verbose_name_plural': 'Push Notifications from Institute to Instructors',
            },
        ),
        migrations.CreateModel(
            name='PushNotificationIStoStudents',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=140, null=True, verbose_name='Subject')),
                ('text', models.TextField(max_length=500, null=True, verbose_name='Text')),
                ('grandStudents', models.ManyToManyField(null=True, related_name='receiverFromInstitute2', to='Institute.GrandStudent')),
                ('institute', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sender2tostudents2', to='Institute.InstituteStaff')),
            ],
            options={
                'verbose_name_plural': 'Push Notifications from Institute to Instructors',
            },
        ),
        migrations.RemoveField(
            model_name='pushnotificationai',
            name='grandStudents',
        ),
        migrations.RemoveField(
            model_name='pushnotificationai',
            name='instructor',
        ),
        migrations.DeleteModel(
            name='PushNotificationAI',
        ),
    ]
