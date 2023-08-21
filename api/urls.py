from django.urls import path, include
from .views import *

urlpatterns = [
    path('', include('scraper.urls')),
    path('auth/', include('authentication.urls')),
    path('scrap/<component>', scrap),
]