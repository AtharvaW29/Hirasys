# Generated by Django 3.1 on 2024-06-21 18:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='candidate',
            name='application',
        ),
    ]