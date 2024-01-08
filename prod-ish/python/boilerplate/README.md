# Python-bolierplate with Portainer

# Portainer

https://docs.portainer.io/start/install-ce/server/docker/linux


## Recall this old stuff

Lets copy some code from the old repos and make two containers.

* Python
* Portainer

https://follow-e-lo.com/2020/02/10/docker-ubuntu/

https://github.com/spawnmarvel/test_docker/blob/master/docker-compose.yml

We will use the while true add the requirements.txt and re factor a bit.

Lets take the app_logs and app_expetions also.

# Build and test app with requirements

Note.

Portainer Community Edition (CE) is a lightweight platform that effortlessly delivers containerized applications.

```bash
cd appdir

ls
Dockerfile  app.py  app_logs  compose.yml  config.json  worker.py

```
Run it

```py

# run it
python3 app.py
2024-01-08 20:55:45,873 - 139707627712960 - 5561 - app.py - 13 -             <module>() root - INFO - Version 0.1
2024-01-08 20:55:45,873 - 139707627712960 - 5561 - app.py - 35 -             <module>() root - INFO - In main
2024-01-08 20:55:45,873 - 139707627712960 - 5561 - app.py - 41 -             <module>() root - INFO - Main Pid: 5561
2024-01-08 20:55:47,875 - 139707627712960 - 5561 - worker.py - 23 -              do_work() root - INFO - Sleeping....
2024-01-08 20:55:47,876 - 139707627712960 - 5561 - worker.py - 17 -            read_conf() root - INFO - [{'name': 'testconfig', 'id': 1}]


```
08.01.2024..... continue
Add a library to requirements and pip install it

Test the app

```bash
sudo apt install python3-pip

sudo pip3 install flask
# We should create an env, but this is just for test
# WARNING: Running pip as the 'root' user can result in broken permissions and conflicting behaviour with the system package manager. It is recommended to use a virtual environment instead: https://pip.pypa.io/warnings/venv

# ad import to app.py
from flask import Flask

# Run it
cd /appdir

python3 app.py

# requirements.txt
sudo nano requirements.txt

Flask==3.0.0

# files
appdir$ ls
Dockerfile  __pycache__  app.py  app_logger.py  logging_config.ini  logs_app.txt  requirements.txt  worker.py

```
Update the Docker file
```bash
# was
FROM python:3.10-slim-buster
WORKDIR /usr/src/app
COPY . .
CMD [ "python", "./app.py" ]

# new
FROM python:3.10-slim-buster
WORKDIR /usr/src/app
COPY . .
run pip3 install -r requirements.txt
CMD [ "python", "./app.py" ]
```

Create the container

```bash
cd /appdir

# build
docker image build -t python-test .

# test it
docker run python-test

```


https://hub.docker.com/r/portainer/portainer-ce

# Docker compose with Portainer

```bash
sudo nano compose.yml
# the content from the compose.yml file

docker compose up
# succcess

```

Note: Not logging to file, hm....

```bash
cd /appdir

docker compose up -d

Container appdir-portainer-1, Running                                                                                  
Container appdir-python-boilerplate-1  Started

docker ps
docker logs 03dd725e142b

```
Added method for reading config in worker.py and added config.json

Test it

```bash
docker images

docker rmi id --force

docker compose up

docker logs appdir-python-boilerplate-1

# working
# do_work() root - INFO - Sleeping....
# read_conf() root - INFO - [{'name': 'testconfig', 'id': 1}]
# when done


```

Where (and why) is logs_app.txt file

```bash
docker compose up -d

docker ps

docker inspect appdir-python-boilerplate-1

"LogPath": "/var/lib/docker/containers/43fa6b08b8ecda00ceff3cba17f067f4e95968fc5c709114fb496ccba9b2f580/43fa6b08b8ecda00ceff3cba17f067f4e95968fc5c709114fb496ccba9b2f580-json.log",

"HostConfig": {
            "Binds": [
                "/home/imsdal/appdir:/code:rw"


"Mounts": [
            {
                "Type": "bind",
                "Source": "/home/imsdal/appdir",
                "Destination": "/code",
                "Mode": "rw",


cd /var/lib/docker/containers/43fa6b08b8ecda00ceff3cba17f067f4e95968fc5c709114fb496ccba9b2f580

```

Edit in compose.yml

```bash

 volumes:
            - .:/code
            - log:/user/src/appdir

# [...]
volumes:
    portainer_data:
    log:


docker compose up

Network appdir_app_network             Created   
Network appdir_default                 Created 
Volume "appdir_log"                    Created
Container appdir-portainer-1           Created
Container appdir-python-boilerplate-1 Created


```





