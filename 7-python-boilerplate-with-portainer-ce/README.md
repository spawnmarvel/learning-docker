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
portainer/portainer-ce:latest

# copy python-boilerplate project to folder appdir
mkdir appdir

cp python-bolierplate

python-bolierplate$ cp Dockerfile app.py app_logger.py logging_config.ini worker.py ../appdir/

```
Edit code

```py

# add a while loop to app.py
 while work:
             wo.do_work()
# edit worker.py
    def do_work(self):
        time.sleep(2)
        logger.info("Sleeping....")


```
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

```





