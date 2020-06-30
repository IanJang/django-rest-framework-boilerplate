from config.settings.base import *

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres_db',
        'USER': 'postgres_user',
        'PASSWORD': 'Pass1@3',
        'HOST': '',
        'PORT': '5432',
    }
}

# SESSION
SESSION_COOKIE_SECURE = True

# CSRF
CSRF_COOKIE_SECURE = True

# SECURITY MIDDLEWARE
SECURE_HSTS_SECONDS = 31536000  # 365 * 24 * 60 * 60
SECURE_HSTS_PRELOAD = True
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_SSL_REDIRECT = True
SECURE_REFERRER_POLICY = 'same-origin'

# CELERY
CELERY_BROKER_URL = ''
