# Generated by Django 5.2 on 2025-04-14 11:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0024_delete_immunisation_records'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Cow',
            new_name='Cow_Profile',
        ),
    ]
