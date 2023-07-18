"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from rest_framework import routers
from django.contrib import admin
from django.urls import path, include
from api.views import *

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

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/scrap/<component>', scrap),
    path('api/', include(router.urls))
]
