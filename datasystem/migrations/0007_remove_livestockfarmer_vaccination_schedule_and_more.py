# Generated by Django 5.1.2 on 2025-01-21 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datasystem', '0006_rename_count2_livestockfarmer_age_number_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='livestockfarmer',
            name='vaccination_schedule',
        ),
        migrations.AddField(
            model_name='livestockfarmer',
            name='date_administered',
            field=models.CharField(default=0, max_length=255),
        ),
        migrations.AddField(
            model_name='livestockfarmer',
            name='vaccin_type',
            field=models.CharField(default=0, max_length=255),
        ),
    ]
