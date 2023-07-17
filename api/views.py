from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from scraper.views import *

@csrf_exempt
def Scrap(request, component):
    hardware_testing = scrap(component=component)
    return JsonResponse(hardware_testing, safe = False)

@csrf_exempt
@api_view(('POST',))
def Build(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        return CreateBuild(data)
    
    return HttpResponse(status = 404)