# Generated by Django 5.1.2 on 2024-11-15 22:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0005_alter_commentmodel_car'),
    ]

    operations = [
        migrations.RenameField(
            model_name='carmodel',
            old_name='descriptoin',
            new_name='description',
        ),
    ]