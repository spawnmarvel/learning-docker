# rmq-x2

```bash

# Docker and Docker compose is installed on machine
mkdir myfolder

cd myfolder
# copy all files in rmq-x2
# Dockerfile_client  Dockerfile_server  client  compose.yml  server

# start
docker compose up -d

# stop with docker stop/start or use portainer

# down
docker compose down

# remove all after compose down
docker rmi -f $(docker images -aq)

docker volume rm $(docker volume ls -qf dangling=true)

```

Then you have the following

* Rabbitmq instance named rmq_client
* Rabbitmq rmq_client 15672 and 5672
* Rabbitmq rmq_client user, and one queue, shovel enabled
* Rabbitmq instance named rmq_server
* Rabbitmq rmq_server 15673 and 5673 (inbound shovel)
* Rabbitmq rmq_server, and same user
* A volume for both that is persistent

Tested:

* Tested docker restart, success
* Testet compose down/up, success
* Tested restart VM when docker is running, success

View it:

https://follow-e-lo.com/2024/01/09/docker-rabbtimq-x2/

## Update version 14.06.2024

Test new version update Dockerfile_client, server

* FROM rabbitmq:3.12-management
* Version 3.13-management

```bash
/home/imsdal/rmq-x2
nano Dockerfile_client
# FROM rabbitmq:3.13-management
nano Dockerfile_server
# FROM rabbitmq:3.13-management

docker compose up -d
```