# Generated by Django 5.1.7 on 2025-03-09 17:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resume_checker', '0002_resume_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resume',
            name='user',
        ),
    ]
