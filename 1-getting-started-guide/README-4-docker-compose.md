##


https://docs.docker.com/compose/

## Commands

```bash
cd folder

touch compose.yml

docker compose up -d

docker compose logs -f

docker compose down
# If you want to remove the volumes, you need to add the --volumes flag.

```

## RabbitMQ

Run

```bash
# create the volume
docker volume create rabbitmq_data

# create the container
docker run -d --hostname rmq2 --name rabbitmq2 -p 15672:15672 -p 5672:5672 --mount type=volume,src=rabbitmq_data,target=/var/lib/rabbitmq rabbitmq:3.12-management
```

Compose

```bash

mkdir rmq

cd rmq

touch Dockerfile

sudo nano DockerFile

touch compose.yml

sudo nano compose.yml

touch rabbitmq.conf

sudo nano rabbitmq.conf

```

Dockerfile

https://hub.docker.com/_/rabbitmq

```bash

FROM rabbitmq:3.12-management
COPY rabbitmq.conf /etc/rabbitmq
RUN cat /etc/rabbitmq/rabbitmq.conf
RUN rabbitmq-plugins enable --offline rabbimq_shovel

```
Compose file

```yml
version: '3'

services:
 rmq-app:
  build:
   context: .
   dockerfile: Dockerfile
  ports:
   - 5672:5672
   - 15672:15672
  networks:
   - net_messaging
  volumes:
   - vol_rabbitmq_data:/var/lib/rabbitmq


networks:
 net_messaging:
  driver: bridge

volumes:
 vol_rabbitmq_data:

```
rabbtimq.conf

```bash
default_user = admin
default_pass = admin123
listeners.tcp.default = 5672
management.tcp.port = 15672
```

Run it

```bash
cd rmq

docker compose up -d

docker compose logs -f

docker compose down¨


```

## Compose file version 3 reference

What does the fields mean?

* FROM


https://docs.docker.com/compose/compose-file/compose-file-v3/

