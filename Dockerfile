FROM python:3.8.3

COPY requirements/requirements-base.txt requirements.txt
RUN pip install -r requirements.txt

COPY project_name project_name
WORKDIR project_name
