# Generated by Django 4.1.1 on 2023-06-28 16:16

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scraper', '0009_alter_psu_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='HDD',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('size', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('form_factor', models.CharField(choices=[('2.5', '2.5'), ('3.5', '3.5'), ('M.2', 'M.2')], max_length=10)),
                ('bus', models.CharField(max_length=100)),
                ('rpm', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)])),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='SSD',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('size', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('form_factor', models.CharField(choices=[('2.5', '2.5'), ('3.5', '3.5'), ('M.2', 'M.2')], max_length=10)),
                ('bus', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
    ]