# Generated by Django 4.2 on 2023-06-14 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_cartdb_proquantity'),
    ]

    operations = [
        migrations.CreateModel(
            name='CheckoutDb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CheckName', models.CharField(blank=True, max_length=50, null=True)),
                ('Checkemail', models.EmailField(blank=True, max_length=60, null=True)),
                ('CheckAddress', models.CharField(blank=True, max_length=100, null=True)),
                ('CheckPhone', models.IntegerField(blank=True, null=True)),
                ('CheckSubject', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
