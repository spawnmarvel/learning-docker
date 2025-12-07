# Grafana and MySql


## Grafana docker run test (http, https)

On dmzdocker03

```bash
docker run -d -p 3000:3000 --name=grafana grafana/grafana

```

* Grafana Open Source: grafana/grafana
* admin, admin

https://grafana.com/docs/grafana/latest/setup-grafana/installation/docker/

http://xx.xx.xxx.90:3000/login

And we are in after open UFW 3000 and NSG 3000.

![grafana 101](https://github.com/spawnmarvel/learning-docker/blob/main/prod-ish-2/grafana-mysql/images/grafana_101.png)


Lets use the same cert as we have for portainer and enable https, view the portainer\portainer-app if you need to see ssl

```bash
docker ps
docker stop grafana
```

```bash
# Ensure both the certificate and key files are readable by everyone (644 permission)
sudo chmod 644 /etc/docker/ssl/portainer/portainer.crt
sudo chmod 644 /etc/docker/ssl/portainer/portainer.key
```

New run cmd, make a bash script

```bash

sudo nano grafana-run-https.sh

```
Add the code below

```bash
#!/bin/bash
docker run -d -p 443:3000 --name=grafana -v /etc/docker/ssl/portainer/portainer.crt:/certs/portainer.crt -v /etc/docker/ssl/portainer/portainer.key:/certs/portainer.key -e "GF_SERVER_PROTOCOL=https" -e "GF_SERVER_CERT_FILE=/certs/portainer.crt" -e "GF_SERVER_CERT_KEY=/certs/portainer.key" grafana/grafana
```

Run it

```bash
# Make it Executable: Grant execution permission to the script file.
sudo chmod +x grafana-run-https.sh

grafana-run-https.sh
```

Now visit it

https://xx.xxx.xxx.90/login

Enter the console to verify certs moved

![grafana 101 https](https://github.com/spawnmarvel/learning-docker/blob/main/prod-ish-2/grafana-mysql/images/grafana_101_https.png)

## Grafana docker compose https

On dmzdocker03

```bash
mkdir docker-grafana-mysql
cd docker-grafana-mysql

```
Generate ssl certificate

Create a directory to store your certificates within your project folder (next to your docker-compose.yml file

```bash
mkdir certs
cd certs

pwd
# /home/imsdal/docker-grafana-mysql/certs

# Provides the subject information (Common Name CN should match the hostname, e.g., localhost or your domain).
sudo openssl req -x509 -newkey rsa:4096 -keyout grafana.key -out grafana.crt -days 730 -nodes -subj "/C=US/ST=State/L=City/O=OrgName/CN=grafanaserver"

# Why 644? The COPY command needs to read the file, and 644 grants read permissions to everyone, ensuring the Docker builder can access it.

sudo chmod 644 grafana.crt
sudo chmod 644 grafana.key

```
Run compose up

```bash

# folder /home/imsdal/docker-grafana-mysql
# add the Dockerfile Dockerfile_grafana, here we specify version and move the certs to the container
# add the compose.yml

ls
Dockerfile_grafana  certs  compose.yml

docker compose up -d --build


```

http://xx.xx.xxx.90:3000/login

![grafana compose https](https://github.com/spawnmarvel/learning-docker/blob/main/prod-ish-2/grafana-mysql/images/grafana_compose_https.png)




## Mysql as backend using secret

Read and list properties


https://hub.docker.com/_/mysql


On dmzdocker03

You absolutely can and should use Docker's built-in secrets mechanism to avoid storing passwords in plaintext environment variables within your docker-compose.yaml file.

1. Create Secret Files on Host
In your project directory (the same location as your docker-compose.yaml), create the following files with the actual secure passwords inside:

```bash
cd docker-grafana-mysql

# Create files and write your secure passwords to them
echo "your_secure_db_password" > db_password.txt
echo "your_secure_admin_password" > grafana_admin_password.txt

# (Recommended: Restrict file permissions)
chmod 600 *.txt

docker compose up --build -d

# Verify that services are running:

docker compose ps

# Verify Grafana Log (Database Connection)

docker compose logs grafana


```

Now visit grafana, https://localhost (or https://<Your Host IP>)

### Check Secrets (Security Verification)

To confirm that your passwords are not exposed as environment variables, inspect the running Grafana container's environment:

```bash
docker inspect grafana | grep -E 'GF_DATABASE_PASSWORD|GF_SECURITY_ADMIN_PASSWORD'
```
You should not see the actual password value; you should only see the _FILE environment variables:
