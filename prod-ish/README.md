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


## apache-portainer-ssl

TODO

## zabbix-portainer-ssl

TODO