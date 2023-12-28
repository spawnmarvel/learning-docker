
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


```

## Part 3 Update the application

## Part 4 Share the application

## Part 5 Persist the DB

## Part 6 Use bind mounts
 
## Part 7 Multi-container apps

## Part 8 Use Docker Compose

## Part 9 Image-building Best practices

## Part 10 What next

https://docs.docker.com/guides/get-started/