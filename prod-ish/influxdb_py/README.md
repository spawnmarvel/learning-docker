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

Lets just verify influxdb

![Influxdb verify](https://github.com/spawnmarvel/learning-docker/blob/main/prod-ish/influxdb_py/images/verify_influx.jpg)


## influxdb has cool features now

Check it out.

![Influxdb features](https://github.com/spawnmarvel/learning-docker/blob/main/prod-ish/influxdb_py/images/influxdb_features.jpg)

```bash
docker compose u -d

```

## Load data

Sources
* So many, files, line protocol, influx cli, client libs, .net, dart, ryby, pyyhon, java.....
* Buckets, A bucket is a named location where time series data is stored. All buckets have a Retention Policy, a duration of time that each data point persists.
* Telegraf is an agent written in Go for collecting metrics and writing them into InfluxDB or other possible outputs.
* Scrapers

## Data explorer

* 

## Notebooks

## Task

## Alerts

## Settings

## Influxdb in a nutshell

InfluxDB 2.x Open Source Time Series Database
InfluxDB is an open source time series database. It has everything you need from a time series platform in a single binary – a multi-tenanted time series database, UI and dashboarding tools, background processing and monitoring agent. All this makes deployment and setup a breeze and easier to secure.

The InfluxDB Platform also includes APIs, tools, and an ecosystem that includes 10 client and server libraries, Telegraf plugins, visualization integrations with Grafana, Google Data Studio, and data sources integrations with Google Bigtable, BigQuery, and more.

https://www.influxdata.com/downloads/

## Key concepts before you get started

InfluxDB Cloud is the platform purpose-built to collect, store, process and visualize time series data. Time series data is a sequence of data points indexed in time order. Data points typically consist of successive measurements made from the same source and are used to track changes over time. Examples of time series data include:

* Industrial sensor data
* Server performance metrics
* Heartbeats per minute
* Electrical activity in the brain
* Rainfall measurements
* Stock prices

```py
b = influxdb_client.Point("my_measurement").tag("location", "Bergen").field("temperature", ran1)
write_api.write(bucket=bucket, org=org, record=b)
o = influxdb_client.Point("my_measurement").tag("location", "Oslo").field("temperature", (ran1+5))
write_api.write(bucket=bucket, org=org, record=o)
```

* The InfluxDB data model organizes time series data into buckets and measurements. A bucket can contain multiple measurements. Measurements contain multiple tags and fields.

* Bucket: Named location where time series data is stored. A bucket can contain multiple measurements
* * Measurement: Logical grouping for time series data. All points in a given measurement should have the same tags. A measurement contains multiple tags and fields.
* * * Tags: Key-value pairs with values that differ, but do not change often. Tags are meant for storing metadata for each point–for example, something to identify the source of the data like host, location, station, etc.
* * * Fields: Key-value pairs with values that change over time–for example: temperature, pressure, stock price, etc.
* * * Timestamp: Timestamp associated with the data. When stored on disk and queried, all data is ordered by time.


***Point: Single data record identified by its measurement, tag keys, tag values, field key, and timestamp.***

***Series: A group of points with the same measurement, tag keys and values, and field key.***


![Influxdb data](https://github.com/spawnmarvel/learning-docker/blob/main/prod-ish/influxdb_py/images/influxdb_data.jpg)

https://docs.influxdata.com/influxdb/cloud/get-started/










