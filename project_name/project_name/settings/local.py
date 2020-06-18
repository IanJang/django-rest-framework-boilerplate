from project_name.settings.base import *

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
