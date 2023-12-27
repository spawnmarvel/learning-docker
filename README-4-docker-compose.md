# Docker compose reference

The Compose file is a YAML file defining services, networks and volumes. The default path for a Compose file is ./docker-compose.yml.

A service definition contains configuration that is applied to each container started for that service, much like passing command-line parameters to docker run. Likewise, network and volume definitions are analogous to docker network create and docker volume create.

As with docker run, options specified in the Dockerfile, such as CMD, EXPOSE, VOLUME, ENV, are respected by default - you don't need to specify them again in docker-compose.yml.



## Reference

https://docs.docker.com/compose/compose-file/compose-file-v3/

## Files and cmds examples

```bash

Dockerfile

# syntax=docker/dockerfile:1
FROM python:3.7-alpine
WORKDIR /code
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
RUN apk add --no-cache gcc musl-dev linux-headers
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 5000
COPY . .
CMD ["flask", "run"]

compose

services:
  web:
    build: .
    ports:
      - "8000:5000"
    volumnes:
      - .:/code
    environment:
      FLASK_DEBUG: "true"
  redis:
    image: "redis:alpine"

docker compose up -d
docker ps
docker compose down
docker logs containername
docker inspect containername
docker images
docker rmi containerid --force

```
## build

```yml

```

## next

```yml

```

## next

```yml

```
