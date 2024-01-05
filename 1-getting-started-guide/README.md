
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
docker run -dp 0.0.0.0:3000:3000 getting-started

# hm, had to change to private ip in cloud (it has a public ip, but the 127.0.0.1 was no resolving)
docker rm containername --force

docker run -dp 0.0.0.0:3000:3000 getting-started

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

docker run --name getst -dp 0.0.0.0:3000:3000 getting-started

# result after visit http://publicip:3000
# You have no todo items yet! Add one above!

# the old container was not running, so success.
# Lets do the update and build if the old container is running
# You have no todo items yet(2)! Add one above!

docker build -t getting started .

docker run --name getst -dp 0.0.0.0:3000:3000 getting-started
# docker: Error response from daemon: Conflict. The container name "/getst" is already in use by container "afd0

# remove the old container
docker ps

docker rm afd086d8eb3e --force

cd getting-started

docker build -t getting started .

docker run --name getst -dp 0.0.0.0:3000:3000 getting-started

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

![Docker hub create repos](https://github.com/spawnmarvel/learning-docker/blob/main/images/dockerrepos.jpg)

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
docker push usernamedocker/getting-started

```

![Build pushed](https://github.com/spawnmarvel/learning-docker/blob/main/images/pushed.jpg)


Pull it and start it

```bash
docker login -u usernamedocker

docker pull username/getting-started
# Using default tag: latest
# latest: Pulling from usernamedocker/getting-started
# Digest: sha256:f82bde5fe25275ad4c05d21008240bd739418788a9423d3335299c4d706a2226
# Status: Image is up to date for usernamedocker/getting-started:latest
# docker.io/usernamedocker/getting-started:latest

docker run -dp 0.0.0.0:3000:3000 username/getting-started

# result after visit http://publicip:3000
# You have no todo items yet! Add one above!

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

With the previous experiment, you saw that each container starts from the image definition each time it starts.

While containers can create, update, and delete files, those changes are lost when you remove the container and Docker isolates all changes to that container. 

With volumes, you can change all of this.

Volumes provide the ability to connect specific filesystem paths of the container back to the host machine. 

If you mount a directory in the container, changes in that directory are also seen on the host machine. 

If you mount that same directory across container restarts, you'd see the same files.

**There are two main types of volumes. You'll eventually use both, but you'll start with volume mounts.**


By default, the todo app stores its data in a SQLite database at /etc/todos/todo.db in the container's filesystem.

```bash
# get container id
docker ps -a

# start it
docker start dcbc57bca889

# verify it visit http://public.ip:3000
```

![App no volume ](https://github.com/spawnmarvel/learning-docker/blob/main/images/app_no_volum.jpg)


It's simply a relational database that stores all the data in a single file.

While this isn't the best for large-scale applications, it works for small demos. 

You'll learn how to switch this to a different database engine later.

With the database being a single file, if you can persist that file on the host and make it available to the next container, it should be able to pick up where the last one left off. 

By creating a volume and attaching (often called "mounting") it to the directory where you stored the data, you can persist the data.

```bash
# Create a volume by using the docker volume create command.
docker volume create todo-db

# view it
docker volume ls

# stop and remove the app
docker rm -f dcbc57bca889

# Start the todo app container, but add the --mount option to specify a volume mount. 
# Give the volume a name, and mount it to /etc/todos in the container, which captures all files created at the path
# By default, the todo app stores its data in a SQLite database at /etc/todos/todo.db in the container's filesystem.
docker run -dp 0.0.0.0:3000:3000 --mount type=volume,src=todo-db,target=/etc/todos getting-started


```

Verify that the data persists

```bash
# verify it visit http://public.ip:3000

# Once the container starts up, open the app and add a few items to your todo list: dinner, training

# get id
docker ps
# remove it
docker rm -f 

# Start a new container using the previous steps.
docker run -dp 0.0.0.0:3000:3000 --mount type=volume,src=todo-db,target=/etc/todos getting-started

# verify it visit http://public.ip:3000
# Open the app. You should see your items still in your list: dinner, training

# You've now learned how to persist data.

```

![App volume ](https://github.com/spawnmarvel/learning-docker/blob/main/images/app_volum.jpg)

Where is Docker storing my data when I use a volume?

```bash
docker volume inspect todo-db

[
    {
        "CreatedAt": "2023-12-29T17:06:14Z",
        "Driver": "local",
        "Labels": null,
        "Mountpoint": "/var/lib/docker/volumes/todo-db/_data",
        "Name": "todo-db",
        "Options": null,
        "Scope": "local"
    }
]

# The Mountpoint is the actual location of the data on the disk. 
# Note that on most machines, you will need to have root access to access this directory from the host.

sudo su -

cd

pwd
# /var/lib/docker/volumes/todo-db/_data

```

https://docs.docker.com/get-started/05_persisting_data/

## Extra 2 get to know docker volume (and move /var/lib/docker)

https://github.com/spawnmarvel/learning-docker/blob/main/1-getting-started-guide/README-2-docker-volume.md

## Part 6 Use bind mounts

Note: moved /var/lib/docker to E, so make the volume again for the todo-app.

Build it, node.js app

```bash
# docker rm, rmi, remove container, image, volume before start

docker volume create todo-db

cd getting-started-app

ls
# Dockerfile  README.md  package.json  spec  src  yarn.lock

# build image
docker build -t getting-started

docker images
# REPOSITORY                 TAG               IMAGE ID       CREATED          SIZE
# getting-started            latest            cfc8068d5338   21 minutes ago   223MB

cd ..

# we can now run the image and make a container, or many
docker run -dp 0.0.0.0:3000:3000 --mount type=volume,src=todo-db,target=/etc/todos getting-started

# visit http://publicip:3000 and add two itmes
# then restart container and verify items

# view it
docker ps

# you can now stop and start the container with a volume
# or set it to always run
docker restart, stop, start getting-started
```

Pull it, rabbitmq

```bash

# create the volume
docker volume create rabbitmq_data

# create the container
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

In part 5, you used a volume mount to persist the data in your database. A volume mount is a great choice when you need somewhere persistent to store your application data.

A bind mount is another type of mount, which lets you share a directory from the host's filesystem into the container. 

When working on an application, you can use a bind mount to mount source code into the container. 

The container sees the changes you make to the code immediately, as soon as you save a file. 

This means that you can run processes in the container that watch for filesystem changes and respond to them.


Trying out bind mounts

```bash
cd getting-started-app

# Run the following command to start bash in an ubuntu container with a bind mount.
docker run -it --mount type=bind,src="$(pwd)",target=/src ubuntu bash

# The --mount option tells Docker to create a bind mount, 
# where src is the current working directory on your host machine (getting-started-app), 
# and target is where that directory should appear inside the container (/src)

# After running the command, Docker starts an interactive bash session in the root directory of the container's filesystem.
cd src

# This is the directory that you mounted when starting the container. Listing the contents of this directory displays the same files as in the getting-started-app directory on your host machine.

ls
# Dockerfile  README.md  package.json  spec  src  yarn.lock

# Create a new file named myfile.txt
touch myfile.txt

# Open the getting-started-app directory on the host and observe that the myfile.txt file is in the directory.
cd getting-started-app/

ls 
# Dockerfile  README.md  myfile.txt  package.json  spec  src  yarn.lock

# From the host, delete the myfile.txt file.
# and it is gone from the container

# exit
ctrl + d

```
That's all for a brief introduction to bind mounts. 

This procedure demonstrated how files are shared between the host and the container, and how changes are immediately reflected on both sides. 

Now you can use bind mounts to develop software.

Development containers

Using bind mounts is common for local development setups. 

The advantage is that the development machine doesn’t need to have all of the build tools and environments installed. 

With a single docker run command, Docker pulls dependencies and tools.

The following steps describe how to run a development container with a bind mount that does the following:

* Mount your source code into the container
* Install all dependencies
* Start nodemon to watch for filesystem changes

```bash
# Run your app in a development container

cd getting-started

docker run -dp 0.0.0.0:3000:3000 \
    -w /app --mount type=bind,src="$(pwd)",target=/app \
    node:18-alpine \
    sh -c "yarn install && yarn run dev"

docker ps
# CONTAINER ID   IMAGE       
# 4ab56afc944d   node:18-alpine

```

* -dp 00.0.0.1:3000:3000 - same as before. Run in detached (background) mode and create a port mapping
* -w /app - sets the "working directory" or the current directory that the command will run from
* --mount type=bind,src="$(pwd)",target=/app - bind mount the current directory from the host into the /app directory in the container
* node:18-alpine - the image to use. Note that this is the base image for your app from the Dockerfile
* sh -c "yarn install && yarn run dev" - the command. You're starting a shell using sh (alpine doesn't have bash) and running yarn install to install packages and then running yarn run dev to start the development server. If you look in the package.json, you'll see that the dev script starts nodemon.

```bash

# You can watch the logs using docker logs <container-id>. You'll know you're ready to go when you see this:
# Using sqlite database at /etc/todos/todo.db
# Listening on port 3000

# Update your app on your host machine and see the changes reflected in the container.

# In the src/static/js/app.js file, on line 109, change the "Add Item" button to simply say "Add":

# Refresh the page in your web browser, and you should see the change reflected almost immediately because of the bind mount.

# Feel free to make any other changes you'd like to make. Each time you make a change and save a file, the change is reflected in the container because of the bind mount. 

# When Nodemon detects a change, it restarts the app inside the container automatically. When you're done, stop the container and build your new image using:

docker build -t getting-started .

```
https://docs.docker.com/get-started/06_bind_mounts/
 
## Part 7 Multi-container apps

Up to this point, you've been working with single container apps. But, now you will add MySQL to the application stack.

Todo App - - > MySQL (Two containers)

Container networking

**Remember that containers, by default, run in isolation and don't know anything about other processes or containers on the same machine.**

**So, how do you allow one container to talk to another? The answer is networking. If you place the two containers on the same network, they can talk to each other.**

Two ways

* Assign the network when starting the container.
* Connect an already running container to a network.


```bash

# Create the network.
docker network create todo-app

# view it
docker network ls
# NETWORK ID     NAME       DRIVER    SCOPE
# 39dd833844aa   todo-app   bridge    local

# Start a MySQL container and attach it to the network.
# -v volume
# -e environment vars
docker run -d \
    --network todo-app --network-alias mysql \
    -v todo-mysql-data:/var/lib/mysql \
    -e MYSQL_ROOT_PASSWORD=secret \
    -e MYSQL_DATABASE=todos \
    mysql:8.0

# In the previous command, you can see the --network-alias flag. In a later section, you'll learn more about this flag

# view it
docker ps
# CONTAINER ID   IMAGE       COMMAND                  CREATED         STATUS         PORTS                 NAMES
# 09d7dc5082ee   mysql:8.0   "docker-entrypoint.s…"   9 seconds ago   Up 7 seconds   3306/tcp, 33060/tcp   kind_pike

# get ip
docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' 09d7dc5082ee
ip=$(docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' 09d7dc5082ee)

# connect to mysql if you have the mysql-client installed
mysql -h $ip -u root -p

# or
docker exec -it 09d7dc5082ee mysql -u root -p

```

Connect to MySQL

Now that you know MySQL is up and running, you can use it. But, how do you use it? If you run another container on the same network, how do you find the container? 

Remember that each container has its own IP address.

```bash
# some mysql images for test
# Start a new container using the nicolaka/netshoot image. Make sure to connect it to the same network.
docker run -it --network todo-app nicolaka/netshoot

# and we are inside the container on the fly

# Inside the container, you're going to use the dig command, which is a useful DNS tool. You're going to look up the IP address for the hostname mysql
dig mysql

# In the "ANSWER SECTION", you will see an A record for mysql that resolves to 172.23.0.2 (your IP address will most likely have a different value). 
# While mysql isn't normally a valid hostname, Docker was able to resolve it to the IP address of the container that had that network alias. 

# Remember, you used the --network-alias earlier.
# ;; ANSWER SECTION:
# mysql.			600	IN	A	172.23.0.2

# What this means is that your app only simply needs to connect to a host named mysql and it'll talk to the database.

```

Run your app with MySQL

The todo app supports the setting of a few environment variables to specify MySQL connection settings. They are:

* MYSQL_HOST - the hostname for the running MySQL server
* MYSQL_USER - the username to use for the connection
* MYSQL_PASSWORD - the password to use for the connection
* MYSQL_DB - the database to use once connected


NOTE!
**While using env vars to set connection settings is generally accepted for development, it's highly discouraged when running applications in production.**

**Diogo Monica, a former lead of security at Docker, wrote a fantastic blog post explaining why.**

https://blog.diogomonica.com//2017/03/27/why-you-shouldnt-use-env-variables-for-secret-data/


A more secure mechanism is to use the secret support provided by your container orchestration framework. 

In most cases, these secrets are mounted as files in the running container. 

You'll see many apps (including the MySQL image and the todo app) also support env vars with a _FILE suffix to point to a file containing the variable.

As an example, setting the MYSQL_PASSWORD_FILE var will cause the app to use the contents of the referenced file as the connection password. 

Docker doesn't do anything to support these env vars. Your app will need to know to look for the variable and get the file contents.

```bash

# Make sure that you are in the getting-started-app directory when you run this command
cd getting-started

# You can now start your dev-ready container.
docker run -dp 127.0.0.1:3000:3000 \
  -w /app -v "$(pwd):/app" \
  --network todo-app \
  -e MYSQL_HOST=mysql \
  -e MYSQL_USER=root \
  -e MYSQL_PASSWORD=secret \
  -e MYSQL_DB=todos \
  node:18-alpine \
  sh -c "yarn install && yarn run dev"

# view it
docker ps
# CONTAINER ID   IMAGE            COMMAND                  CREATED         STATUS         PORTS                      NAMES
# e535cb0d78dc   node:18-alpine   "docker-entrypoint.s…"   7 seconds ago   Up 6 seconds   127.0.0.1:3000->3000/tcp   stupefied_gagarin

# rm it, can not visit 172.0.0.1
docker rm -f e535cb0d78dc


# sisnce it was day to, we have to run the mysql again....it depends on that.....well well, we are learning
# after inspecting logs
docker logs 7fe5210a5a21
# [nodemon] starting `node src/index.js`
# Waiting for mysql:3306.......
# Timeout
# Error: connect ETIMEDOUT

# make mysql container run
docker run -d \
    --network todo-app --network-alias mysql \
    -v todo-mysql-data:/var/lib/mysql \
    -e MYSQL_ROOT_PASSWORD=secret \
    -e MYSQL_DATABASE=todos \
    mysql:8.0

# You can now start your dev-ready container.
docker run -dp 3000:3000 \
  -w /app -v "$(pwd):/app" \
  --network todo-app \
  -e MYSQL_HOST=mysql \
  -e MYSQL_USER=root \
  -e MYSQL_PASSWORD=secret \
  -e MYSQL_DB=todos \
  node:18-alpine \
  sh -c "yarn install && yarn run dev"


# view both
docker ps

# If you look at the logs for the container (docker logs -f <container-id>), 
# you should see a message similar to the following, which indicates it's using the mysql database.
docker logs 202c110e81a2
# Waiting for mysql:3306.
# Connected!
# Connected to mysql db at host mysql
# Listening on port 3000

# To confirm you have the database up and running, connect to the database and verify that it connects.
docker ps

# get the mysql id
docker exec -it 98bac07d1504 mysql -u root -p

# or
ip=$(docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' 98bac07d1504)
mysql -h $ip -u root -p

# Connect to the mysql database and prove that the items are being written to the database. Remember, the password is secret.
docker exec -it 98bac07d1504 mysql -p todos
```

Verify data after adding some items

```sql
mysql> select * from todo_items;

```
![Multi container ](https://github.com/spawnmarvel/learning-docker/blob/main/images/multi_container.jpg)

In the next section, you'll learn about Docker Compose. With Docker Compose, you can share your application stacks in a much easier way and let others spin them up with a single, simple command.

https://docs.docker.com/get-started/07_multi_container/

## Extra 3 get to know docker networking

https://github.com/spawnmarvel/learning-docker/blob/main/1-getting-started-guide/README-3-docker-network.md

## Part 8 Use Docker Compose

Docker Compose is a tool that helps you define and share multi-container applications. 

With Compose, you can create a YAML file to define the services and with a single command, you can spin everything up or tear it all down.

The big advantage of using Compose is you can define your application stack in a file, keep it at the root of your project repository (it's now version controlled), and easily enable someone else to contribute to your project. 

Someone would only need to clone your repository and start the app using Compose. In fact, you might see quite a few projects on GitHub/GitLab doing exactly this now.

```bash

# Create the Compose file
# In the getting-started-app directory, create a file named compose.yaml.
touch compose.yml
```
Define the app service

```bash
docker run -dp 127.0.0.1:3000:3000 \
  -w /app -v "$(pwd):/app" \
  --network todo-app \
  -e MYSQL_HOST=mysql \
  -e MYSQL_USER=root \
  -e MYSQL_PASSWORD=secret \
  -e MYSQL_DB=todos \
  node:18-alpine \
  sh -c "yarn install && yarn run dev"

```
You'll now define this service in the compose.yaml file.

```yml
services:
  app:
    image: node:18-alpine
    command: sh -c "yarn install && yarn run dev"
    ports:
      - 127.0.0.1:3000:3000
    working_dir: /app
    volumes:
      - ./:/app
    environment:
      MYSQL_HOST: mysql
      MYSQL_USER: root
      MYSQL_PASSWORD: secret
      MYSQL_DB: todos
```
Define the MySQL service

```bash
# Now, it's time to define the MySQL service. The command that you used for that container was the following:

docker run -d \
  --network todo-app --network-alias mysql \
  -v todo-mysql-data:/var/lib/mysql \
  -e MYSQL_ROOT_PASSWORD=secret \
  -e MYSQL_DATABASE=todos \
  mysql:8.0

```

```yml
services:
  app:
    # The app service definition
  mysql:
    image: mysql:8.0
    volumes:
      - todo-mysql-data:/var/lib/mysql
    environment:
      MYSQL_ROOT_PASSWORD: secret
      MYSQL_DATABASE: todos

volumes:
  todo-mysql-data:

```
At this point, your complete compose.yaml should look like this:

```yml
services:
  app:
    image: node:18-alpine
    command: sh -c "yarn install && yarn run dev"
    ports:
      - 3000:3000
    working_dir: /app
    volumes:
      - ./:/app
    environment:
      MYSQL_HOST: mysql
      MYSQL_USER: root
      MYSQL_PASSWORD: secret
      MYSQL_DB: todos

  mysql:
    image: mysql:8.0
    volumes:
      - todo-mysql-data:/var/lib/mysql
    environment:
      MYSQL_ROOT_PASSWORD: secret
      MYSQL_DATABASE: todos

volumes:
  todo-mysql-data:
```

Run the application stack
```bash
# remove all copies of running containers
docker ps
docker rm f id

# start it
cd getting-started-app
docker compose up -d

# Look at the logs using the docker compose logs -f command. You'll see the logs from each of the services interleaved into a single stream.
docker compose logs -f

# Tear it all down
docker compose down

# If you want to remove the volumes, you need to add the --volumes flag.
```

Note:

By default, named volumes in your compose file are not removed when you run docker compose down. If you want to remove the volumes, you need to add the --volumes flag.

https://docs.docker.com/get-started/08_using_compose/

## Extra 4 get to know docker compose

https://github.com/spawnmarvel/learning-docker/blob/main/1-getting-started-guide/README-4-docker-compose.md

## Part 9 Image-building Best practices

https://docs.docker.com/get-started/09_image_best/

## Part 10 What next

https://docs.docker.com/guides/get-started/