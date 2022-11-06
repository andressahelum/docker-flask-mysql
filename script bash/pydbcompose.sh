#!/bin/bash

echo Opening application directory.
# Change this path below by the path of your docker-compose.yaml (something like /opt/app/pydbcompose)
cd C:\Users\Helum\PycharmProjects\pydbcompose
echo Running docker compose.
docker compose build
docker compose up -d
echo Done!