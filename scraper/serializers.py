from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from dj_rest_auth.serializers import UserDetailsSerializer
from django.utils.translation import gettext as _

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

class CaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Case
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    builder_data = UserDetailsSerializer(read_only=True, source='builder')
    class Meta:
        model = Comment
        fields = '__all__'
        extra_kwargs = {
            'build': {'write_only': True},
        }

class BuildImageSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        user = self.context['request'].user

        if user == validated_data.get('build').builder:
            image = BuildImage(**validated_data)
            image.save()
            return image
        else:
            raise serializers.ValidationError(_("You do not have permission to perform this action."))

    class Meta:
        model = BuildImage
        fields = '__all__'
        extra_kwargs = {
            'build': {'write_only': True},
        }

class BuildSerializer(serializers.ModelSerializer):
    cpu_data = CPUSerializer(read_only=True, source='cpu')
    motherboard_data = MotherboardSerializer(read_only=True, source='motherboard')
    ram_data = RAMSerializer(read_only=True, source='ram')
    gpu_data = GPUSerializer(read_only=True, source='gpu')
    air_cooler_data = AirCoolerSerializer(read_only=True, source='air_cooler')
    liquid_cooler_data = LiquidCoolerSerializer(read_only=True, source='liquid_cooler')
    hdd_data = HDDSerializer(read_only=True, source='hdd')
    ssd_data = SSDSerializer(read_only=True, source='ssd')
    psu_data = PSUSerializer(read_only=True, source='psu')
    case_data = CaseSerializer(read_only=True, source='case')

    comments = CommentSerializer(read_only=True, many=True, source='comment_set')
    images = BuildImageSerializer(read_only=True, many=True, source='buildimage_set')
    builder_data = UserDetailsSerializer(read_only=True, source='builder')

    def check_sockets(self, attrs):
        errors = {}

        cpu = attrs.get('cpu')
        motherboard = attrs.get('motherboard')

        if cpu.socket != motherboard.socket:
            errors['motherboard'] = _("CPU and Motherboard Sockets must be the same")

        return errors
    
    def check_cooler(self, attrs):
        errors = {}

        cpu = attrs.get('cpu')
        air_cooler = attrs.get('air_cooler', None)
        liquid_cooler = attrs.get('liquid_cooler', None)

        if not air_cooler and not liquid_cooler:
            errors['cooler'] = _("You must select a Cooler")
        elif air_cooler and liquid_cooler:
            errors['cooler'] = _("You only can select one Cooler")
        elif air_cooler and not cpu.socket in air_cooler.supported_sockets.all():
            errors['air_cooler'] = _("CPU and Cooler Sockets must be the same")
        elif liquid_cooler and not cpu.socket in liquid_cooler.supported_sockets.all():
            errors['liquid_cooler'] = _("CPU and Cooler Sockets must be the same")

        return errors
    
    def check_ram(self, attrs):
        errors = {}

        motherboard = attrs.get('motherboard')
        ram = attrs.get('ram')

        if motherboard.memory_type != ram.type:
            errors['ram'] =  _("Motherboard and RAM must have the same RAM type")
        elif motherboard.ram_slots < ram.units:
            errors['ram'] =  _("There are more modules on this RAM pack than the availables on the Motherboard")
        elif motherboard.ram_capacity < ram.size:
            errors['ram'] =  _("The maximun RAM size on this Motherboard is smaller than the RAM size of this RAM pack")

        return errors
    
    def check_gpu(self, attrs):
        errors = {}

        cpu = attrs.get('cpu')
        gpu = attrs.get('gpu', None)

        if not gpu and not cpu.integrated_graphics:
            errors['gpu'] = _("You must select a Graphics Card because CPU doesn't have integrated graphics")

        return errors
    
    def check_storage_drives(self, attrs):
        errors = {}

        motherboard = attrs.get('motherboard')
        hdd = attrs.get('hdd', None)  
        ssd = attrs.get('ssd', None)

        if not (hdd or ssd):
            errors['storage_drive'] = _("You must select at least one Storage Drive Unit")
        else:
            if hdd and ssd:
                if ssd.form_factor == '2.5' and motherboard.sata_slots < 2:
                    errors['storage_drive'] = _("These HDD and SSD not compatible because there aren't enoght SATA ports on this Motherboard")
            elif hdd and motherboard.sata_slots == 0:
                errors['hdd'] = _("This HDD is not compatible because there isn't any SATA ports on this Motherboard")
            elif ssd:
                form_factor = ssd.form_factor
                m2_slots = motherboard.m2_3_slots + motherboard.m2_3_slots
                if form_factor == 'M.2' and m2_slots == 0:
                    errors['ssd'] = _("This SSD is not compatible because there aren't any M.2 ports on this Motherboard")
                elif form_factor == '2.5' and motherboard.sata_slots == 0:
                    errors['ssd'] = _("This SSD is not compatible because there aren't any SATA ports on this Motherboard")
    
        return errors
    
    def check_case(self, attrs):
        errors = []

        case = attrs.get('case')

        case_motherboard_compatibility = {
            'E-ATX': ['E-ATX', 'ATX', 'Micro-ATX', 'Mini-ITX'],
            'ATX': ['ATX', 'Micro-ATX', 'Mini-ITX'],
            'Micro-ATX': ['Micro-ATX', 'Mini-ITX'],
            'Mini-ITX': ['Mini-ITX']
        }

        motherboard = attrs.get('motherboard')

        air_cooler = attrs.get('air_cooler', None)
        liquid_cooler = attrs.get('liquid_cooler', None)

        hdd = attrs.get('hdd', None)  
        ssd = attrs.get('ssd', None)

        gpu = attrs.get('gpu', None)
        psu = attrs.get('psu', None)

        if not motherboard.form_factor in case_motherboard_compatibility[case.motherboard_size]:
            errors.append(_("This Case is very small for the selected Motherboard"))

        if gpu and gpu.length > case.gpu_length:
            errors.append( _("This Case is very small for the selected Graphics Card"))

        if air_cooler and air_cooler.height > case.air_cooler_height:
            errors.append(_("This Case is very small for the selected Air Cooler"))

        if liquid_cooler and getattr(case, f"_{liquid_cooler.radiator}_radiator_support") == 0:
            errors.append(_("This Case is not compatible with the radiator of the selected Liquid Cooler"))

        if psu.form_factor != case.psu_size:
            errors.append( _("This Case is not compatible with the form factor of the selected PSU"))


        _2_5_slots_to_check = 0
        if hdd:
            if hdd.form_factor == '2.5':
                _2_5_slots_to_check = 1
            elif case._3_5_disk_slot == 0:
                errors.append(_("This Case don't have any 3.5\" slot"))

        if ssd:
            if ssd.form_factor == '2.5':
                _2_5_slots_to_check += 1

        if _2_5_slots_to_check > 0 and case._2_5_disk_slot < _2_5_slots_to_check:
            errors.append(_("This Case don't have enoght 2.5\" slots"))


        if errors:
            return {'case': errors}
        
        return {}
    
    def validate(self, attrs):
        errors = {}
        checks = ['sockets', 'cooler', 'ram', 'gpu', 'storage_drives', 'case']

        for check in checks:
            errors |= getattr(self, f"check_{check}")(attrs)

        if errors:
            raise ValidationError(errors)

        return attrs

    class Meta:
        model = Build
        fields = '__all__'
