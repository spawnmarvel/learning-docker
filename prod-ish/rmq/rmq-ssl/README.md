## rmq-ssl

```bash

# Docker and Docker compose is installed on machine
mkdir myfolder

cd myfolder
# copy all files in rmq-ssl
# compose.yml, definitions.json, Dockerfile, generate.sertificate.sh, generate.sertificate_keyusage.sh, rabbitmq.config

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

* Rabbitmq instance named rmq1.cloud
* Rabbitmq https 15671 and 5671 (5672)
* Rabbitmq user, and one queue, shovel enabled
* Certificate is enabled with -addext "extendedKeyUsage = serverAuth, clientAuth" (for shovel)
* A volume

Tested:

* Tested docker restart, success
* Testet compose down/up, success
* Tested restart VM when docker is running, success

View it:

https://follow-e-lo.com/2024/01/06/docker-rabbitmq/