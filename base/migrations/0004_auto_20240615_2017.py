# Generated by Django 3.0.5 on 2024-06-15 20:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_auto_20240613_1129'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate',
            name='applications',
            field=models.ManyToManyField(to='base.Application'),
        ),
        migrations.AddField(
            model_name='candidate',
            name='experiences',
            field=models.ManyToManyField(to='base.Experience'),
        ),
        migrations.AddField(
            model_name='candidate',
            name='skills',
            field=models.ManyToManyField(to='base.Skill'),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='education',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='candidates', to='base.Education'),
        ),
    ]