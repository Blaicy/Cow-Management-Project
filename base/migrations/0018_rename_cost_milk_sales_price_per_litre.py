# Generated by Django 5.2 on 2025-04-11 21:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0017_remove_reproduction_estimated_delivery'),
    ]

    operations = [
        migrations.RenameField(
            model_name='milk_sales',
            old_name='cost',
            new_name='price_per_litre',
        ),
    ]
