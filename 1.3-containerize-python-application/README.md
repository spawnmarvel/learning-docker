# Python as container


## Visuals

https://follow-e-lo.com/2024/01/29/containerize-a-python-application-docker/

## Containerize a Python application

The app is ready to clone in github or you have the code local.

We have it local.

```bash
cp python-boilerplate
cd python-boilerplate

python app.py
python3 app.py
```
Logs

```logs
2024-02-02 20:23:32,726 - 30640 - 2380 - app.py - 11 -             <module>() root - INFO - Version 0.1
2024-02-02 20:23:32,726 - 30640 - 2380 - app.py - 33 -             <module>() root - INFO - In main
2024-02-02 20:23:32,727 - 30640 - 2380 - app.py - 39 -             <module>() root - INFO - Main Pid: 2380
2024-02-02 20:23:34,731 - 30640 - 2380 - worker.py - 16 -              do_work() root - INFO - Sleeping....
2024-02-02 20:23:36,737 - 30640 - 2380 - worker.py - 16 -              do_work() root - INFO - Sleeping....
2024-02-02 20:23:38,752 - 30640 - 2380 - worker.py - 16 -              do_work() root - INFO - Sleeping....
2024-02-02 20:23:40,765 - 30640 - 2380 - worker.py - 16 -              do_work() root - INFO - Sleeping....
2024-02-02 20:23:42,038 - 30640 - 2380 - app.py - 42 -             <module>() root - INFO - Stop command recieved
2024-02-02 20:23:43,041 - 30640 - 2380 - app.py - 44 -             <module>() root - INFO - Cleaning up
2024-02-02 20:23:43,041 - 30640 - 2380 - app.py - 45 -             <module>() root - INFO - Stopped, bye, bye
```


### Initialize Docker assets

Now that we have the application we need to a Dockerfile and compose.yml.

We will wait a bit with compose and take it further down.

Login to a server with docker.

```bash

ssh user@ip

mkdir python-boilerplate

cp python-boilerplate

cd python-boilerplate

ls
# app.py  app_logger.py  logging_config.ini  worker.py  requirements.txt

touch Dockerfile

```
Dockerfile

```bash
ls

Dockerfile  app.py  app_logger.py  logging_config.ini  requirements.txt  worker.py

# Dockerfile
FROM python:3.10-slim-buster
ADD . /code
WORKDIR /code
RUN pip3 install -r requirements.txt
CMD [ "python", "./app.py" ]

```

## Now make the docker container with image build

```bash

# build 
cd python-boilerplate

docker image build -t python-boiler .

# good for debugging to see that it works
# Run it, --rm removed on stop or ctrl c, -tag tag
docker run --name python-test --rm -t python-boiler

# good when you are done with debugging
# Run it, --d detached in background for ever instead of opening a new terminal
docker run --name python-test -d -t python-boiler

docker ps

docker exec -it python-boiler bash

```

The docker build command builds Docker images from a Dockerfile and a "context". A build's context is the set of files located in the specified PATH or URL. The build process can refer to any of the files in the context.

https://docs.docker.com/engine/reference/commandline/image_build/#:~:text=The%20docker%20build%20command%20builds,the%20specified%20PATH%20or%20URL%20.


https://docs.docker.com/get-started/02_our_app/

## Update the application

```bash
# view it
docker images

# edit worker.py
# logger.info("Sleeping....")
# logger.info("Sleeping long tomorrow....")

# remove it
docker rmi 5c8089f9ef31 --force

# re build it
docker image build -t python-boiler .

# good for debugging to see that it works
# Run it, --rm removed on stop or ctrl c, -tag tag
docker run --name python-test --rm -t python-boiler

# good when you are done with debugging
# Run it, --d detached in background for ever instead of opening a new terminal
docker run --name python-test -d -t python-boiler

docker ps

docker exec -it python-test bash

```
https://docs.docker.com/get-started/03_updating_app/

## Share the application create a repository and push


1. Sign up or Sign in to Docker Hub.

https://hub.docker.com/

2. Select the Create Repository button.

3. For the repository name, use python-boiler. Make sure the Visibility is Public.

Select Create.

```bash
# docker repos
YOUR-USER-NAME/python-boiler

```


Sign in to private docker to get your repository.


```bash

cd python-boiler

# if we are good, then build it
docker image build -t python-boiler .

# good for debugging to see that it works
# Run it, --rm removed on stop or ctrl c, -tag tag
docker run --name python-test --rm -t python-boiler

# your username
docker login -u espenkle

# Use the docker tag command to give the python-boiler image a new name. Replace YOUR-USER-NAME with your Docker ID.
docker tag python-boiler espenkle/python-boiler

# push the images
docker push espenkle/python-boiler

```
https://docs.docker.com/get-started/04_sharing_app/

## Pull and run a container image from Docker Hub


```bash
# In your terminal, run docker pull espenkle/python-boiler to pull the image from Docker Hub. 
# You should see output similar to:
docker pull espenkle/python-boiler

# Using default tag: latest
# latest: Pulling from espenkle/python-boiler
# Digest: sha256:715d5fd5a6b6a096cff0ac5db2ec10dae4993ddc58b8c3bac73fd5b3afec3ec1
# Status: Image is up to date for espenkle/python-boiler:latest
# docker.io/espenkle/python-boiler:latest

docker image ls

#  docker image ls
# REPOSITORY               TAG       IMAGE ID       CREATED        SIZE
# espenkle/python-boiler   latest    5917cf27bc1d   14 hours ago   130MB
# python-boiler            latest    5917cf27bc1d   14 hours ago   130MB

# run it
docker run espenkle/python-boiler
```

## Update the image on docker hub

```bash
# view it
docker images

# edit worker.py
# logger.info("Sleeping long tomorrow....")
# logger.info("Sleeping long tomorrow also....")

# test it
python3 app.py

# remove the old image
dokcker image ls

docker rmi '<ID>' --force

# re build it
docker image build -t python-boiler .

# good for debugging to see that it works
# Run it, --rm removed on stop or ctrl c, -tag tag
docker run --name python-test --rm -t python-boiler

# Use the docker tag command to give the python-boiler image a new name. Replace YOUR-USER-NAME with your Docker ID.
docker tag python-boiler espenkle/python-boiler

# push the images
docker push espenkle/python-boiler

# pull it
docker pull espenkle/python-boiler

# run it
docker run espenkle/python-boiler


```
logs

```logs
2024-02-03 10:38:41,203 - 140357808113472 - 1 - app.py - 12 -             <module>() root - INFO - Version 0.1
2024-02-03 10:38:41,203 - 140357808113472 - 1 - app.py - 35 -             <module>() root - INFO - In main
2024-02-03 10:38:41,203 - 140357808113472 - 1 - app.py - 41 -             <module>() root - INFO - Main Pid: 1
2024-02-03 10:38:43,205 - 140357808113472 - 1 - worker.py - 15 -              do_work() root - INFO - Sleeping long tomorrow also....

```
https://docs.docker.com/docker-hub/quickstart/


## Use Docker Compose

```bash

docker rmi -f espenkle/python-boiler
docker rmi -f python-boiler
# not the latest it only at docker hub

#TBD
```


https://docs.docker.com/get-started/08_using_compose/







