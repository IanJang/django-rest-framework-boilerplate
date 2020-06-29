from config.settings.base import *

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'project_db',
        'USER': 'project_user',
        'PASSWORD': 'Pass1@3',
        'HOST': 'project_db',
        'PORT': '5432',
    }
}

# CELERY
CELERY_BROKER_URL = 'amqp://admin:Pass1@3@rabbitmq:5672//'
