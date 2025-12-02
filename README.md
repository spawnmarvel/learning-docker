# Learning-docker
Testing and learning Docker with Azure

![docker](https://github.com/spawnmarvel/learning-docker/blob/main/images/docker.png)

## Learning docker


What do we get extra here:

* Python for programming
* Bash and linux, ssh, .sh scripts
* Azure VM with Docker, NSG, (mount data drive, not not this time)
* Azure Container with Docker
* Azure Container registry with Docker
* Github actions and runners in the DevOps part

Azure resources

![Azure resources](https://github.com/spawnmarvel/learning-docker/blob/main/images/azure_resources2.jpg)


Azure Resource visualizer

![Azure resources visual](https://github.com/spawnmarvel/learning-docker/blob/main/images/azure_visual.png)


## Docker: be efficient

https://follow-e-lo.com/2024/01/14/docker-be-efficient/

## Visuals

https://follow-e-lo.com/category/docker/

# Phase 1: Master Docker Fundamentals

## 1 Getting started guide CLI

* docker run
* docker volume
* docker newtwork
* docker compose
* docker build

https://github.com/spawnmarvel/learning-docker/blob/main/1-getting-started-guide/README.md

All sections

![Tutorials](https://github.com/spawnmarvel/learning-docker/blob/main/images/tutorials.jpg)

## 1.1 What are containers and docker

https://github.com/spawnmarvel/learning-docker/blob/main/1.1-what-are-containers-john-s/Examples.sh

All examples bash

https://github.com/spawnmarvel/learning-docker/blob/main/1-what-are-containers-john-s/Examples.sh


## 1.2 Dockerlabs

For notes view readme

https://github.com/spawnmarvel/learning-docker/tree/main/1.2-dockerlabs


## Docker docs

Docker Engine is an open source containerization technology for building and containerizing your applications

https://docs.docker.com/engine/

## Installing Docker on a VM (Azure) (Done 2)

Update vm tbd

Get the latest install script

https://docs.docker.com/engine/install/ubuntu/


```bash
# update vm
sudo apt update -y

sudo apt upgrade -y

```
Create script

```bash

# create script
touch add_docker_repository_to_apt.sh

nano add_docker_repository_to_apt.sh

```
add_docker_repository_to_apt.sh

```bash
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
sudo bash add_docker_repository_to_apt.sh

```

Install the Docker packages

```bash
sudo apt install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

Verify versions docker and compose

```bash
docker --version
# Docker version 29.0.3, build 511dad6

docker compose version
# Docker Compose version v2.40.3
```

Run hello-world

```bash
sudo docker run hello-world
# docker: permission denied while trying to connect to the docker API at unix:///var/run/docker.sock
# go to user setup section
```

https://docs.docker.com/engine/install/ubuntu/

## Mount disk on VM (Done 2)

* cd /datadrive/

https://github.com/spawnmarvel/learning-docker/blob/main/README-0-mount.md


## Docker user setup (Done 2)

```bash
# login
ssh user@IP

# From above we ised sudo in front of docker, result without
docker run hello-world
# docker: permission denied while trying to connect to the Docker daemon socket

# Check if docker groups is present
getent group
# docker:x:988:

getent group | grep docker
# docker:x:999:

# check if a user is in a group
id the_username
# we see groups

# Add the connected user the_username to the docker group. Change the user name to match your preferred user if you do not want to use your current user:

sudo usermod -aG docker the_username
# Adding user username to group docker

id the_username
# we seee groups and now the 988(docker)

# Activate, either do a newgrp docker or log out/in to activate the changes to groups.
newgrp docker

# Now run
docker run hello-world
# Hello from Docker!
# This message shows that your installation appears to be working correctly.

```

## Docker move /var/lib/docker (Done 2)

The standard data location used for docker is /var/lib/docker. Because this directory contains all containers/images/volumes, it can be large.

So we mounted a data disk.


```bash
lsblk

# [...]
sdc       8:32   0    4G  0 disk
└─sdc1    8:33   0    4G  0 part /datadrive

sudo systemctl stop docker.socket
sudo systemctl status docker.socket

cd /etc/docker
sudo nano daemon.json

```

daemon.json (set data drive path)

```json
{
   "data-root": "/datadrive"
}
```

Copy all files

```bash
sudo rsync -aP /var/lib/docker/ /datadrive

sudo su
cd /datadrive
ls

docker run hello-world

# Hello from Docker!
# This message shows that your installation appears to be working correctly.
```


https://github.com/spawnmarvel/learning-docker/blob/main/1-getting-started-guide/README-2-docker-volume.md#docker-volume-data-move

## Set up portainer https (Done 2)


First UFW and also add NSG for http/https

```bash
sudo ufw show added
Added user rules (see 'ufw status' for running firewall):
ufw allow 22/tcp
ufw allow 9000/tcp
ufw allow 9443/tcp
ufw allow 443

sudo ufw enable

```

check status

```bash
sudo ufw status verbose
```

Log

```log
Status: active
Logging: on (low)
Default: deny (incoming), allow (outgoing), deny (routed)
New profiles: skip

To                         Action      From
--                         ------      ----
22/tcp                     ALLOW IN    Anywhere
443                        ALLOW IN    Anywhere
9000                       ALLOW IN    Anywhere
9443                       ALLOW IN    Anywhere
22/tcp (v6)                ALLOW IN    Anywhere (v6)
443 (v6)                   ALLOW IN    Anywhere (v6)
9000 (v6)                  ALLOW IN    Anywhere (v6)
9443 (v6)                  ALLOW IN    Anywhere (v6)

```

Go to how to

https://github.com/spawnmarvel/learning-docker/blob/main/prod-ish-2/portainer/README.md


## Failed container? Well check logs

```bash
docker compose logs portainer

```

Container is build success, but restarting.

![container restarting](https://github.com/spawnmarvel/learning-docker/blob/main/images/restarting.png)

Build success
![container restarting](https://github.com/spawnmarvel/learning-docker/blob/main/images/container_restarting.png)




## Repeat the 1 Getting started guide

You have done it before, but do the link all over again https://docs.docker.com/get-started/ and store it in:

* 1-getting-started-guide-repeat, you dont need to write mych down, just repeat it and store sections for how far you are.

##

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

## AI what is the difference between dockerfile and compose file, and if you use both, what should go where?

A Dockerfile is a text document that contains a set of instructions used to build a Docker image. It acts as a blueprint for creating containers, defining the environment and dependencies required for your application to run.

Dockerfile: Use for building individual images representing a single component or service.


A Docker Compose file (typically named compose.yml) is used to define and manage multi-container Docker applications. It allows you to declare services, networks, and volumes in a declarative way using YAML syntax.

* Multi-Container Management: Orchestrates the deployment and interaction of multiple containers.
* Service Definition: Defines services (which are essentially containers based on images) that make up the application.
* Networking: Manages container networking, allowing services to communicate with each other.
* Volumes: Defines persistent storage volumes for data management.
* Environment Configuration: Provides a way to manage environment variables and other configurations.
* Simplified Management: Offers a simple command-line interface for managing the entire application lifecycle (start, stop, build).

Docker Compose: Use for defining and managing the interconnections and configurations of a multi-container application.


## Dockerfile

Dockerfile

Example

* FROM	    Create a new build stage from a base image.
* COPY	    Copy files and directories.
* RUN	        Execute build commands.

https://github.com/spawnmarvel/learning-docker/blob/main/README-1-dockerfile-reference

Example amqp

```bash
FROM rabbitmq:3.13-management
COPY rabbitmq.conf /etc/rabbitmq
RUN rabbitmq-plugins enable --offline rabbitmq_shovel && rabbitmq-plugins enable --offline rabbitmq_shovel_management

```

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

## Modify your Compose file for production

https://docs.docker.com/compose/how-tos/production/

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


## 1.3 Containerize a Python application

https://github.com/spawnmarvel/learning-docker/blob/main/2-azure-container-instance/Readme.md

## 1.4 Azure Container Registry

https://github.com/spawnmarvel/learning-docker/blob/main/1.4-azure-container-instance/Readme-container-registry.md

# 2 Azure devops

Go to devops readme after you are done with ## Phase 1: Master Docker Fundamentals

https://github.com/spawnmarvel/learning-docker/blob/main/README-devops.md












