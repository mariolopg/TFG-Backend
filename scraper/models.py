from enum import Enum
from django.db import models
from django.core.validators import *
# Create your models here.
    
class Socket(models.Model):
    id = models.CharField(primary_key = True, max_length=50)
    class Meta:
        ordering = ['id']
 
    def __str__(self):
        return self
    
class Chipset(models.Model):
    id = models.CharField(primary_key = True, max_length=50)
    class Meta:
        ordering = ['id']
 
    def __str__(self):
        return self
    
class RAMType(models.Model):
    id = models.CharField(primary_key = True, max_length=50)
    class Meta:
        ordering = ['id']
 
    def __str__(self):
        return self
    
class CPU(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(blank = False, unique=True, max_length=100)
    socket = models.ForeignKey('Socket', on_delete=models.CASCADE)
    cores = models.IntegerField(validators=[MinValueValidator(1)])
    threads = models.IntegerField(validators=[MinValueValidator(1)])

    class Meta:
        ordering = ['name']
 
    def __str__(self):
        return self

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
    socket = models.ForeignKey('Socket', on_delete=models.CASCADE)
    chipset = models.ForeignKey('Chipset', on_delete=models.CASCADE)
    memory_type = models.ForeignKey('RAMType', on_delete=models.CASCADE)
    ram_capacity = models.IntegerField(validators=[MinValueValidator(1)])
    ram_slots = models.IntegerField(validators=[MinValueValidator(1)])
    sata_slots = models.IntegerField(validators=[MinValueValidator(0)])
    m2_3_slots = models.IntegerField(validators=[MinValueValidator(0)])
    m2_4_slots = models.IntegerField(validators=[MinValueValidator(0)])

    class Meta:
        ordering = ['name']
 
    def __str__(self):
        return self
    
class RAM(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(blank = False, unique=True, max_length=100)
    type = models.ForeignKey('RAMType', on_delete=models.CASCADE)
    size = models.IntegerField(validators=[MinValueValidator(1)])
    mhz = models.IntegerField(validators=[MinValueValidator(1)])
    units = models.IntegerField(validators=[MinValueValidator(1)])

    class Meta:
        ordering = ['name']
 
    def __str__(self):
        return self
    
class GPUSeries(models.Model):
    id = models.CharField(primary_key = True, max_length=100)
    class Meta:
        ordering = ['id']
 
    def __str__(self):
        return self
    
class GPU(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(blank = False, unique=True, max_length=100)
    series = models.ForeignKey('GPUSeries', on_delete=models.CASCADE)
    vram = models.IntegerField(validators=[MinValueValidator(1)])
    tdp = models.IntegerField(validators=[MinValueValidator(1)])
    length = models.IntegerField(validators=[MinValueValidator(1)])
    eight_pin_connectors = models.IntegerField(validators=[MinValueValidator(0)])
    six_pin_connectors = models.IntegerField(validators=[MinValueValidator(0)])

    class Meta:
        ordering = ['name']
 
    def __str__(self):
        return self
    
class PSUEfficiency(models.Model):
    id = models.CharField(primary_key = True, max_length=50)
    class Meta:
        ordering = ['id']
 
    def __str__(self):
        return self
    
class PSU(models.Model):

    FORM_FACTOR_CHOICES =(
        ('ATX', 'ATX'),
        ('TFX', 'TFX'),
        ('SFX', 'SFX'),
    )

    id = models.AutoField(primary_key = True)
    name = models.CharField(blank = False, unique=True, max_length=100)
    watts = models.IntegerField(validators=[MinValueValidator(1)])
    form_factor = models.CharField(blank = False, max_length=10, choices = FORM_FACTOR_CHOICES)
    efficiency = models.ForeignKey('PSUEfficiency', on_delete=models.CASCADE)
    eight_pcie_connectors = models.IntegerField(validators=[MinValueValidator(0)])
    six_pcie_connectors = models.IntegerField(validators=[MinValueValidator(0)])