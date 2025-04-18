# Generated by Django 5.2 on 2025-04-08 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0009_spraying_birth_records'),
    ]

    operations = [
        migrations.CreateModel(
            name='Funfacts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fact', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Manure_Sales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('litres', models.FloatField(default=0)),
                ('cost', models.FloatField(default=0)),
            ],
        ),
        migrations.RemoveField(
            model_name='veterinary_care',
            name='medicine',
        ),
        migrations.RemoveField(
            model_name='veterinary_care',
            name='quantity',
        ),
    ]
