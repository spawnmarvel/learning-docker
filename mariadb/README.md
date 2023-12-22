# Installing and Using MariaDB via Docker

https://mariadb.com/kb/en/installing-and-using-mariadb-via-docker/#installing-docker-on-your-system-with-the-universal-installation-script

## Downloading an Image

```bash
docker search mariadb
# Once you have found an image that you want to use, you can download it via Docker.

docker pull mariadb:11.0

# List all
docker images

REPOSITORY    TAG       IMAGE ID       CREATED        SIZE
mariadb       11.0      2103f67114de   6 days ago     404MB
hello-world   latest    d2c94e258dcb   7 months ago   13.3kB

```

## Creating container 

```bash
# run it
docker run --name mariadbtest -e MYSQL_ROOT_PASSWORD=mypass -p 3306:3306 -d docker.io/library/mariadb:11.0

# view all
docker ps
CONTAINER ID   IMAGE          COMMAND                  CREATED              STATUS              PORTS                                       NAMES
1fbf23217254   mariadb:11.0   "docker-entrypoint.s…"   About a minute ago   Up About a minute   0.0.0.0:3306->3306/tcp, :::3306->3306/tcp   mariadbtest

# stop it
docker stop mariadbtest

# Optionally, after the image name, we can specify some options for mysqld. For example: But you cannot use the same name, and later it.

docker run --name mariadbtest -e MYSQL_ROOT_PASSWORD=mypass -p 3306:3306 -d mariadb:11.0 --log-bin --binlog-format=MIXED

```

## Running and Stopping the Container

```bash
# Docker allows us to restart a container with a single command:
docker restart mariadbtest

# The container can also be stopped like this:
docker stop mariadbtest

# The container will not be destroyed by this command. The data will still live inside the container, even if MariaDB is not running. To restart the container and see our data, we can issue:
docker start mariadbtest

# With docker stop, the container will be gracefully terminated: a SIGTERM signal will be sent to the mysqld process, and Docker will wait for the process to shutdown before returning the control to the shell. However, it is also possible to set a timeout, after which the process will be immediately killed with a SIGKILL. 
docker stop --time=30 mariadbtest

# Or it is possible to immediately kill the process, with no timeout.
docker kill mariadbtest

# In case we want to destroy a container, perhaps because the image does not suit our needs, we can stop it and then run:

# In case we want to destroy a container, perhaps because the image does not suit our needs, we can stop it and then run:

docker rm mariadbtest

# and then we can create a new with the same name
docker run --name mariadbtest -e MYSQL_ROOT_PASSWORD=mypass -p 3306:3306 -d docker.io/library/mariadb:11.0

# Automatic Restart
# no, on-failure, unless-stopped, always
# It is possible to change the restart policy of existing, possibly running containers:
docker update --restart always mariadbtest


```


## Troubleshooting a Container

```bash
docker logs mariadbtest

```


## Accessing the Container

```bash
docker exec -it mariadbtest bash

# Now we can use normal Linux commands like cd, ls, etc. We will have root privileges. We can even install our favorite file editor, for example

exit

```


## Connecting to MariaDB from Outside the Container

```bash
```


## Next

```bash
```


## Next

```bash
```

