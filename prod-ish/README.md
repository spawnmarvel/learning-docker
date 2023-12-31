# Production-ish

## rmq-portainer-ssl

```bash

# Docker and Docker compose is installed on machine
mkdir myfolder

cd myfolder
# copy all files in rmq-portainer-ssl
# compose.yml, definitions.json, Dockerfile, generate.sertificate.sh, rabbitmq.config

# run generate sertificate
bash generate.sertificate_keyusage.sh

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

* Portainer https 9443
* Rabbitmq instance named rmq1.cloud
* Rabbitmq https 15671 and 5671 (5672)
* Rabbitmq user, and one queue, shovel enabled
* Certificate is enabled with -addext "extendedKeyUsage = serverAuth, clientAuth" (for shovel)
* A volume for both that is persistent

Tested:

* Tested docker restart, success
* Testet compose down/up, success
* Tested restart VM when docker is running, success

View it:

https://follow-e-lo.com/2024/01/06/docker-rabbitmq/

## rmq-x2-portainer

```bash

# Docker and Docker compose is installed on machine
mkdir myfolder

cd myfolder
# copy all files in rmq-x2-portainer
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

* Portainer https 9443
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

## apache-portainer

```bash
# Go to folder and just copy all files to a dir and run 

docker compose up -d

# Network apache-portainer_net_http             Created                                                       
# Volume "apache-portainer_vol_portainer_data"  Created                                                          
# Container apache-portainer-portainer-1        Started                                                          
# Container httpd_web                           Started
```

## apache-portainer-ssl

TODO

## zabbix-portainer-ssl

TODO

## wordpress

TODO

## wordpress ssl

TODO

## python with build image/push and pull to docker hub

TODO