# Generated by Django 4.2.7 on 2023-11-04 06:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('department', models.CharField(max_length=100)),
                ('salary', models.FloatField()),
                ('date_of_joining', models.DateField(default=datetime.datetime(2023, 11, 4, 12, 19, 22, 100349))),
                ('leaves', models.FloatField()),
                ('active', models.BooleanField(default=True)),
            ],
        ),
    ]