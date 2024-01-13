# Networking overview

Containers have networking enabled by default, and they can make outgoing connections. 

A container has no information about what kind of network it's attached to, or whether their peers are also Docker workloads or not. 

A container only sees a network interface with an IP address, a gateway, a routing table, DNS services, and other networking details. 

That is, unless the container uses the none network driver.

Drivers

* bridge, the default network driver.
* host, remove network isolation between the container and the Docker host.
* none, completely isolate a container from the host and other containers.
* overlay, overlay networks connect multiple Docker daemons together.
* ipvlan
* macvlan

https://docs.docker.com/network/

## Commands

```bash

docker network ls

docker network connect

docker network create

docker network disconnect

docker network inspect

docker network prune

docker network rm

```

https://docs.docker.com/engine/reference/commandline/network/

## NetworkChuck


```bash
# 7 Networks in total

# remove all and start fresh
docker compose down
docker ps -a
docker rmi -f $(docker images -aq)
# maybe you need to rm volumes also if container name is changed or hostname
# docker volume rm $(docker volume ls -qf dangling=true)
docker network ls
docker network prune



# when we installed docker we get some cool stuff
ip address show
1: [..., inet 127.0.0.1/8]
2: etho0 [...., 192.xxx.x.x/24] # private
3: docker0 [..., 172.17.0.1/16] # 

docker network ps
# default
NETWORK ID     NAME      DRIVER    SCOPE
21b05ed49511   bridge    bridge    local
16e4c0c05bc5   host      host      local
0d5aff734251   none      null      local
```

Bridge, default in docker, docker0

```mermaid
graph TD;
    hostvm private-->docker private;
    
```
https://www.youtube.com/watch?v=bKFMS5C4CG0&t=844s

Lets use the rabbitmq x 2 with shovel containers