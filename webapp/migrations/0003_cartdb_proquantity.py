# Generated by Django 4.2 on 2023-06-08 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_cartdb'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartdb',
            name='ProQuantity',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]