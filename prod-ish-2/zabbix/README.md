# Zabbix Docker / Nemesis

## docker compose

Create a folder for your Zabbix stack and set up these two files:

zabbix-stack/
* .env
* compose.yaml


## 1. Build and launch the stack:

```bash
sudo nano compose.yml

compose up -d
```


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
Open NSG for the same port also.


## 2. Access the Dashboard: Go to http://<your-server-ip>:8081

1. Initial Login
URL: http://<your-server-ip>:8081

Username: Admin (Capital 'A' is mandatory)

Password: zabbix

*  Enable Docker Monitoring:

* In the Zabbix UI, go to Data collection > Hosts.

* Find the "Zabbix Docker Host" (or create it if it doesn't appear).

* Add the template: "Docker by Zabbix agent 2".

* Because you mapped /var/run/docker.sock, Zabbix will now automatically discover and monitor all other containers in this stack.

Key Improvements in this Setup
* MySQL 8.4 Compatibility: Included --log-bin-trust-function-creators=1 which is mandatory for Zabbix to create its database schema on first run.

* Apache vs Nginx: Switched to the apache-mysql image as requested.

* Agent 2: By using Agent 2 instead of the classic Agent, you get native support for the Docker monitoring plugin without needing external scripts.