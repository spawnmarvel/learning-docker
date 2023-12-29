
# Getting started guide CLI

## Part 1 Overview

* Build and run an image as a container.
* Share images using Docker Hub
* Deploy Docker applications using multiple containers with a database
* Run applications using Docker Compose

What is a container

* Isolated from all other processes.
* That isolation leverages kernel namespaces and cgroups, features that have been in Linux for a long time.

What is an image

* This isolated filesystem, dependencies, scripts etc.

https://docs.docker.com/get-started/

## Part 2 Containerize an application


Prerequisites

* You have installed the latest version of Docker Desktop = Engine
* You have installed a Git client
* You have an IDE or a text editor to edit files. Docker recommends using Visual Studio Code

Can use sftp for transfer

![Azure resources](https://github.com/spawnmarvel/learning-docker/blob/main/images/filezilla2.jpg)

Get the app

```bash

git version
# git version 2.34.1

docker --version / version
# Client: Docker Engine - Community
# Version:           24.0.7

docker compose version
# Docker Compose version v2.21.0

git clone https://github.com/docker/getting-started-app.git

```
Build the app's images

* We need Dockerfile

```bash
cd getting-started-app

touch Dockerfile

# syntax=docker/dockerfile:1

FROM node:18-alpine
WORKDIR /app
COPY . .
RUN yarn install --production
CMD ["node", "src/index.js"]
EXPOSE 3000

# build the image
docker build -t getting-started .

docker images

# REPOSITORY        TAG       IMAGE ID       CREATED          SIZE
# getting-started   latest    00767b2de32f   10 minutes ago   223MB


```
* The docker build command uses the Dockerfile to build a new image
* After Docker downloaded the image (node:18-alpine)
*  the instructions from the Dockerfile copied in your application and used yarn to install your application's dependencies. 
* The CMD directive specifies the default command to run when starting a container from this image.
* Finally, the -t flag tags your image.
* The . at the end of the docker build command, look current directory

Start an app container

```bash

# start an app
# The -d flag (short for --detach) runs the container in the background.
# The -p flag (short for --publish) creates a port mapping between the host and the container. 
# The -p flag takes a string value in the format of HOST:CONTAINER, where HOST is the address on the host, 
# and CONTAINER is the port on the container. 
# The command publishes the container's port 3000 to 127.0.0.1:3000 (localhost:3000) on the host.
docker run -dp 127.0.0.1:3000:3000 getting-started

# hm, had to change to private ip in cloud (it has a public ip, but the 127.0.0.1 was no resolving)
docker rm containername --force

docker run -dp 192.168.3.4:3000:3000 getting-started

# http://public-ip:3000/

# add an item in the todo list: dinner, sleep

# Run the following docker ps command in a terminal to list your containers.
docker ps

docker stop containername

```
https://docs.docker.com/get-started/02_our_app/

## Extra 1 get to know docker run

https://github.com/spawnmarvel/learning-docker/blob/main/1-getting-started-guide/README-1-docker-run.md

## Part 3 Update the application

In part 2, you containerized a todo application. In this part, you'll update the application and image. You'll also learn how to stop and remove a container.

```bash
cd getting-started
# updated app.js with: You have no todo...

docker build -t getting started .

docker run --name getst -dp 192.168.3.4:3000:3000 getting-started

# result after visit http://publicip:3000
# You have no todo items yet! Add one above!

# the old container was not running, so success.
# Lets do the update and build if the old container is running
# You have no todo items yet(2)! Add one above!

docker build -t getting started .

docker run --name getst -dp 192.168.3.4:3000:3000 getting-started
# docker: Error response from daemon: Conflict. The container name "/getst" is already in use by container "afd0

# remove the old container
docker ps

docker rm afd086d8eb3e --force

cd getting-started

docker build -t getting started .

docker run --name getst -dp 192.168.3.4:3000:3000 getting-started

# result after visit http://publicip:3000
# You have no todo items yet(2)! Add one above!


```

https://docs.docker.com/get-started/03_updating_app/


## Part 4 Share the application

Now that you've built an image, you can share it. To share Docker images, you have to use a Docker registry. The default registry is Docker Hub and is where all of the images you've used have come from.

1. Sign up or Sign in to Docker Hub.
2. Select the Create Repository button.
3. For the repository name, use getting-started. Make sure the Visibility is Public.
4. Select Create.

![Azure resources](https://github.com/spawnmarvel/learning-docker/blob/main/images/dockerrepos.jpg)

https://hub.docker.com/

```bash
# push
docker push docker/getting-started
# Using default tag: latest
# The push refers to repository [docker.io/docker/getting-started]
# An image does not exist locally with the tag: docker/getting-started

# Why did it fail? The push command was looking for an image named docker/getting-started, but didn't find one. 
# If you run docker image ls, you won't see one either.

# To fix this, you need to tag your existing image you've built to give it another name.

docker login -u username
# success

pwd
/home/username

docker tag getting-started usernamedocker/getting-started

# push it
docker push  usernamedocker/getting-started

```

![Azure resources](https://github.com/spawnmarvel/learning-docker/blob/main/images/pushed.jpg)


Pull it and start it

```bash
docker login -u usernamedocker

docker pull username/getting-started
# Using default tag: latest
# latest: Pulling from usernamedocker/getting-started
# Digest: sha256:f82bde5fe25275ad4c05d21008240bd739418788a9423d3335299c4d706a2226
# Status: Image is up to date for usernamedocker/getting-started:latest
# docker.io/usernamedocker/getting-started:latest


```

https://docs.docker.com/get-started/04_sharing_app/

## Part 5 Persist the DB

In case you didn't notice, your todo list is empty every single time you launch the container. Why is this? In this part, you'll dive into how the container is working.

See this in practice
To see this in action, you're going to start two containers and create a file in each. 

What you'll see is that the files created in one container aren't available in another.

```bash
# Start an ubuntu container that will create a file named /data.txt with a random number between 1 and 10000.
docker run -d ubuntu bash -c "shuf -i 1-10000 -n 1 -o /data.txt && tail -f /dev/null"

docker ps
# Validate that you can see the output by accessing the terminal in the container. 
docker exec a93d357f8557 cat /data.txt
# 1068

# Now, start another ubuntu container (the same image) and you'll see you don't have the same file.
docker run -it ubuntu ls /

# In this case the command lists the files in the root directory of the container. Look, there's no data.txt file there! That's because it was written to the scratch space for only the first container.

```

Container volumes

With the previous experiment, you saw that each container starts from the image definition each time it starts. While containers can create, update, and delete files, those changes are lost when you remove the container and Docker isolates all changes to that container. 

With volumes, you can change all of this.

Volumes provide the ability to connect specific filesystem paths of the container back to the host machine. 

If you mount a directory in the container, changes in that directory are also seen on the host machine. 

If you mount that same directory across container restarts, you'd see the same files.

There are two main types of volumes. You'll eventually use both, but you'll start with volume mounts.


By default, the todo app stores its data in a SQLite database at /etc/todos/todo.db in the container's filesystem.

```bash
# get container id
docker ps -a

# start it
docker start dcbc57bca889

# verify it visit http://public.ip:3000
```

![Azure resources](https://github.com/spawnmarvel/learning-docker/blob/main/images/app-no-volum.jpg)

https://docs.docker.com/get-started/05_persisting_data/

## Extra 2 get to know docker volume

https://github.com/spawnmarvel/learning-docker/blob/main/1-getting-started-guide/README-2-docker-volume.md

## Part 6 Use bind mounts
 
## Part 7 Multi-container apps

## Part 8 Use Docker Compose

## Part 9 Image-building Best practices

## Part 10 What next

https://docs.docker.com/guides/get-started/