# Generated by Django 4.2.5 on 2024-09-18 06:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created_jobs', to='manager.hrmanager'),
        ),
        migrations.AlterField(
            model_name='job',
            name='skills_required',
            field=models.JSONField(),
        ),
    ]
