# Zabbix Docker / Nemesis

## docker compose

Create a folder for your Zabbix stack and set up these two files:

zabbix-stack/
* .env
* compose.yaml

Versions

* image: mysql:8.4
* image: zabbix/zabbix-server-mysql:ubuntu-7.0-latest

.env

```ini
# General Paths
ZABBIX_DATA_PATH=/datadrive/zabbix-data

# Database Credentials
MYSQL_DATABASE=zabbix
MYSQL_USER=zabbix
MYSQL_PASSWORD=apasssword
MYSQL_ROOT_PASSWORD=anewpassword

# Zabbix Config
ZBX_SERVER_NAME=zabbixdocker
PHP_TZ=Europe/Oslo
ZBX_STARTPINGERS=3
```

This build assumes there in an external datadrive:

```bash
df -h /datadrive
Filesystem      Size  Used Avail Use% Mounted on
/dev/sdc1       8.0G  473M  7.5G   6% /datadrive
```

Docker is using it for volumes

```bash
cat /etc/docker/daemon.json
{
   "data-root": "/datadrive"
}

```
## 1 Build and launch the stack

```bash
sudo nano compose.yml
# add the compose from this repo
docker compose up -d

# The "Total Wipe" (Clean Slate) if you need to rebuild
# 1. Stop and remove everything
docker compose down -v

# 2. Delete the data folders from BOTH possible locations
sudo rm -rf ./zabbix-data
sudo rm -rf /datadrive/zabbix-data

# 3. Prune Docker to clear any stuck cache
docker system prune -a --volumes -f

```

1. Disk Space: Since /datadrive is now 8GB and XFS-formatted, MySQL 8.4 has enough room to expand its temporary "Undo Logs" during the import.

2. Hostname Sync: By setting ZBX_HOSTNAME=ZabbixDocker in the .env, the agent will identify itself correctly the moment it heartbeats to the server.

3. Pathing: Docker will automatically create /datadrive/zabbix-data with the correct permissions.

This takes 3 to 5 minutes, take a break.

![pull](https://github.com/spawnmarvel/learning-docker/blob/main/prod-ish-2/zabbix/zabbix-stack/images/pull.png)

How to monitor the
```bash

# you can watch the table count grow until it hits 170 to 220, change the password
watch -n 5 'docker exec -it zabbix-db mysql -u zabbix -apassword -e "USE zabbix; SHOW TABLES;" | wc -l'

Sun Jan 18 20:44:24 2026

208

```
If you run a compose down, you will see.

```logs
imsdal@dmzdocker03:~/docker-zabbix-stack$ docker compose up -d
WARN[0000] No services to build                         
[+] up 5/5
 ✔ Network docker-zabbix-stack_default Created                                                                        0.0s 
 ✔ Container zabbix-db                 Created                                                                        0.5s 
 ✔ Container zabbix-server             Created                                                                        0.2s 
 ✔ Container zabbix-agent              Created                                                                        0.3s 
 ✔ Container zabbix-web                Created                                                                        0.3s

```

The "No services to build" Warning
This warning (WARN[0000] No services to build) is completely normal.

* What it means: It's just Docker telling you that there isn't a build: instruction in your YAML file (because we are using pre-made official images instead of building our own).

* Why you see it: Recent updates to Docker Compose added this log message to let users know it's skipping the "build" phase. Since your output shows [+] up 5/5 and all containers show ✔ Created, the command was 100% successful.


Open ufw since it is enabled

```bash
sudo ufw status
sudo ufw allow 8081

```
Open NSG for the same port 8081 also.

## 2 Verify the stack or jump to 3.

```bash

# check logs or use portainer
docker logs -f zabbix-db
docker logs -f zabbix-server
docker logs -f zabbix-agent
docker logs -f zabbix-web

# Run this command to see exactly which disk is holding your database files:
sudo df -h /datadrive/zabbix-data
Filesystem      Size  Used Avail Use% Mounted on
/dev/sdc1       8.0G  932M  7.1G  12% /datadrive

```

Or portainer

![portainer](https://github.com/spawnmarvel/learning-docker/blob/main/prod-ish-2/zabbix/zabbix-stack/images/portainer.png)


## 3 Access the Dashboard: Go to http://<your-server-ip>:8081

1. Initial Login
URL: http://<your-server-ip>:8081

Username: Admin (Capital 'A' is mandatory)

Password: zabbix

![run stack](https://github.com/spawnmarvel/learning-docker/blob/main/prod-ish-2/zabbix/zabbix-stack/images/run_stack3.png)

After a short while you will get an alert for Zabbix server

Zabbix server Linux: Zabbix agent is not available (for 3m)

* Edit the hostname to match the .env 	zabbixdocker
* DNS Name: Put zabbix-agent
* Connect to: Click the DNS button (this is the most important part)
* IP Address: Put 0.0.0.0 (or leave 127.0.0.1 there)
* Port: 10050
* Click Update

After short time, we geth the green host.

Why this works
When "Connect to" is set to DNS, Zabbix ignores the IP field and asks the Docker internal DNS "Where is the container named zabbix-agent?" Docker then provides the correct internal IP (like 172.20.0.x) automatically.

![zabbix_agent_green](https://github.com/spawnmarvel/learning-docker/blob/main/prod-ish-2/zabbix/zabbix-stack/images/zabbix_agent_green.png)


View usage in portainer for

zabbix-server

![stats server](https://github.com/spawnmarvel/learning-docker/blob/main/prod-ish-2/zabbix/zabbix-stack/images/stats_server.png)


zabbix-db

![stats db](https://github.com/spawnmarvel/learning-docker/blob/main/prod-ish-2/zabbix/zabbix-stack/images/stats_db.png)


If you need to enter a container you can use


portainer

![container](https://github.com/spawnmarvel/learning-docker/blob/main/prod-ish-2/zabbix/zabbix-stack/images/container.png)

or cli

```bash
docker exec -it zabbix-agent bash
zabbix@7b8d147eee27:~$ ls
buffer  enc  enc_internal  user_scripts
zabbix@7b8d147eee27:~$ cd /etc/zabbix/
zabbix@7b8d147eee27:/etc/zabbix$ ls
zabbix_agent2.conf  zabbix_agent2.d  zabbix_agentd.d

```

## Add ssl to zabbix docker

If you want to keep it simple and add the certificate directly to your zabbix-web container, we can do that by mounting the certificates and enabling the SSL port.


```bash
cd docker-zabbix-stack/

docker compose down

# we just need to edit ownership on the datadrive
sudo systemctl stop docker
sudo systemctl stop docker.socket

# Kill any "Zombie" processes
sudo fuser -mk /datadrive

# Run the ownership fix now
sudo chown -R $USER:$USER /datadrive
sudo chmod -R 755 /datadrive

ls -la /datadrive/zabbix-data
total 4
drwxr-xr-x  4 imsdal imsdal   44 Jan 18 20:54 .
drwxr-xr-x 12 imsdal imsdal  191 Jan 28 14:51 ..
drwxr-xr-x  8 imsdal imsdal 4096 Jan 28 15:03 zabbix-db
drwxr-xr-x  4 imsdal imsdal   49 Jan 18 20:54 zabbix-server

sudo systemctl start docker
cd docker-zabbix-stack/
docker compose up -d

# ssl
sudo mkdir -p /datadrive/zabbix-data/ssl

sudo su

cd /datadrive/zabbix-data/ssl

openssl req -x509 -nodes -days 3650 -newkey rsa:2048 \
  -keyout zabbix.key \
  -out zabbix.crt \
  -subj "/C=NO/ST=Oslo/L=Oslo/O=Zabbix/CN=zabbixdocker"

chmod 644 zabbix.crt
chmod 600 zabbix.key

cd docker-zabbix-stack/

sudo nano compose.yml
# paste yml

docker compose up -d


```

log

```
WARN[0000] No services to build
[+] up 4/4
 ✔ Container zabbix-db     Running                                                                                 0.0s
 ✔ Container zabbix-server Running                                                                                 0.0s
 ✔ Container zabbix-agent  Running                                                                                 0.0s
 ✔ Container zabbix-web    Recreated                                                                               1.4s
Error response from daemon: failed to set up container networking: driver failed programming external connectivity on endpoint zabbix-web (2cad3ff64b4105c296b10a156bfea81925c8316f69fb3b060f5d0eb5d95b219d): Bind for 0.0.0.0:443 failed: port is already allocated

```

```bash
docker ps
CONTAINER ID   IMAGE                          COMMAND                  CREATED       STATUS          PORTS                                                                                                NAMES
26a5cb204257   docker-portainer-portainer     "/portainer -p 9443 …"   10 days ago   Up 13 minutes   0.0.0.0:8000->8000/tcp, [::]:8000->8000/tcp, 0.0.0.0:9443->9443/tcp, [::]:9443->9443/tcp, 9000/tcp   portainer-app
217c3c9eba5b   docker-grafana-mysql-grafana   "/run.sh"                6 weeks ago   Up 13 minutes   0.0.0.0:443->3000/tcp, [::]:443->3000/tcp                                                            grafana
628b027ee1cc   mysql:8.0                      "docker-entrypoint.s…"   6 weeks ago   Up 13 minutes   3306/tcp, 33060/tcp                                                                                  grafana_db


```
Mystery solved! Look at your grafana container:

0.0.0.0:443->3000/tcp

```bash

# The Solution: Change the Zabbix SSL Port
# Since Grafana is already using 443, let's move Zabbix to 8443. This is the standard "alternative" HTTPS port.

# Open nsg 8443

nano docker-compose.yml
ports:
  - "8081:8080"
  - "8443:8443"  # Change the first number from 443 to 8443

docker compose up -d

```
log

```log
WARN[0000] No services to build
[+] up 5/5
 ✔ Network docker-zabbix-stack_default Created                                                                     0.1s
 ✔ Container zabbix-db                 Created                                                                     0.3s
 ✔ Container zabbix-server             Created                                                                     0.2s
 ✔ Container zabbix-agent              Created                                                                     0.4s
 ✔ Container zabbix-web                Created                                                                     0.4s

```

Go to:

https://<YOUR_VM_IP>:8443 did not work, check container



log inside zabbix-web check portainer or 

```bash
docker logs zabbix-web

```
logs

```log
Wed Jan 28 15:26:52.370914 2026] [ssl:emerg] [pid 35:tid 125602953664384] (13)Permission denied: AH02574: Init: Can't open server private key file /etc/ssl/apache2/ssl.key

[Wed Jan 28 15:26:52.370981 2026] [ssl:emerg] [pid 35:tid 125602953664384] AH02312: Fatal error initialising mod_ssl, exiting.

[Wed Jan 28 15:26:52.370984 2026] [ssl:emerg] [pid 35:tid 125602953664384] AH02564: Failed to configure encrypted (?) private key zabbix:8443:0, check /etc/ssl/apache2/ssl.key

AH00016: Configuration Failed
```

```bash

# Set the group to 'docker' or just make it globally readable for this lab
sudo chmod 644 /datadrive/zabbix-data/ssl/zabbix.key
sudo chmod 644 /datadrive/zabbix-data/ssl/zabbix.crt

sudo su
ls -l /datadrive/zabbix-data/ssl/
 ls -l /datadrive/zabbix-data/ssl/
total 8
-rw-r--r-- 1 root root 1285 Jan 28 15:14 zabbix.crt
-rw-r--r-- 1 root root 1704 Jan 28 15:14 zabbix.key

# run it
docker compose down

docker compose up -d

```

Go to:

https://<YOUR_VM_IP>:8443

And check container



## 5 update zabbix config

Since you are running Zabbix in Docker, you never edit the config files inside the container manually (like we did with cat earlier). If the container restarts, those changes disappear.

Instead, you manage everything through the compose.yml and .env files.

Actually, you don't even need to run docker compose down! Docker is smart enough to perform a "rolling update." When you run up -d after editing your files, Docker compares the new config to the running containers and only restarts the ones that changed.

Here is exactly how to do it.

1. Update your .env file
Add the new variable for Trappers to your .env so you can keep your compose.yml clean.

.env

```ini
# ... existing variables ...
ZBX_STARTPINGERS=3
ZBX_STARTTRAPPERS=5
```
2. Update the zabbix-server in compose.yml
Add the mapping for the Trappers variable under the environment: section of the zabbix-server service.

```yml
# Zabbix Server 7.0
  zabbix-server:
    # ... other settings ...
    environment:
      - DB_SERVER_HOST=zabbix-db
      - MYSQL_DATABASE=${MYSQL_DATABASE}
      - MYSQL_USER=${MYSQL_USER}
      - MYSQL_PASSWORD=${MYSQL_PASSWORD}
      - MYSQL_ROOT_PASSWORD=${MYSQL_ROOT_PASSWORD}
      - ZBX_STARTPINGERS=${ZBX_STARTPINGERS}
      - ZBX_STARTTRAPPERS=${ZBX_STARTTRAPPERS} # <--- Add this line
    # ... rest of service ...

```

3. Apply the changes
Just run this command. It will detect the change in the Server environment and restart only that container:

```bash
docker compose up -d
```

4. Verify the change is active
You can verify that the Zabbix Server has actually started 5 trapper processes without even looking at the Web UI. Run this from your terminal:

```bash
docker exec -it zabbix-server ps aux | grep trapper
```

## 5 most critical environment variables to tune in your zabbix-server section

Since you're planning to add more hosts, would you like me to give you a list of the 5 most important environment variables for performance tuning?

1. ZBX_STARTPOLLERS
What it does: Controls how many "Passive" workers are reaching out to agents to ask for data.

When to increase: When the ZBX icon stays gray or logs show "intermittent" data.

Recommended for growth: 10 to 20.

2. ZBX_CACHESIZE
What it does: The amount of RAM dedicated to storing host, item, and trigger data.

When to increase: If you see the "Zabbix configuration cache, % free" trigger in your dashboard.

Recommended for growth: 32M to 64M.

3. ZBX_STARTPINGERS
What it does: Dedicated workers for ICMP (Ping) checks.

When to increase: If you are monitoring many network devices or using "ICMP Ping" templates and the response time looks delayed.

Recommended for growth: 5 to 10.

4. ZBX_HISTORYCACHESIZE
What it does: The "waiting room" for data before it is written to the MySQL database.

When to increase: If you have high-frequency items (checking every 1–5 seconds).

Recommended for growth: 16M to 32M.

5. ZBX_STARTDBSYNCERS
What it does: These are the workers that take data from the cache and write it to the disk.

When to increase: If your docker stats shows high CPU but the database is idle; it means data is stuck in the middle.

Recommended for growth: 4 (Default is usually enough for up to 100 hosts).

## 6 Send push and pull / active and passive

Now lets send some data to zabbix in docker
