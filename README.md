# learning-docker
Testing and learning Docker with Azure

## Learning docker

* Python for programming
* Bash and linux
* Azure VM with Docker
* Azure Container with Docker

## Visuals

https://follow-e-lo.com/2023/12/20/docker/

## What ARE Containers? (and Docker ...)

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


## Mount fileshare on VM

Storage account staccvmdocker01

Fileshare dockershare01

Better use a disk, not fileshare....args



## Overview of get started

https://github.com/spawnmarvel/learning-docker/blob/main/README-1-getstarted.md


## Docker basic commands

```bash
# login
ssh user@IP

```
https://github.com/spawnmarvel/learning-docker/blob/main/README-2-commands.md

## Configure Applications

RabbitMQ:

https://github.com/spawnmarvel/learning-docker/tree/main/rmq

Zabbix:

Wordpress:

Portainer:

## Using docker on Azure Container

