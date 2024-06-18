# Generated by Django 3.1 on 2024-06-18 14:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('candidate_id', models.CharField(max_length=20)),
                ('applied_to_job', models.CharField(max_length=300)),
                ('status', models.CharField(choices=[('Applied', 'Applied'), ('In Progress', 'In Progress'), ('Shortlisted', 'Shortlisted'), ('Rejected', 'Rejected'), ('Offered', 'Offered')], default='Applied', max_length=20)),
                ('scores', models.JSONField(blank=True, default=dict)),
                ('cover_letter', models.CharField(max_length=500)),
                ('interview_feedback', models.CharField(max_length=200)),
                ('application_date', models.DateTimeField(auto_now_add=True)),
                ('job_name', models.CharField(max_length=300)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-application_date',),
            },
        ),
    ]