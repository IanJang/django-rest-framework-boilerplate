#!/usr/bin/env bash

if [ "${IS_CELERY_WORKER}" == "true" ]
then
    celery -A config worker -l info
else
    python manage.py collectstatic --noinput
    python manage.py migrate
    gunicorn config.wsgi:application --bind 0.0.0.0:8000
fi
