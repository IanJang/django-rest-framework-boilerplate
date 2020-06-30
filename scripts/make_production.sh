#!/usr/bin/env bash

docker-compose -f docker-compose.yml -f docker-compose.production.yml stop
docker-compose -f docker-compose.yml -f docker-compose.production.yml up --build

docker rmi "$(docker images -f "dangling=true" -q)" 2> /dev/null
