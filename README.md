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

## 1 Getting started guide CLI

* docker run
* docker volume
* docker newtwork
* docker compose
* docker build

https://github.com/spawnmarvel/learning-docker/blob/main/1-getting-started-guide/README.md

## 1.1 What are containers and docker

https://github.com/spawnmarvel/learning-docker/blob/main/1.1-what-are-containers-john-s/Examples.sh

All examples bash

https://github.com/spawnmarvel/learning-docker/blob/main/1-what-are-containers-john-s/Examples.sh

Notes:

**Controlling resources**

* Linux control groups, cgroups (default to linux), how much cpu, memeory, blockio.
* Everything on linux lives in cgroup.
* Docker process within container running in own cgroup, meaning we an restrict all of this.
* And thats is, the cgroup can controll, check and controll the container.

```bash
# region Cgroups
# [...]

#starting deteched -d but interactive -it so bash has a terminal to attach to and not exit straight away
# Run new container with a name, detached/interactive, 
# limit resources, use Ubuntu image and the container should run the bash process
docker run --name ubuntu -dit --memory=256m --cpus="2" ubuntu bash
```

**Visibility (isoloation) Namespaces**

* Linux default also, can use name space.

```bash
# region Namespaces


```

38.00

* 


## 1.2 dockerlabs TODO

For notes view readme

https://github.com/spawnmarvel/learning-docker/tree/main/1.2-dockerlabs


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

## Docker clean up docker clutter

Use the docker prune’ command to clean up various Docker objects, freeing up system resources and making your Docker environment more efficient. 

```bash
# To remove all stopped containers
docker container prune

# To remove all unused networks
docker network prune

# To remove all dangling images
docker image prune

# To remove all unused volumes
docker volume prune

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
docker rmi -f $(docker images -aq)

# remove containers
docker ps -a
docker rm -f id_name
docker rm $(docker ps -aq)

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

# view logs
docker logs rabbitmq
docker logs -f rabbitmq

# 2024-01-01 15:47:03.330225+00:00 [info] <0.230.0>  node           : rabbit@rmq2
# 2024-01-01 15:47:03.330225+00:00 [info] <0.230.0>  home dir       : /var/lib/rabbitmq
# 2024-01-01 15:47:03.330225+00:00 [info] <0.230.0>  config file(s) : /etc/rabbitmq/conf.d/10-defaults.conf
# 2024-01-01 15:47:03.330225+00:00 [info] <0.230.0>  log(s)         : <stdout>
# 2024-01-01 15:47:03.330225+00:00 [info] <0.230.0>  data dir       : /var/lib/rabbitmq/mnesia/rabbit@rmq2

# enter container, exit 13
docker exec -it rabbitmq2 bash



```
## Docker Volums (preferred by Docker containers)

Volumes are a mechanism for storing data outside containers. All volumes are managed by Docker and stored in a dedicated directory on your host, usually /var/lib/docker/volumes for Linux systems.

```bash
# create the volume
docker volume create rabbitmq_data

# create the container
docker run -d --hostname rmq2 --name rabbitmq2 -p 15672:15672 -p 5672:5672 --mount type=volume,src=rabbitmq_data,target=/var/lib/rabbitmq rabbitmq:3.12-management


# veiw
docker volume ls

# remove not associated or used
docker volume prune

# In Docker, a "dangling" volume refers to a volume that is no longer associated with a container.
docker volume rm $(docker volume ls -qf dangling=true)
```
https://follow-e-lo.com/2023/12/30/docker-volume-data-move/

## Dockerfile

Dockerfile

https://github.com/spawnmarvel/learning-docker/blob/main/README-1-dockerfile-reference

Layers

When you run a build, the builder attempts to reuse layers from earlier builds. 

If a layer of an image is unchanged, then the builder picks it up from the build cache. 

If a layer has changed since the last build, that layer, and all layers that follow, must be rebuilt.

```bash

FROM
WORKDIR
COPY
RUN download
COPY . .
RUN use the download
RUN
ENTRYPOINT ["PATH OR FILE", ARGS]
```

https://docs.docker.com/build/guide/layers/#:~:text=The%20order%20of%20Dockerfile%20instructions,layers%20in%20a%20container%20image

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






