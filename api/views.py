from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import sys

from scraper.views import *

@csrf_exempt
def Scrap(request, component):
    hardware_testing = getattr(sys.modules[__name__], "scrap_%s" % component)()
    return JsonResponse(hardware_testing, safe = False)