# Generated by Django 3.1 on 2024-06-26 15:14

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('candidate_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone', models.CharField(blank=True, max_length=17, validators=[django.core.validators.RegexValidator(message='Invalid Phone Number', regex='^\\+?1?\\d{9,10}$')])),
                ('education', models.JSONField(max_length=255)),
                ('experiences', models.JSONField(blank=True, max_length=300, null=True)),
                ('skills', models.JSONField(blank=True, max_length=300, null=True)),
            ],
        ),
    ]