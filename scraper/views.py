import sys

from rest_framework import viewsets
from django.http import JsonResponse
from .scraper import *

def scrap(request, component):
    if request.method == 'GET':
        hardware = getattr(sys.modules[__name__], "scrap_%s" % component)()
        return JsonResponse(hardware, safe = False)

class CPUViewSet(viewsets.ModelViewSet):
    queryset = CPU.objects.all()
    serializer_class = CPUSerializer

class MotherboardViewSet(viewsets.ModelViewSet):
    queryset = Motherboard.objects.all()
    serializer_class = MotherboardSerializer

class RAMViewSet(viewsets.ModelViewSet):
    queryset = RAM.objects.all()
    serializer_class = RAMSerializer

class GPUViewSet(viewsets.ModelViewSet):
    queryset = GPU.objects.all()
    serializer_class = GPUSerializer

class AirCoolerViewSet(viewsets.ModelViewSet):
    queryset = AirCooler.objects.all()
    serializer_class = AirCoolerSerializer

class LiquidCoolerViewSet(viewsets.ModelViewSet):
    queryset = LiquidCooler.objects.all()
    serializer_class = LiquidCoolerSerializer

class HDDViewSet(viewsets.ModelViewSet):
    queryset = HDD.objects.all()
    serializer_class = HDDSerializer

class SSDViewSet(viewsets.ModelViewSet):
    queryset = SSD.objects.all()
    serializer_class = SSDSerializer

class PSUViewSet(viewsets.ModelViewSet):
    queryset = PSU.objects.all()
    serializer_class = PSUSerializer

class CaseViewSet(viewsets.ModelViewSet):
    queryset = Case.objects.all()
    serializer_class = CaseSerializer

class BuildViewSet(viewsets.ModelViewSet):
    queryset = Build.objects.all()
    serializer_class = BuildSerializer

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class BuildImageViewSet(viewsets.ModelViewSet):
    queryset = BuildImage.objects.all()
    serializer_class = BuildImageSerializer