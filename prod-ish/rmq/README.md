# Production-ish

## rmq-portainer-ssl

```bash
mkdir myfolder

cd myfolder
# copy all files in rmq-portainer-ssl
# compose.yml, definitions.json, Dockerfile, generate.sertificate.sh, rabbitmq.config

# run generate sertificate
bash generate.sertificate.sh

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
* Volume for both

View it:


