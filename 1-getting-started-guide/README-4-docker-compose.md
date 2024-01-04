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

```

Dockerfile

```bash
```
Compose file

```yml
```

