# Production-ish


## portainer
````bash
https://github.com/spawnmarvel/learning-docker/blob/main/prod-ish/portainer/README.md

```
## rmq-ssl

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

## wordpress-phpmyadmin-portainer

Go to readme for more details.

```bash
# Go to folder and just copy all files to a dir and run 
mkdir my_wordpress
cd my_wordpress

docker compose up -d

# Network my_wordpress_net_shared           Created                                                             
# Volume "my_wordpress_vol_portainer_data"  Created                                                              
# Volume "my_wordpress_vol_db_data"         Created                                                               
# Volume "my_wordpress_vol_wp_data"         Created                                                               
# Container my_wordpress-db-1               Started                                                               
# Container my_wordpress-portainer-1        Started                                                               
# Container my_wordpress-wordpress-1        Started                                                               
# Container my_wordpress-phpmyadmin-1       Started
```

## wordpress-portainer ssl

TODO

## zabbix-portainer

TODO

## zabbix-portainer-ssl


TODO

## python with build image/push and pull to docker hub

TODO