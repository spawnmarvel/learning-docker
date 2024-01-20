# Zabbix

Could you make a compose.yml for zabbix with local agent, but no proxy and mysql?

Could you make a compose.yml for zabbix version 6 with local agent, but no proxy and mysql?

## Vicuna


### compose1

Could you make a compose.yml for zabbix version 6 with local agent, but no proxy and mysql?

Here is a docker compose file for Zabbix version 6 with a local Zabbix agent, MySQL database, and no proxy:

Compose1.yml


The key differences from Zabbix 5.x:

Use Zabbix 6.0 images
MySQL 8.0 instead of 5.7
No Zabbix proxy service
Otherwise it follows the same pattern of Zabbix server, MySQL database, and local Zabbix agent.


### compose2

Sure, here is a simple example of docker-compose.yml file that starts Zabbix server with MySQL database and Zabbix agent:

compose2.yml

This docker-compose.yml file creates three services: zabbix-server, mysql-server, and zabbix-agent.

The Zabbix server and agent services are using the latest Zabbix 6.0 images. The MySQL service is using a MySQL 8.0 image. The Zabbix server and agent services depend on the MySQL service.

The Zabbix server and agent services are configured using environment variables. The MySQL service is also configured using environment variables, and its data is stored in a Docker volume.

Please adjust the MySQL root password and other environment variables as per your needs.

## Lets spin up compose 2

```bash
mkdir zabbix2
cp compose.yml

 docker compose up -d
[+] Running 29/3
 ✔ zabbix-agent 6 layers [⣿⣿⣿⣿⣿⣿]      0B/0B      Pulled                                    10.8s
 ✔ zabbix-server 9 layers [⣿⣿⣿⣿⣿⣿⣿⣿⣿]      0B/0B      Pulled                                15.7s
 ✔ mysql-server 11 layers [⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿]      0B/0B      Pulled                              25.2s
[+] Running 5/5
 ✔ Network zabbix2_default            Created                                                0.1s
 ✔ Volume "zabbix2_mysql-data"        Created                                                0.0s
 ✔ Container zabbix2-mysql-server-1   Started                                                0.0s
 ✔ Container zabbix2-zabbix-server-1  Started                                                0.2s
 ✔ Container zabbix2-zabbix-agent-1   Started

```

## But surely that was not enough....so much to AI or my prompts....

# HOW-TO: Install Zabbix with MySQL as containers using docker-compose


## Visuals on e-lo

https://follow-e-lo.com/2024/01/20/docker-zabbix/

## Install Zabbix with MySQL as containers using docker-compose

* VM
* Docker and docker compose

Clone the official Zabbix Docker GitHub repository

```bash

git clone https://github.com/zabbix/zabbix-docker.git

cd zabbix-docker

```

If you already have a copy of the repository and want to make sure that you have the latest code, then use the git fetch command.

```bash
git fetch https://github.com/zabbix/zabbix-docker.git

```

### Bring up zabbix with docker compose

```bash

/home/imsdal/zabbix-docker

docker compose -f /home/imsdal/zabbix-docker/docker-compose_v3_ubuntu_mysql_local.yaml up -d


[...]
Unable to flush stdout: No space left on device

# used space
df -h
Filesystem      Size  Used Avail Use% Mounted on
/dev/root        29G  3.8G   26G  13% /
tmpfs           2.0G     0  2.0G   0% /dev/shm
tmpfs           781M  1.1M  780M   1% /run
tmpfs           5.0M     0  5.0M   0% /run/lock
/dev/sdb15      105M  6.1M   99M   6% /boot/efi
/dev/sda1       4.0G  3.7G  332M  92% /datadrive
/dev/sdc1       7.8G   28K  7.4G   1% /mnt
tmpfs           391M  4.0K  391M   1% /run/user/1000

# out of inodes?
df -i
Filesystem      Inodes  IUsed   IFree IUse% Mounted on
/dev/root      3870720 122502 3748218    4% /
tmpfs           499622      1  499621    1% /dev/shm
tmpfs           819200    791  818409    1% /run
tmpfs           499622      3  499619    1% /run/lock
/dev/sdb15           0      0       0     - /boot/efi
/dev/sda1       827528 147528  680000   18% /datadrive
/dev/sdc1       524288     12  524276    1% /mnt
tmpfs            99924     25   99899    1% /run/user/1000
# nope, none is 100%



# It is the datadrive
/dev/sda1       4.0G  3.7G  332M  92% /datadrive

docker system prune
# Total reclaimed space: 436.2MB

df -h
/dev/sda1       4.0G  2.1G  2.0G  52% /datadrive

# expand it to 8 GB since docker stores everything on /datadrive due to update docker config


docker compose -f /home/imsdal/zabbix-docker/docker-compose_v3_ubuntu_mysql_local.yaml up -d


```

### zbx_env directory

```bash
/home/imsdal/zabbix-docker/zbx_env
ls
etc  usr  var
# This is where all persistent data from the containers are stored.
```

### Zabbix configuration

Go to browser and enter your the IP address of the host machine for the docker containers.
* Admin, zabbix

### Container IP configuration

We now need to get the IP address of the docker container that hosts the agent to provide to the Zabbix application so that it can do self-reporting.

```bash
docker ps --filter  "name=zabbix-docker_zabbix-agent_1"
# there is no container for agent, ref visual also it is not started or built.
```

https://github.com/zabbix/zabbix-docker/issues/889


docker compose

* Use -f to specify the name and path of one or more Compose files
* * docker compose -f docker-compose.yml -f docker-compose.admin.yml run backup_db
* Use profiles to enable optional services
* * Use --profile to specify one or more active profiles Calling docker compose --profile frontend up starts the services with the profile frontend and services without any specified profiles. 
* * You can also enable multiple profiles, e.g. with docker compose --profile frontend --profile debug up the profiles frontend and debug is enabled.
* * Profiles can also be set by COMPOSE_PROFILES environment variable.

https://docs.docker.com/engine/reference/commandline/compose/


docker-compose_v3_ubuntu_mysql_local.yaml

```yml
 profiles:
   - all

```
```bash
# bring it down

docker compose -f /home/imsdal/zabbix-docker/docker-compose_v3_ubuntu_mysql_local.yaml down

# and up
docker compose -f /home/imsdal/zabbix-docker/docker-compose_v3_ubuntu_mysql_local.yaml up -d

# execute docker-compose with --profile=full or --profile=all.
# unknown flag: --profile=all

docker compose
# [...]
-f, --file stringArray           Compose configuration files
      --parallel int               Control max parallelism, -1 for unlimited (default -1)
      --profile stringArray        Specify a profile to enable


docker compose -f /home/imsdal/zabbix-docker/docker-compose_v3_ubuntu_mysql_local.yaml --profile=all up -d

[...]
12.47  unable to create '/var/lib/dpkg/updates/tmp.i': No space left on device

df -h
Filesystem      Size  Used Avail Use% Mounted on
/dev/root        29G  4.2G   25G  15% /
tmpfs           2.0G     0  2.0G   0% /dev/shm
tmpfs           781M  1.1M  780M   1% /run
tmpfs           5.0M     0  5.0M   0% /run/lock
/dev/sdb15      105M  6.1M   99M   6% /boot/efi
/dev/sda1       4.0G  3.4G  628M  85% /datadrive
/dev/sdc1       7.8G   28K  7.4G   1% /mnt
tmpfs           391M  4.0K  391M   1% /run/user/1000

```

Resize disk (it was 4gb) and resize it on the vm also

```bash

# GOTO and partition it from 4 to use all 8 gb avaliable
# https://github.com/spawnmarvel/learning-docker/blob/main/README-0-mount.md

df -h
Filesystem      Size  Used Avail Use% Mounted on
/dev/root        29G  4.2G   25G  15% /
tmpfs           2.0G     0  2.0G   0% /dev/shm
tmpfs           781M  1.1M  780M   1% /run
tmpfs           5.0M     0  5.0M   0% /run/lock
/dev/sda15      105M  6.1M   99M   6% /boot/efi
/dev/sdc1       8.0G  3.5G  4.6G  43% /datadrive
/dev/sdb1       7.8G   32K  7.4G   1% /mnt
tmpfs           391M  4.0K  391M   1% /run/user/1000



```

pause 20.01.2024

```bash
docker compose -f /home/imsdal/zabbix-docker/docker-compose_v3_ubuntu_mysql_local.yaml down
```



https://gist.github.com/gmirsky/8e2ad4627648194c7fc27930b6928880