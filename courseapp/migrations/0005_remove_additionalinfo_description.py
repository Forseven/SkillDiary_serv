# Generated by Django 3.2 on 2021-10-25 12:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courseapp', '0004_auto_20211025_1437'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='additionalinfo',
            name='description',
        ),
    ]
