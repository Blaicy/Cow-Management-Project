# Generated by Django 5.2 on 2025-04-08 14:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0010_funfacts_manure_sales_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='manure_sales',
            old_name='litres',
            new_name='quantity',
        ),
    ]
