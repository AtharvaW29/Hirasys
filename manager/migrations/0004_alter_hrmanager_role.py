# Generated by Django 4.2.5 on 2024-09-18 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0003_remove_hrmanager_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hrmanager',
            name='role',
            field=models.CharField(choices=[('HRAdmin', 'HR Admin'), ('HR', 'HR'), ('Employee', 'Employee')], max_length=50),
        ),
    ]