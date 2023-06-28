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

class GPUSeriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = GPUSeries
        fields = ['id']

class GPUSerializer(serializers.ModelSerializer):
    class Meta:
        model = GPU
        fields = ['name', 'series', 'vram', 'tdp', 'length', 'eight_pin_connectors', 'six_pin_connectors']

class PSUSerializer(serializers.ModelSerializer):
    class Meta:
        model = PSU
        fields = ['name', 'watts', 'form_factor', 'efficiency', 'eight_pcie_connectors', 'six_pcie_connectors']

class HDDSerializer(serializers.ModelSerializer):
    class Meta:
        model = HDD
        fields = ['name', 'size', 'form_factor', 'bus', 'rpm']

class SSDSerializer(serializers.ModelSerializer):
    class Meta:
        model = SSD
        fields = ['name', 'size', 'form_factor', 'bus']