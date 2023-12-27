# Try Docker Compose

https://docs.docker.com/compose/gettingstarted/

## Install it

```bash
sudo apt update -y
sudo apt install docker-compose-plugin
# docker-compose-plugin is already the newest version (2.21.0-1~ubuntu.22.04~jammy).

docker compose version
Docker Compose version v2.21.0

```

https://docs.docker.com/compose/install/linux/#install-using-the-repository

## Prerequisites

## Step 1: Define the application dependencies

```bash
mkdir composetest

cd composetest

sudo nano app.py

# cp the python code for the app, we are not here to learn python, but docker.

sudo nano requirements.txt

# flask
# redis

```

## Step 2: Create a Dockerfile

```bash
# create the docker file
sudo nano Dockerfile

# syntax=docker/dockerfile:1
FROM python:3.7-alpine
WORKDIR /code
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
RUN apk add --no-cache gcc musl-dev linux-headers
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 5000
COPY . .
CMD ["flask", "run"]

```
This tells Docker to:

* Build an image starting with the Python 3.7 image.
* Set the working directory to /code.
* Set environment variables used by the flask command.
* Install gcc and other dependencies
* Copy requirements.txt and install the Python dependencies.
* Add metadata to the image to describe that the container is listening on port 5000
* Copy the current directory . in the project to the workdir . in the image.
* Set the default command for the container to flask run.

## Step 3: Define services in a Compose file

```bash
sudo nano compose.yml
```
yml

```yml
services:
  web:
    build: .
    ports:
      - "8000:5000"
  redis:
    image: "redis:alpine"

```

The web service uses an image that's built from the Dockerfile in the current directory. It then binds the container and the host machine to the exposed port, 8000. This example service uses the default port for the Flask web server, 5000.

The redis service uses a public Redis image pulled from the Docker Hub registry.

## Step 4: Build and run your app with Compose

```bash
docker compose up
```
Add NSG for port 8000

Enter http://publicip:8000/ in a browser to see the application running.

Result:

```log
Hello World! I have been seen 17 times.

composetest-web-1    | 80.xx.xx.xx - - [27/Dec/2023 12:50:33] "GET / HTTP/1.1" 200 -
composetest-web-1    | 80.xxx.xx.xx - - [27/Dec/2023 12:50:33] "GET / HTTP/1.1" 200 -


```

https://docs.docker.com/compose/gettingstarted/