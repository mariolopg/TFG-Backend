import sys
from django_cron import CronJobBase, Schedule
from .views import *

class AutoScrap(CronJobBase):
    RUN_EVERY_MINS = 1

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'cron.auto_scrap'

    COMPONENTS = ['motherboards', 'coolers', 'cpus', 'rams', 'gpus', 'hdds', 'ssds', 'psus', 'cases']

    def do(self):
        for component in self.COMPONENTS:
            getattr(sys.modules[__name__], "scrap_%s" % component)()
