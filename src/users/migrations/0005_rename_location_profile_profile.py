# Generated by Django 5.1.7 on 2025-03-27 16:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_location_zip_code'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='location',
            new_name='profile',
        ),
    ]
