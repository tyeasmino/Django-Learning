# Generated by Django 5.1.2 on 2024-11-06 03:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('diagnostic_center', '0002_remove_diagnostic_center_marketing_executive'),
        ('marketing_executive', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Marketing_Executive',
        ),
    ]