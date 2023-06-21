from django.db import models
from django.core.validators import *

# Create your models here.

class CPU(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(blank = False, unique=True, max_length=100)
    socket = models.CharField(blank = False, max_length=100)
    cores = models.IntegerField(validators=[MinValueValidator(1)])
    threads = models.IntegerField(validators=[MinValueValidator(1)])

    class Meta:
        _name = ['name']
        _socket = ['socket']
        _cores = ['cores']
        _threads = ['threads']
 
    def __str__(self):
        return f"CPU: {self.name}"
