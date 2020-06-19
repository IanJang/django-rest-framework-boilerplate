#!/usr/bin/env bash

docker-compose -f docker-compose.yml -f docker-compose.local.yml stop
docker-compose -f docker-compose.yml -f docker-compose.local.yml up --build

