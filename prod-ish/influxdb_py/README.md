# Grafana (not sure if we need it influxdb has cool features now)

## Docs

https://grafana.com/docs/grafana/latest/setup-grafana/configure-docker/

## Connect Azure Table Storage

https://stackoverflow.com/questions/74194700/azure-table-storage-data-source-for-grafana

Please add as answer if you find any workarounds like piping from Table Store to an intermediatory low priced store which is supported by Grafana

## Grafana get data oink (tested first with mongodb)

Enterprise License Error
The Enterprise data source grafana-mongodb-datasource is not available with your current subscription. To activate this data source, please upgrade your plan by visiting https://grafana.com/pricing
license token file not found: /var/lib/grafana/license.jwt

## Middle store influxdb

Grafana ships with built-in support for InfluxDB releases >0.9.x.

https://grafana.com/grafana/plugins/influxdb/

# Docker

We create a usedefined network in docker, so the ip does not change.

```yml
networks:
      static_network:
        ipv4_address: 172.27.0.2
```

```bash
docker compose up -d
```

Ensure that InfluxDB is running. If running InfluxDB locally, visit http://localhost:8086


![Influxdb](https://github.com/spawnmarvel/learning-docker/blob/main/prod-ish/influxdb_py/images/influxdb.jpg)

sign in with
* - DOCKER_INFLUXDB_INIT_USERNAME=adminuser
* - DOCKER_INFLUXDB_INIT_PASSWORD=adminpassword

## influxdb InfluxDB (so many versions and clients, 1.8, 2>, 3>)

```bash
pip install influxdb-client

python3 run_influx.py

Failed to establish a new connection: [Errno 111] Connection refused

telnet 172.27.0.2 8086
Trying 172.27.0.2...
Connected to 172.27.0.2.

# updated URL to use
url="http://172.27.0.2:8086"

# All good
```

Python example

https://docs.influxdata.com/influxdb/cloud/api-guide/client-libraries/python/

## Insert data

```bash
python3 run_influx.py

```

![Influxdb insert](https://github.com/spawnmarvel/learning-docker/blob/main/prod-ish/influxdb_py/images/influxdb_insert.jpg)



## Docker down

```bash
docker compose down

docker compose u -d

#no data

# https://community.influxdata.com/t/influxdb-image-do-not-persist-data-in-docker-volume-docker-compose-stack/31193
# If you’re running an InfluxDB version that’s 2.x or newer, the data is stored in /var/lib/influxdb2. If you’re using this version, modify your volume mapping like this: - vol_influxdb:/var/lib/influxdb2

# Test again after rm image / volume and insert data

docker compose down

python3 run.py

docker compose u -d
```

And yea, data and dashboard is there.

## ACI Registry

Ref https://github.com/spawnmarvel/learning-docker/blob/main/2-azure-container-instance/Readme-container-registry.md

Here we deployed RMQ with just a Dockerfile and

```bash
az container create --resource-group
                    [--acr-identity]
                    [--add-capabilities]
                    [--allow-escalation]
                    [--assign-identity]
                    [--azure-file-volume-account-key]
                    [...]


```
 lets use the containerapp

```bash
az containerapp compose create --environment
                               --resource-group
                               [--compose-file-path]
                               [--location]
                               [--registry-password]
                               [--registry-server]
                               [--registry-username]
                               [--tags]
                               [--transport]
                               [--transport-mapping]
```
to deploy a influxdb with a compose file.

Lets just verify influxdb

![Influxdb verify](https://github.com/spawnmarvel/learning-docker/blob/main/prod-ish/influxdb_py/images/verify_influx.jpg)


## influxdb has cool features now

Check it out.

![Influxdb features](https://github.com/spawnmarvel/learning-docker/blob/main/prod-ish/influxdb_py/images/influxdb_features.jpg)

```bash
docker compose u -d

```

## Load data

## Data explorer

## Notebooks

## Task

## Alerts

## Settings






