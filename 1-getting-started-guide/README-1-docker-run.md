# Docker run

The docker run command runs a command in a new container, pulling the image if needed and starting the container.

https://docs.docker.com/engine/reference/commandline/run/

## Visuals

https://follow-e-lo.com/2023/12/29/docker-run/

## Examle Ubuntu

```bash

# list all images
docker images
# none

# list all running containers
docker ps

# list all containers
docker ps -a

# remove all containers
docker rm -f $(docker ps -a -q)


# pull ubuntu and start shell inside, quit shell with exit 13
docker run --name testubuntu -it ubuntu

docker ps

docker ps -a
# testubuntu  47 seconds ago

# start it, stop or restart
docker start testubuntu

# Capture container ID (--cidfile)

```
docker ps -a

CONTAINER ID   IMAGE     COMMAND       CREATED        STATUS                      PORTS     NAMES

2b2cce6e6241   ubuntu    "/bin/bash"   13 hours ago   Exited (137) 13 hours ago             testubuntu

docker images

REPOSITORY   TAG       IMAGE ID       CREATED       SIZE

ubuntu       latest    174c8c134b2a   2 weeks ago   77.8MB
## Example MariaDB

```bash

docker search mariadb

docker pull mariadb:11
```
https://mariadb.com/kb/en/installing-and-using-mariadb-via-docker/

## Example RabbitMQ

```bash
```

## Example Apache

```bash
```