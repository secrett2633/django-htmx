# Generated by Django 5.1.7 on 2025-03-09 14:30

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("user", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="serviceuser",
            name="provider",
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
