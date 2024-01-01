# learning-docker
Testing and learning Docker with Azure

## Learning docker


What do we get extra here:

* Python for programming
* Bash and linux, ssh, .sh scripts
* Azure VM with Docker, mount data drive, NSG
* Azure Container with Docker


Azure resources

![Azure resources](https://github.com/spawnmarvel/learning-docker/blob/main/images/azure_resources.jpg)

## Visuals

https://follow-e-lo.com/2023/12/20/docker/

## 1 Getting started guide CLI TODO

https://github.com/spawnmarvel/learning-docker/blob/main/1-getting-started-guide/README.md

## 1.1 What ARE Containers? (and Docker ...) TODO

https://github.com/spawnmarvel/learning-docker/blob/main/1.1-what-are-containers-john-s/Examples.sh

All examples bash

https://github.com/spawnmarvel/learning-docker/blob/main/1-what-are-containers-john-s/Examples.sh

Notes:

Linux control groups, cgroup, how much cpu, memeory, blokio.

Eveything on linux lives in cgroup.

Docker process within container running in own cgroup.

31.37

* 


## 1.2 Tutorialspoint TODO

https://github.com/spawnmarvel/learning-docker/blob/main/1.2-tutorialspoint/README.md

## Docker docs

Docker Engine is an open source containerization technology for building and containerizing your applications

https://docs.docker.com/engine/

## Installing Docker on a VM (Azure) (Done)

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


## Mount disk on VM (Done)

* cd /datadrive/

https://github.com/spawnmarvel/learning-docker/blob/main/README-0-mount.md


## Docker user setup (Done)

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

## Docker basic commands (Done)

```bash
# get all commands
docker

# help
docker COMMAND --help

docker system info

# https://www.digitalocean.com/community/tutorials/how-to-remove-docker-images-containers-and-volumes

# Docker provides a single command that will clean up any resources — images, containers, volumes, and networks — that are dangling (not tagged or associated with a container):
docker system prune

# To additionally remove any stopped containers and all unused images (not just dangling images), add the -a flag to the command:
docker system prune -a

# remove images
docker images -a
docker rmi -f id_name

# remove containers
docker ps -a
dokcer rm -f id_name

# remove volumes
docker volume ls
docker volume rm -f volume_name

# create the volume for presistent rmq,  and pull rmq, start rmq
docker volume create rabbitmq_data

# the volume is on a mounted datadrive, view README-2-docker-volume.md, so we can separate os from data and even increase the disk.
sudo su -
cd /datadrive
# buildkit  containers  engine-id  image  network  overlay2  plugins  runtimes  swarm  tmp  volumes
exit

df -h
# Filesystem      Size  Used Avail Use% Mounted on
# /dev/sda1       4.0G  702M  3.4G  18% /datadrive

# create the container for rmq
docker run -d --hostname rmq2 --name rabbitmq2 -p 15672:15672 -p 5672:5672 --mount type=volume,src=rabbitmq_data,target=/var/lib/rabbitmq rabbitmq:3.12-management

# view it
docker ps

docker images
# REPOSITORY                 TAG                       
# rabbitmq                   3.12-management

# you can now stop and start the container with a volume
# or set it to always run
docker restart, stop, start rabbitmq2
```
## Docker Volums (preferred by Docker containers)

Volumes are a mechanism for storing data outside containers. All volumes are managed by Docker and stored in a dedicated directory on your host, usually /var/lib/docker/volumes for Linux systems.

```bash
# create the volume
docker volume create rabbitmq_data

# create the container
docker run -d --hostname rmq2 --name rabbitmq2 -p 15672:15672 -p 5672:5672 --mount type=volume,src=rabbitmq_data,target=/var/lib/rabbitmq rabbitmq:3.12-management

```
https://follow-e-lo.com/2023/12/30/docker-volume-data-move/

## Docker file

Dockerfile

https://github.com/spawnmarvel/learning-docker/blob/main/README-1-dockerfile-reference

## Install Docker Compose Ubuntu (Done)

It seems that it is already apart of the docker install from apt (install docker)

```bash
sudo apt update
sudo apt install docker-compose-plugin
# docker-compose-plugin is already the newest version (2.21.0-1~ubuntu.22.04~jammy).

docker compose version
Docker Compose version v2.21.0
```

## Docker compose commands

```bash
mkdir composetest

cd composetest

# for python code for example
sudo nano Dockerfile

sudo nano compose.yml

# If you want to run your services in the background, you can pass the -d flag (for "detached" mode) to docker compose up and use docker compose ps to see what is currently running:

docker compose up -d

docker compose up

# Switch to another terminal
docker images

docker image ls

docker inspect containername

docker logs containername

docker compose ps

# The docker compose run command allows you to run one-off commands for your services. For example, to see what environment variables are available to the web service:
docker compose run web env

# If you started Compose with docker compose up -d, stop your services once you've finished with them:
docker compose stop

# You can bring everything down, removing the containers entirely, with the down command.
docker compose down

# Pass --volumes to also remove the data volume used by the Redis container:
docker compose down --volumes


```

## Docker Compose file version 3 reference

https://docs.docker.com/compose/compose-file/compose-file-v3/


# Azure

## Quickstart: Deploy a container instance in Azure using the Azure CLI

https://learn.microsoft.com/en-us/azure/container-instances/container-instances-quickstart

## Run Docker containers with Azure Container Instances

https://learn.microsoft.com/en-us/training/modules/run-docker-with-azure-container-instances/

## Azure Container Instances documentation

https://learn.microsoft.com/en-us/azure/container-instances/






