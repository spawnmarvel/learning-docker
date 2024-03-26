# Grafana

## Docs

https://grafana.com/docs/grafana/latest/setup-grafana/configure-docker/

## Connect Azure Table Storage

https://stackoverflow.com/questions/74194700/azure-table-storage-data-source-for-grafana

Please add as answer if you find any workarounds like piping from Table Store to an intermediatory low priced store which is supported by Grafana

## Middle store

```bash
docker compose up -d

# compose.yml
# - GF_INSTALL_PLUGINS=grafana-mongodb-datasource

# enter container
/var/lib/grafana/plugins
ls
grafana-mongodb-datasource

```

MongoDB data source for Grafana

![Mongodb](https://github.com/spawnmarvel/learning-docker/blob/main/prod-ish/grafana_mongo_py/images/mongdb.jpg)


