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

Now that we have the application we can use docker init.

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

docker image build -t python-boil .

# good for debugging to see that it works
# Run it, --rm removed on stop or ctrl c, -t tag
docker run --name python-test --rm -t python-boil

# good when you are done with debugging
# Run it, --d detached in background for ever instead of opening a new terminal
docker run --name python-test -d -t python-boil

docker ps

docker exec -it python-test bash

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
docker image build -t python-boil .

# good for debugging to see that it works
# Run it, --rm removed on stop or ctrl c, -t tag
docker run --name python-test --rm -t python-boil

# good when you are done with debugging
# Run it, --d detached in background for ever instead of opening a new terminal
docker run --name python-test -d -t python-boil

docker ps

docker exec -it python-test bash

```
https://docs.docker.com/get-started/03_updating_app/

## Share the application


https://docs.docker.com/get-started/04_sharing_app/


## Use Docker Compose


https://docs.docker.com/get-started/08_using_compose/







