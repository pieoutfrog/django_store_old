# Generated by Django 4.2.4 on 2023-08-16 08:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='Дата создания'),
        ),
    ]
