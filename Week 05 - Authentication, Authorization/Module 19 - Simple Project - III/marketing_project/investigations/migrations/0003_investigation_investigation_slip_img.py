# Generated by Django 5.1.2 on 2024-11-09 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('investigations', '0002_investigation_marketing_executive_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='investigation',
            name='investigation_slip_img',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/'),
        ),
    ]
