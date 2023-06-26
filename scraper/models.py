from enum import Enum
from django.db import models
from django.core.validators import *
from enumchoicefield import ChoiceEnum, EnumChoiceField
# Create your models here.

class CPU(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(blank = False, unique=True, max_length=100)
    socket = models.CharField(blank = False, max_length=100)
    cores = models.IntegerField(validators=[MinValueValidator(1)])
    threads = models.IntegerField(validators=[MinValueValidator(1)])

    class Meta:
        ordering = ['name']
 
    def __str__(self):
        return f"CPU: {self.name}"

class Motherboard(models.Model):

    FORM_FACTOR_CHOICES =(
        ('E-ATX', 'E-ATX'),
        ('ATX', 'ATX'),
        ('Micro-ATX', 'Micro-ATX'),
        ('Mini-ITX', 'Mini-ITX'),
    )

    id = models.AutoField(primary_key = True)
    name = models.CharField(blank = False, unique=True, max_length=100)
    form_factor = models.CharField(blank = False, max_length=10, choices = FORM_FACTOR_CHOICES)
    socket = models.CharField(blank = False, max_length=10)
    chipset = models.CharField(blank = False, max_length=10)
    memory_type = models.CharField(blank = False, max_length=10)
    ram_capacity = models.IntegerField(validators=[MinValueValidator(1)])
    ram_slots = models.IntegerField(validators=[MinValueValidator(1)])
    sata_slots = models.IntegerField(validators=[MinValueValidator(0)])
    m2_3_slots = models.IntegerField(validators=[MinValueValidator(0)])
    m2_4_slots = models.IntegerField(validators=[MinValueValidator(0)])

    class Meta:
        ordering = ['name']
 
    def __str__(self):
        return f"Motherboard: {self.name}"
