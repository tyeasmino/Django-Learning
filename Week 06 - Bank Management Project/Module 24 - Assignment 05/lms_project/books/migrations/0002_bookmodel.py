# Generated by Django 5.1.2 on 2024-11-29 15:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=500)),
                ('quantity', models.IntegerField()),
                ('price', models.IntegerField()),
                ('book_img', models.ImageField(upload_to='car/media/uploads/')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.bookcategorymodel')),
            ],
        ),
    ]