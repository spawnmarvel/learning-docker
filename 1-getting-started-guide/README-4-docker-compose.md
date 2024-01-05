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
# every time you update the Dockerfile, you must rm the docker images

FROM rabbitmq:3.12-management
COPY rabbitmq.conf /etc/rabbitmq
RUN cat /etc/rabbitmq/rabbitmq.conf
RUN rabbitmq-plugins enable --offline rabbitmq_shovel && rabbitmq-plugins enable --offline  rabbitmq_shovel_management
RUN rabbitmq-plugins enable --offline rabbitmq_mqtt

```
Compose file

```yml
version: '3'

services:
 rmq-app:
  build:
   context: .
   dockerfile: dockerfile
  hostname: rmq3.cloud
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
# ✔ Network rmq_net_messaging       Created                                                                                                 
# ✔ Volume "rmq_vol_rabbitmq_data"  Created                                                                                                  
# ✔ Container rmq-rmq-app-1         Started 


# volume
/datadrive/volumes/rmq_vol_rabbitmq_data/_data/mnesia

# volume on external drive
ls
rabbit@rmq3  rabbit@rmq3-feature_flags  rabbit@rmq3-plugins-expand

# config inside container
docker exec -it 6c4eee3c74ab bash
root@rmq3:/# cd /etc/rabbitmq/
root@rmq3:/etc/rabbitmq# ls
conf.d  enabled_plugins  rabbitmq.conf
# exit 13

docker compose logs -f

# to stop all
docker compose down


```

visit http://public-ip:15672

Shovel is listed and hostname is set.

![Shovel ](https://github.com/spawnmarvel/learning-docker/blob/main/images/shovel2.jpg)

Update Dockerfile ?

```bash
cd rmq

docker compose down
#  Container rmq-rmq-app-1    Removed                                                                                                      
#  Network rmq_net_messaging  Removed

# update the line to Dockerfile
# RUN rabbitmq-plugins enable --offline rabbitmq_shovel && rabbitmq-plugins enable --offline rabbitmq_shovel_management
# every time you update the Dockerfile, you must rm the docker images
docker images
docker rmi -f name

# maybe also remove volume, depends.

# start it
docker compose up -d

```




Persistent data

```bash
# we created a volume and ran docker compose up -d above

cd rmq

docker compose up -d

# Cluster rabbit@rmq3.cloud
# Create a queue3, add some messages, 2
# remember the volume
# volume
/datadrive/volumes/rmq_vol_rabbitmq_data/_data/mnesia

# volume on external drive
ls
rabbit@rmq3  rabbit@rmq3-feature_flags  rabbit@rmq3-plugins-expand

# stop it
docker compose down

docker compose up -d


```
![RabbitMQ persistent ](https://github.com/spawnmarvel/learning-docker/blob/main/images/rabbitmq_persistent2.jpg)

Data is presistent since we used hostname

https://follow-e-lo.com/2024/01/04/docker-compose/

## RabittMQ 2 (just a test for config)

Tested with advanced.config and shovel, it works.

It creates the shovel and tries to connect, success, but get timeout due to ports.

Both queues were added manually.

![RabbitMQ 2 advanced config ](https://github.com/spawnmarvel/learning-docker/blob/main/images/rabbitmq_advanced2.jpg)



## Compose file version 3 reference

What does the fields mean?

* FROM


https://docs.docker.com/compose/compose-file/compose-file-v3/

