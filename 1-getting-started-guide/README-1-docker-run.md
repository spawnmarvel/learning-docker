# Docker run

The docker run command runs a command in a new container, pulling the image if needed and starting the container.

https://docs.docker.com/engine/reference/commandline/run/

## Examples

```bash

# list all images
docker images
# none

# list all running containers
docker ps

# list all containers
docker ps -a

# remove all containers
docker rm -f $(docker ps -a -q)


# pull ubuntu and start shell inside, quit shell with exit 13
docker run --name testubuntu -it ubuntu

docker ps

docker ps -a
# testubuntu  47 seconds ago

# start it, stop or restart
docker start testubuntu

# Capture container ID (--cidfile)

```