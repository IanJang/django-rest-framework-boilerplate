FROM python:3.8.3

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements/requirements-base.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt

# copy project
COPY . /usr/src/app
COPY . /usr/src/app

RUN chmod +x docker-entrypoint.sh
ENTRYPOINT ./docker-entrypoint.sh
