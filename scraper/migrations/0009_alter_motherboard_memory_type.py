# Generated by Django 4.1.1 on 2023-06-26 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scraper', '0008_alter_motherboard_chipset_alter_motherboard_socket'),
    ]

    operations = [
        migrations.AlterField(
            model_name='motherboard',
            name='memory_type',
            field=models.CharField(max_length=100),
        ),
    ]
