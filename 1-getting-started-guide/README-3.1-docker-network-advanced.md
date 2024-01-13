# Networking advanced overview

https://academy.pointtosource.com/docker/advanced-docker-networking/

If you create a docker-compose service but do not specify a network, docker will create a network for you.

1. it will assign a name, normally default_service1, where 'service1' is the name of the first service in the stack
2. it will assign an IP subnet

# Networking in Compose

https://docs.docker.com/compose/networking/

## Creating network in compose

```bash
# go to folder rmq6-portainer
# we just pasted the files from rmq4-portainer

# make a folder and run it

mkdir rmq6-portainer
cd rmq6-portainer

# copy the files

# run it and test
docker compose up

#visit http://public-ip:15672

docker network ls

NETWORK ID     NAME                           DRIVER    SCOPE
e0874f3b7a35   bridge                         bridge    local
16e4c0c05bc5   host                           host      local
0d5aff734251   none                           null      local
ed9f785cbb36   rmq6-portainer_net_messaging   bridge    local

docker ps

ip address show

3: docker0
- link/ether 02:42:c3:15:b8:81 brd ff:ff:ff:ff:ff:ff
- inet 172.17.0.1/16 brd 172.17.255.255 scope global docker0
9: br-ed9f785cbb36:
- link/ether 02:42:8e:8e:a8:ae brd ff:ff:ff:ff:ff:ff
- inet 172.19.0.1/16 brd 172.19.255.255 scope global br-ed9f785cbb36 
11: veth1061f68@if10:
- link/ether 22:a8:c8:25:cc:f6 brd ff:ff:ff:ff:ff:ff link-netnsid 1
- inet6 fe80::20a8:c8ff:fe25:ccf6/64 scope link
13: veth0e490da@if12
- link/ether ce:79:58:12:be:92 brd ff:ff:ff:ff:ff:ff link-netnsid 0
- inet6 fe80::cc79:58ff:fe12:be92/64 scope link

```
current network

```yml

networks:
  net_messaging:
    driver: bridge

```
inspect net_messaging

```bash
# get bridge
bridge link

11: veth1061f68@if10: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 master br-ed9f785cbb36 state forwarding priority 32 cost 2
13: veth0e490da@if12: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 master br-ed9f785cbb36 state forwarding priority 32 cost 2


# get ip address, by using the network name appended with folder
docker inspect rmq6-portainer_net_messaging

 "Containers": {
     "Name": "rmq6-portainer-portainer-1",
      "IPv4Address": "172.19.0.3/16",
       "Name": "rmq6-portainer-rmq-app-1",
       "IPv4Address": "172.19.0.2/16",

```

## Defining the network name and IP subnet.

Now when you run the docker-compose file, it will create a network called net_messaging, assign it to that particular subnet (if it's free) and connect your container to it.

Update the compose file.

```yml
networks:
  default:
    name: net_messaging
    ipam: 
      config:
        - subnet: 172.50.0.0/24

```
## Creating the 'default' docker network

Stack of 1 to n containers.

Now we could specify networks: in each 'service' block, but we don't need to. We can do it directly from the ' networks' block:
This applies to all the services which do not have their own networks: variable.

```bash
cd rmq6-portainer

docker compose down

docker compose up -d

# Network net_messaging                 Created                                                                         # Container rmq6-portainer-portainer-1  Started                                                                         
# Container rmq6-portainer-rmq-app-1    Started

# run the same drill to get the ip address

docker network ls

docker network ls
NETWORK ID     NAME            DRIVER    SCOPE
e0874f3b7a35   bridge          bridge    local
16e4c0c05bc5   host            host      local
2dfcd41aa23f   net_messaging   bridge    local
0d5aff734251   none            null      local

docker inspect net_messaging
"Containers": {
     "Name": "rmq6-portainer-rmq-app-1",
      "IPv4Address": "172.50.0.3/24",
       "Name": "rmq6-portainer-portainer-1",
       "IPv4Address": "172.50.0.2/24",


# enter rmq
docker exec -it rmq6-portainer-rmq-app-1 sh

apt update -y
apt install -y iputils-ping

# ping it
ping 172.50.0.2
PING 172.50.0.2 (172.50.0.2) 56(84) bytes of data.
64 bytes from 172.50.0.2: icmp_seq=1 ttl=64 time=0.119 ms
64 bytes from 172.50.0.2: icmp_seq=2 ttl=64 time=0.076 ms

# dns

ping rmq6-portainer-portainer-1
PING rmq6-portainer-portainer-1 (172.50.0.2) 56(84) bytes of data.
64 bytes from rmq6-portainer-portainer-1.net_messaging (172.50.0.2): icmp_seq=1 ttl=64 time=0.064 ms
64 bytes from rmq6-portainer-portainer-1.net_messaging (172.50.0.2): icmp_seq=2 ttl=64 time=0.078 ms

```

Lets see the link and create a container without network (use default bridge)

```bash

# 
cd rmq6-portainer

docker compose down

# ip address
ip address show
4: docker0:

# bridge
bridge link
# null

docker compose up -d

# ip address
ip address shwo
4: docker0:
9: br-8922d7a09a26:
11: veth4e32edb@if10:
13: veth287c510@if12:

# bridge
bridge link

11: veth4e32edb@if10: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 master br-8922d7a09a26 state forwarding priority 32 cost 2
13: veth287c510@if12: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 master br-8922d7a09a26 state forwarding priority 32 cost 2

cd ..
docker run -itd --rm -p 80:80 --name stormbreaker nginx

# ip address
ip address shwo
4: docker0:
9: br-8922d7a09a26:
11: veth4e32edb@if10:
13: veth287c510@if12:
15: vethf6a8bef@if14:

# default bridge net
docker inspect bridge
"Containers": {
   "Name": "stormbreaker",
    "IPv4Address": "172.17.0.2/16",

# net_messaging
docker inspect net_messaging 
docker inspect net_messaging
"Containers": {
     "Name": "rmq6-portainer-rmq-app-1",
      "IPv4Address": "172.50.0.3/24",
       "Name": "rmq6-portainer-portainer-1",
       "IPv4Address": "172.50.0.2/24",

# stop
docker stop stormbreaker
cd rmq6-portainer
docker compose down

```
1. We have the default network bridge.
2. We make a network for all containers to share in a compose file.
3. You can make more net's in the same docker, ie. app can talk to frontend and db. But db can only talk to app.
