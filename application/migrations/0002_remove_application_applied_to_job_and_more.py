# Generated by Django 4.2.5 on 2024-09-18 06:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='application',
            name='applied_to_job',
        ),
        migrations.RemoveField(
            model_name='application',
            name='job_name',
        ),
    ]
