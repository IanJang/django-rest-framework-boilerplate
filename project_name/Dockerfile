FROM python:3.8.3

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
COPY /requirements/requirements-base.txt requirements.txt
RUN pip install -r requirements.txt

COPY . /usr/src/app
WORKDIR /usr/src/app

# collectstatic
RUN python manage.py collectstatic --noinput
