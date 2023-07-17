import sys
from .scraper import *

def scrap(component):
    return getattr(sys.modules[__name__], "scrap_%s" % component)()

def CreateBuild(data):
    serializer = BuildSerializer(data=data)
    return save_serializer(serializer=serializer)