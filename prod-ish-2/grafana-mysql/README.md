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


Lets use the same cert as we have for portainer and enable https

```bash
docker ps
docker stop grafana
```

New run cmd

```bash
docker run -d -p 3000:3000 --name=grafana grafana/grafana
```

## Grafana docker compose https

```bash
mkdir docker-grafana-mysql

```

## Mysql

On dmzdocker03

```bash

```

