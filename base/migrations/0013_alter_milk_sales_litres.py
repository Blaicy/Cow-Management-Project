# Generated by Django 5.2 on 2025-04-08 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0012_alter_feeding_record_session_alter_milk_sales_litres_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='milk_sales',
            name='litres',
            field=models.FloatField(default=0),
        ),
    ]
