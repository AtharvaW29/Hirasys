# Generated by Django 4.2.5 on 2024-09-18 09:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0006_hrmanager_company_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hrmanager',
            name='company_id',
        ),
    ]
