# Generated by Django 4.1.1 on 2023-06-26 18:29

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scraper', '0004_ram'),
    ]

    operations = [
        migrations.CreateModel(
            name='GPUSeries',
            fields=[
                ('id', models.CharField(max_length=100, primary_key=True, serialize=False)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='GPU',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('vram', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('tdp', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('length', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('eight_pin_connectors', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('six_pin_connectors', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('series', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='scraper.gpuseries')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]
