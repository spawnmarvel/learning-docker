# learning-docker
Testing and learning Docker with Azure

## Learning docker

* Python for programming
* Bash and linux
* Azure VM with Docker
* Azure Container with Docker

## Visuals

https://follow-e-lo.com/2023/12/20/docker/

## 1 What ARE Containers? (and Docker ...)

Time 11.51

https://github.com/spawnmarvel/learning-docker/tree/main/1-what-are-containers

## Docker docs

Docker Engine is an open source containerization technology for building and containerizing your applications

https://docs.docker.com/engine/

## Installing Docker on a VM (Azure)

Update vm vmdocker01

```bash
# update vm
sudo apt update -y

sudo apt upgrade -y

```
Create script

```bash

# create script
touch add_repository_to_apt.sh

nano add_repository_to_apt.sh

#!/bin/bash
# Add Docker's official GPG key:
sudo apt update
sudo apt install ca-certificates curl gnupg
sudo install -m 0755 -d /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
sudo chmod a+r /etc/apt/keyrings/docker.gpg

# Add the repository to Apt sources:
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update

```
Run it
```bash
sudo bash add_repository_to_apt.sh

```

Install the Docker packages

```bash
sudo apt install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

Verify Docker Engine
```bash
sudo docker run hello-world

# Unable to find image 'hello-world:latest' locally
# latest: Pulling from library/hello-world
# xxxxxxxxxx: Pull complete
# Digest: sha256:xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
# Status: Downloaded newer image for hello-world:latest

# Hello from Docker!
# This message shows that your installation appears to be working correctly.

# To generate this message, Docker took the following steps:
# 1. The Docker client contacted the Docker daemon.
# 2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
#    (amd64)
# 3. The Docker daemon created a new container from that image which runs the
#    executable that produces the output you are currently reading.
# 4. The Docker daemon streamed that output to the Docker client, which sent it
#    to your terminal.

# To try something more ambitious, you can run an Ubuntu container with:
# $ docker run -it ubuntu bash

# Share images, automate workflows, and more with a free Docker ID:
# https://hub.docker.com/

# For more examples and ideas, visit:
#  https://docs.docker.com/get-started/


docker --version
# Docker version 24.0.7, build afdd53b
```

https://docs.docker.com/engine/install/ubuntu/


## Mount disk on VM

* cd /datadrive/

https://github.com/spawnmarvel/learning-docker/blob/main/README-0-mount.md


## Overview of get started

https://github.com/spawnmarvel/learning-docker/blob/main/README-1-getstarted.md


## Docker user setup

```bash
# login
ssh user@IP

# From above we ised sudo in front of docker, result without
docker run hello-world
# docker: permission denied while trying to connect to the Docker daemon socket

# Check if docker groups is present
getent group

getent group | grep docker
# docker:x:999:

# check if a user is in a group
id username

# Add the connected user "$USER" to the docker group. Change the user name to match your preferred user if you do not want to use your current user:

sudo gpasswd -a $USER docker
# Adding user username to group docker

# Activate, either do a newgrp docker or log out/in to activate the changes to groups.
newgrp docker

# Now run
docker run hello-world
# Hello from Docker!
# This message shows that your installation appears to be working correctly.

```
https://github.com/spawnmarvel/learning-docker/blob/main/README-2-commands.md

## Docker basic commands

```bash
# get all
docker

# help
docker COMMAND --help

# show containers running
docker ps

# show docker all info
docker info

# [version, path etc]
# Server:
# Containers: 3
#  Running: 0
#  Paused: 0
#  Stopped: 3
#  Images: 1

# search images from repos
docker search mariadb

# pull
docker pull mariadb:11.0

# list installed images
docker images

# docker make container
docke run -help

docker run --name mariadbtest -e MYSQL_ROOT_PASSWORD=mypass -p 3306:3306 -d docker.io/library/mariadb:11.0

docker start mariadbtest
docker restart mariadbtest

# With docker stop, the container will be gracefully terminated: a SIGTERM signal will be sent
docker stop mariadbtest
docker stop --time=30 mariadbtest

# Or it is possible to immediately kill the process, with no timeout.
docker kill mariadbtest

# Automatic Restart, It is possible to change the restart policy of existing, possibly running containers:
docker update --restart always mariadb

# destroy container
docker rm mariadbtest

# Note that the command above does not destroy the data volume that Docker has created for /var/lib/mysql. If you want to destroy the volume as well, use:

docker rm -v mariadbtest

# Troubleshooting a Container
docker logs mariadbtest

# Accessing the Container
docker exec -it mariadbtest bash

# Now we can use normal Linux commands like cd, ls, etc. We will have root privileges. We can even install our favorite file editor.

exit

# Connecting to MariaDB from Outside the Container
docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' mariadbtest

# You can now connect to the MariaDB server using a TCP connection to that IP address.
sudo apt install mysql-client-core-8.0

# connect
mysql -h 172.17.0.2 -u root -p
# Enter password:
# Welcome to the MySQL monitor.  Commands end with ; or \g.
# Your MySQL connection id is 3
# Server version: 11.0.4-MariaDB-1:11.0.4+maria~ubu2204 mariadb.org binary distribution



```
https://github.com/spawnmarvel/learning-docker/blob/main/README-2-commands.md

## Docker Volums

Volumes are a mechanism for storing data outside containers. All volumes are managed by Docker and stored in a dedicated directory on your host, usually /var/lib/docker/volumes for Linux systems.

```bash

# Root
sudo su -

cd /var/lib/docker
# buildkit  containers  engine-id  image  network  overlay2  plugins  runtimes  swarm  tmp  volumes

# switch
su username

```
## Configure Applications

MariaDB:

RabbitMQ:

https://github.com/spawnmarvel/learning-docker/tree/main/rmq

Zabbix:

Wordpress:

Portainer:

## Using docker on Azure Container

