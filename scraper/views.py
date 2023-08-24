import sys

from rest_framework import viewsets
from django.http import JsonResponse
from .scraper import *
from authentication.permissions import IsAuthenticatedCreateOnly, IsOwnerOrReadOnly, ReadOnly, IsBuildOwnerOrReadOnly

def scrap(request, component):
    if request.method == 'GET':
        hardware = getattr(sys.modules[__name__], "scrap_%s" % component)()
        return JsonResponse(hardware, safe = False)

class CPUViewSet(viewsets.ModelViewSet):
    queryset = CPU.objects.all()
    serializer_class = CPUSerializer
    permission_classes = [ReadOnly]

class MotherboardViewSet(viewsets.ModelViewSet):
    queryset = Motherboard.objects.all()
    serializer_class = MotherboardSerializer
    permission_classes = [ReadOnly]

class RAMViewSet(viewsets.ModelViewSet):
    queryset = RAM.objects.all()
    serializer_class = RAMSerializer
    permission_classes = [ReadOnly]

class GPUViewSet(viewsets.ModelViewSet):
    queryset = GPU.objects.all()
    serializer_class = GPUSerializer
    permission_classes = [ReadOnly]

class AirCoolerViewSet(viewsets.ModelViewSet):
    queryset = AirCooler.objects.all()
    serializer_class = AirCoolerSerializer
    permission_classes = [ReadOnly]

class LiquidCoolerViewSet(viewsets.ModelViewSet):
    queryset = LiquidCooler.objects.all()
    serializer_class = LiquidCoolerSerializer
    permission_classes = [ReadOnly]

class HDDViewSet(viewsets.ModelViewSet):
    queryset = HDD.objects.all()
    serializer_class = HDDSerializer
    permission_classes = [ReadOnly]

class SSDViewSet(viewsets.ModelViewSet):
    queryset = SSD.objects.all()
    serializer_class = SSDSerializer
    permission_classes = [ReadOnly]

class PSUViewSet(viewsets.ModelViewSet):
    queryset = PSU.objects.all()
    serializer_class = PSUSerializer
    permission_classes = [ReadOnly]

class CaseViewSet(viewsets.ModelViewSet):
    queryset = Case.objects.all()
    serializer_class = CaseSerializer
    permission_classes = [ReadOnly]

class BuildViewSet(viewsets.ModelViewSet):
    queryset = Build.objects.filter(builder__is_active=True)
    serializer_class = BuildSerializer
    permission_classes = [IsAuthenticatedCreateOnly, IsOwnerOrReadOnly]

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.filter(builder__is_active=True)
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedCreateOnly]

class BuildImageViewSet(viewsets.ModelViewSet):
    queryset = BuildImage.objects.all()
    serializer_class = BuildImageSerializer
    permission_classes = [IsBuildOwnerOrReadOnly]