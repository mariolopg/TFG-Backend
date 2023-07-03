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
        fields = ['name', 'series', 'vram', 'tdp', 'length', '_8_pin_connectors', '_6_pin_connectors']

class PSUSerializer(serializers.ModelSerializer):
    class Meta:
        model = PSU
        fields = ['name', 'watts', 'form_factor', 'efficiency', '_8_pcie_connectors', '_6_pcie_connectors']

class HDDSerializer(serializers.ModelSerializer):
    class Meta:
        model = HDD
        fields = ['name', 'size', 'form_factor', 'bus', 'rpm']

class SSDSerializer(serializers.ModelSerializer):
    class Meta:
        model = SSD
        fields = ['name', 'size', 'form_factor', 'bus']

class AirCoolerSerializer(serializers.ModelSerializer):
    class Meta:
        model = AirCooler
        fields = ['name', 'supported_sockets', 'height']

class LiquidCoolerSerializer(serializers.ModelSerializer):
    class Meta:
        model = LiquidCooler
        fields = ['name', 'supported_sockets', 'radiator', '_80_mm_fans', '_92_mm_fans', '_120_mm_fans', '_140_mm_fans', '_200_mm_fans']

class CaseSerializeer(serializers.ModelSerializer):
    class Meta:
        model = Case
        fields = ['name', 'motherboard_size', 'psu_size', 'gpu_length', 'air_cooler_height', '_120_radiator_support', '_140_radiator_support', '_240_radiator_support', '_280_radiator_support', '_360_radiator_support', '_2_5_disk_slot', '_3_5_disk_slot']