#!/usr/bin/env bash

python manage.py collectstatic --noinput
python manage.py migrate
gunicorn project_name.wsgi:application --bind 0.0.0.0:8000
