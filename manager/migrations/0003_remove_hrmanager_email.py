# Generated by Django 4.2.5 on 2024-06-27 13:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0002_hrmanager_profile_pic_alter_hrmanager_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hrmanager',
            name='email',
        ),
    ]
