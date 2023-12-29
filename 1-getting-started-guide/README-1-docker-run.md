# Docker run

The docker run command runs a command in a new container, pulling the image if needed and starting the container.

https://docs.docker.com/engine/reference/commandline/run/

## Visuals

https://follow-e-lo.com/2023/12/29/docker-run/

## Examle Ubuntu

```bash

# list all images
docker images
# none

# list all running containers
docker ps

# list all containers
docker ps -a

# remove all containers
docker rm -f $(docker ps -a -q)


# pull ubuntu and start shell inside, quit shell with exit 13
docker run --name testubuntu -it ubuntu

docker ps

docker ps -a
# testubuntu  47 seconds ago

# start it, stop or restart
docker start testubuntu

# Capture container ID (--cidfile)

```
docker ps -a

CONTAINER ID   IMAGE     COMMAND       CREATED        STATUS                      PORTS     NAMES

2b2cce6e6241   ubuntu    "/bin/bash"   13 hours ago   Exited (137) 13 hours ago             testubuntu

docker images

REPOSITORY   TAG       IMAGE ID       CREATED       SIZE

ubuntu       latest    174c8c134b2a   2 weeks ago   77.8MB
## Example MariaDB

```bash

docker search mariadb

docker pull mariadb:11

# --name			Assign a name to the container
# --env	    -e		Set environment variables
# --publish	-p		Publish a container's port(s) to the host
# --detach	-d		Run container in background and print container ID

# --rm			Automatically remove the container when it exits


# docker images to get the id for run
c74611c2858a

docker run --name mariadb1 -e MYSQL_ROOT_PASSWORD=mypass -p 3306:3306 -d c74611c2858a

docker ps

# create a new instance, just for test and show
docker run --name mariadb2 -e MYSQL_ROOT_PASSWORD=mypass -p 3307:3307 -d c74611c2858a

# now there are two containers from the same image
docker ps -a


# connecting to mariadb from outside the container

docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' mariadb1

# ip is returned

# You can now connect to the MariaDB server using a TCP connection to that IP address.
sudo apt install mysql-client-core-8.0

mysql -h 172.17.0.2 -u root -p


```
Persistent data: SQL, db, table and a row.

```sql
/* Create a db, table and and insert a row. */
create database db1;

use db1;

create table tb1(t_id INT NOT NULL AUTO_INCREMENT, t_name VARCHAR(20), PRIMARY KEY(t_id));

insert into tb1 (t_name) values ("John");

select * from tb1;

exit;
/* Bye */
```

Stop and start

```bash
docker stop mariadb1

docker start mariadb1

docker ps

# enter mysql and the data is there

docker inspect mariadb1

# Mounts:
#"Type": "volume",
#                "Name": #"a66cca[..]",
#                "Source": "/var/lib/docker/volumes/#a66cca[..]/_data",
#                "Destination": "/var/lib/mysql",
#                "Driver": "local",

```
Restart vm

```bash
docker start mariadb1

docker ps

docker start mariadb

# enter mysql and the data is there

# autmatic restart update
docker update --restart always mariadb1

# test with restart vm


# enter container with bash, out exit 13
docker exec -it mariadb1 bash

# logs
docker logs mariadb1


```
https://mariadb.com/kb/en/installing-and-using-mariadb-via-docker/