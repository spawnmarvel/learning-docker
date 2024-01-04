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
# ✔ Network rmq_net_messaging       Created                                                                                                 
# ✔ Volume "rmq_vol_rabbitmq_data"  Created                                                                                                  
# ✔ Container rmq-rmq-app-1         Started 

docker compose logs -f

docker compose down¨


```

visit http://public-ip:15672

Shovel is listed

But not showing in management, had to update Dockerfile with:

```bash

# run compose again, since we already had installed a container with no rabbitmq_shovel_management in Dockerfile
cd rmq

docker compose down
#  Container rmq-rmq-app-1    Removed                                                                                                      
#  Network rmq_net_messaging  Removed

# remove container if needed
docker ps -a

# remove image
docker rmi -f rmq-rmq-app

# remove volume
docker volume ls
docker volume rm -f 

# update the line to Dockerfile
# RUN rabbitmq-plugins enable --offline rabbitmq_shovel && rabbitmq-plugins enable --offline rabbitmq_shovel_management

# start it 
docker compose up -d

docker compose logs

# success with bot plugins


docker compose down
#  Container rmq-rmq-app-1    Removed                                                                                                      
#  Network rmq_net_messaging  Removed

# update the line to Dockerfile
# RUN rabbitmq-plugins enable --offline rabbitmq_mqtt


# every time you update the Dockerfile, you must rm the docker images
docker images
docker rmi -f rmq-rmq-app

# start it
docker compose up -d

```
Logs
```logs
rmq-rmq-app-1  | 2024-01-04 14:10:38.513106+00:00 [info] <0.604.0>  * rabbitmq_prometheus
rmq-rmq-app-1  | 2024-01-04 14:10:38.513106+00:00 [info] <0.604.0>  * rabbitmq_shovel_management
rmq-rmq-app-1  | 2024-01-04 14:10:38.513106+00:00 [info] <0.604.0>  * rabbitmq_mqtt
rmq-rmq-app-1  | 2024-01-04 14:10:38.513106+00:00 [info] <0.604.0>  * rabbitmq_shovel
rmq-rmq-app-1  | 2024-01-04 14:10:38.513106+00:00 [info] <0.604.0>  * rabbitmq_management
rmq-rmq-app-1  | 2024-01-04 14:10:38.513106+00:00 [info] <0.604.0>  * rabbitmq_management_agent
rmq-rmq-app-1  | 2024-01-04 14:10:38.513106+00:00 [info] <0.604.0>  * rabbitmq_web_dispatch

```

Persistent data

```bash
# we created a volume in docker compose up -d above

# the container is running

# make a queue and add a message and restart the container
docker restart containerid

# and queue01 is there with one message

# if we run docker compose down, and up again, then we get a new container name and mnesia is fresh again
```
https://follow-e-lo.com/2024/01/04/docker-compose/

## Compose file version 3 reference

What does the fields mean?

* FROM


https://docs.docker.com/compose/compose-file/compose-file-v3/

