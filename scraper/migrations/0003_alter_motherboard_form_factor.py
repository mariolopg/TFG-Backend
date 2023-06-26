# Generated by Django 4.1.1 on 2023-06-26 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scraper', '0002_alter_motherboard_form_factor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='motherboard',
            name='form_factor',
            field=models.CharField(choices=[('E-ATX', 'E-ATX'), ('ATX', 'ATX'), ('Micro-ATX', 'Micro-ATX'), ('Mini-ITX', 'Mini-ITX')], max_length=10),
        ),
    ]