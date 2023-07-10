from rest_framework import serializers
from .models import *
 
class CPUSerializer(serializers.ModelSerializer):
    class Meta:
        model = CPU
        fields = '__all__'

class MotherboardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Motherboard
        fields = '__all__'
        
class RAMSerializer(serializers.ModelSerializer):
    class Meta:
        model = RAM
        fields = '__all__'

class GPUSeriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = GPUSeries
        fields = '__all__'

class GPUSerializer(serializers.ModelSerializer):
    class Meta:
        model = GPU
        fields = '__all__'

class PSUSerializer(serializers.ModelSerializer):
    class Meta:
        model = PSU
        fields = '__all__'

class HDDSerializer(serializers.ModelSerializer):
    class Meta:
        model = HDD
        fields = '__all__'

class SSDSerializer(serializers.ModelSerializer):
    class Meta:
        model = SSD
        fields = '__all__'

class AirCoolerSerializer(serializers.ModelSerializer):
    class Meta:
        model = AirCooler
        fields = '__all__'

class LiquidCoolerSerializer(serializers.ModelSerializer):
    class Meta:
        model = LiquidCooler
        fields = '__all__'

class CaseSerializeer(serializers.ModelSerializer):
    class Meta:
        model = Case
        fields = '__all__'