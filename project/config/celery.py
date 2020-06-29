from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

DEPLOYMENT_LEVEL = os.environ.setdefault("DEPLOYMENT_LEVEL", "development")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.{deployment_level}".format(deployment_level=DEPLOYMENT_LEVEL))

app = Celery('api')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
