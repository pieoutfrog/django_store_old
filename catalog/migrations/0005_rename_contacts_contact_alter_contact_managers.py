# Generated by Django 4.2.4 on 2023-08-18 08:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_contacts'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Contacts',
            new_name='Contact',
        ),
        migrations.AlterModelManagers(
            name='contact',
            managers=[
            ],
        ),
    ]