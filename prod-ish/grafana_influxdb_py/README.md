# Grafana

## Docs

https://grafana.com/docs/grafana/latest/setup-grafana/configure-docker/

## Connect Azure Table Storage

https://stackoverflow.com/questions/74194700/azure-table-storage-data-source-for-grafana

Please add as answer if you find any workarounds like piping from Table Store to an intermediatory low priced store which is supported by Grafana

## Middle store influxdb

```bash
docker compose up -d
```

Grafana ships with built-in support for InfluxDB releases >0.9.x.

https://grafana.com/grafana/plugins/influxdb/

## influxdb

```bash
pip install influxdb

```
We create a usedefined network in docker, so the ip does not change.

```yml
networks:
      static_network:
        ipv4_address: 172.27.0.2
```

## Grafana get data oink (tested first with mongodb)

Enterprise License Error
The Enterprise data source grafana-mongodb-datasource is not available with your current subscription. To activate this data source, please upgrade your plan by visiting https://grafana.com/pricing
license token file not found: /var/lib/grafana/license.jwt

## InfluxDB

pip install influxdb

```py
python3 run_influx.py

```

Now connect with grafana

https://www.mongodb.com/docs/manual/reference/connection-string/








