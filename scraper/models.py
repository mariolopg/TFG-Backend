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
    _8_pin_connectors = models.IntegerField(validators=[MinValueValidator(0)])
    _6_pin_connectors = models.IntegerField(validators=[MinValueValidator(0)])

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
    _8_pcie_connectors = models.IntegerField(validators=[MinValueValidator(0)])
    _6_pcie_connectors = models.IntegerField(validators=[MinValueValidator(0)])

    class Meta:
        ordering = ['id']
 
    def __str__(self):
        return self

class StorageDrive(models.Model):

    FORM_FACTOR_CHOICES =(
        ('2.5', '2.5'),
        ('3.5', '3.5'),
        ('M.2', 'M.2'),
    )

    id = models.AutoField(primary_key = True)
    name = models.CharField(blank = False, max_length=100)
    size = models.IntegerField(validators=[MinValueValidator(1)])
    form_factor = models.CharField(blank = False, max_length=10, choices = FORM_FACTOR_CHOICES)
    bus = models.CharField(blank = False, max_length=100)

    class Meta:
        abstract = True
        unique_together = ['name', 'size', 'form_factor']

class HDD(StorageDrive):
    rpm = models.IntegerField(validators=[MinValueValidator(1)])

    class Meta:
        ordering = ['id']
 
    def __str__(self):
        return self

class SSD(StorageDrive):
    class Meta:
        ordering = ['id']
 
    def __str__(self):
        return self
    
class Cooler(models.Model):

    id = models.AutoField(primary_key = True)
    name = models.CharField(blank = False, max_length=200)
    supported_sockets = models.ManyToManyField(Socket)

    class Meta:
        abstract = True

class AirCooler(Cooler):
    height = models.IntegerField(validators=[MinValueValidator(1)])

    class Meta:
        ordering = ['id']
        unique_together = ['name', 'height']
 
    def __str__(self):
        return self

class LiquidCooler(Cooler):
    radiator = models.IntegerField(validators=[MinValueValidator(1)])
    _80_mm_fans = models.IntegerField(validators=[MinValueValidator(0)])
    _92_mm_fans = models.IntegerField(validators=[MinValueValidator(0)])
    _120_mm_fans = models.IntegerField(validators=[MinValueValidator(0)])
    _140_mm_fans = models.IntegerField(validators=[MinValueValidator(0)])
    _200_mm_fans = models.IntegerField(validators=[MinValueValidator(0)])
    class Meta:
        ordering = ['id']
        unique_together = ['name', 'radiator']
 
    def __str__(self):
        return self
    
class Case(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(blank = False, unique=True, max_length=100)
    motherboard_size = models.CharField(blank = False, max_length=10, choices=Motherboard.FORM_FACTOR_CHOICES)
    psu_size = models.CharField(blank = False, max_length=10, choices=PSU.FORM_FACTOR_CHOICES)
    gpu_length = models.IntegerField(validators=[MinValueValidator(1)])
    air_cooler_height = models.IntegerField(validators=[MinValueValidator(1)])
    _120_radiator_support = models.IntegerField(validators=[MinValueValidator(0)])
    _140_radiator_support = models.IntegerField(validators=[MinValueValidator(0)])
    _240_radiator_support = models.IntegerField(validators=[MinValueValidator(0)])
    _280_radiator_support = models.IntegerField(validators=[MinValueValidator(0)])
    _360_radiator_support = models.IntegerField(validators=[MinValueValidator(0)])
    _2_5_disk_slot = models.IntegerField(validators=[MinValueValidator(0)])
    _3_5_disk_slot = models.IntegerField(validators=[MinValueValidator(0)])

    class Meta:
        ordering = ['name']
 
    def __str__(self):
        return self
 