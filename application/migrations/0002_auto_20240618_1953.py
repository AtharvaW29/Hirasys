# Generated by Django 3.1 on 2024-06-18 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='application',
            name='id',
        ),
        migrations.AddField(
            model_name='application',
            name='application_id',
            field=models.AutoField(default=True, primary_key=True, serialize=False),
        ),
    ]
