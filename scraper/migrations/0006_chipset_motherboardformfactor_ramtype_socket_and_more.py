# Generated by Django 4.1.1 on 2023-06-27 16:20

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scraper', '0005_gpuseries_gpu'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chipset',
            fields=[
                ('id', models.CharField(max_length=20, primary_key=True, serialize=False)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='MotherboardFormFactor',
            fields=[
                ('id', models.CharField(max_length=20, primary_key=True, serialize=False)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='RAMType',
            fields=[
                ('id', models.CharField(max_length=20, primary_key=True, serialize=False)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Socket',
            fields=[
                ('id', models.CharField(max_length=20, primary_key=True, serialize=False)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.AlterField(
            model_name='gpu',
            name='eight_pin_connectors',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='gpu',
            name='series',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scraper.gpuseries'),
        ),
        migrations.AlterField(
            model_name='gpu',
            name='six_pin_connectors',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='cpu',
            name='socket',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scraper.socket'),
        ),
        migrations.AlterField(
            model_name='motherboard',
            name='chipset',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scraper.chipset'),
        ),
        migrations.AlterField(
            model_name='motherboard',
            name='memory_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scraper.ramtype'),
        ),
        migrations.AlterField(
            model_name='motherboard',
            name='socket',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scraper.socket'),
        ),
        migrations.AlterField(
            model_name='ram',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scraper.ramtype'),
        ),
    ]