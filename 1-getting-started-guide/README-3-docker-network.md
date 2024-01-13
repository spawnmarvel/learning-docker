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

docker network

docker network connect

docker network create

docker network disconnect

docker network inspect

docker network prune

docker network rm

```

https://docs.docker.com/engine/reference/commandline/network/