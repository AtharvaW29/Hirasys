# Generated by Django 4.2.5 on 2024-09-18 08:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0002_remove_company_logo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='socials',
        ),
    ]
