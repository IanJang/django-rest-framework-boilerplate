#!/usr/bin/env bash

docker-compose -f docker-compose.yml -f docker-compose.staging.yml stop
docker-compose -f docker-compose.yml -f docker-compose.staging.yml up --build

docker rmi "$(docker images -f "dangling=true" -q)" 2> /dev/null
