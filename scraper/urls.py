# authentication/urls.py
from rest_framework import routers
from django.urls import path, include

from scraper.views import CPUViewSet, MotherboardViewSet, RAMViewSet, GPUViewSet, AirCoolerViewSet, LiquidCoolerViewSet, HDDViewSet, SSDViewSet, CaseViewSet, PSUViewSet,BuildViewSet, CommentViewSet, BuildImageViewSet

router = routers.SimpleRouter()
router.register(r'cpu', CPUViewSet)
router.register(r'motherboard', MotherboardViewSet)
router.register(r'ram', RAMViewSet)
router.register(r'gpu', GPUViewSet)
router.register(r'air_cooler', AirCoolerViewSet)
router.register(r'liquid_cooler', LiquidCoolerViewSet)
router.register(r'hdd', HDDViewSet)
router.register(r'ssd', SSDViewSet)
router.register(r'psu', PSUViewSet)
router.register(r'case', CaseViewSet)
router.register(r'build', BuildViewSet)
router.register(r'comment', CommentViewSet)
router.register(r'build_image', BuildImageViewSet)

urlpatterns = [
    path("", include(router.urls)),
]