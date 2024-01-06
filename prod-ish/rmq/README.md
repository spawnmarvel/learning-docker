# Production-ish

## rmq-portainer-ssl

```bash
mkdir myfolder

cd myfolder
# copy all files in rmq-portainer-ssl

# run generate sertificate
bash generate.sertificate.sh

docker compose up -d

```

Then you have the following

* Portainer https
* Rabbitmq https and 5671 (5672)
* Rabbitmq user, and one queue, shovel enabled
* Volume for both

View it:


