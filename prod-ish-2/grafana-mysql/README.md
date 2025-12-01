# Grafana and MySql


## Grafana docker run (http, https)

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

```bash
mkdir docker-grafana-mysql

```

## Mysql

On dmzdocker03

```bash

```

