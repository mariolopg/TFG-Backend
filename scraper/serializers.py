from rest_framework import serializers
from .models import *
 
class CPUSerializer(serializers.ModelSerializer):
    class Meta:
        model = CPU
        fields = ['name', 'socket', 'cores', 'threads']

class MotherboardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Motherboard
        fields = ['name', 'form_factor', 'socket', 'chipset', 'memory_type', 'ram_capacity', 'ram_slots', 'sata_slots', 'm2_3_slots', 'm2_4_slots']

class RAMSerializer(serializers.ModelSerializer):
    class Meta:
        model = RAM
        fields = ['name', 'type', 'size', 'mhz', 'units']