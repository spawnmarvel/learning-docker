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


Now connect with grafana

https://www.mongodb.com/docs/manual/reference/connection-string/

## Pymongo

```bash
pip install pymongo
# Successfully installed dnspython-2.6.1 pymongo-4.6.2

# ping the docker host
 ping 172.27.0.2
PING 172.27.0.2 (172.27.0.2) 56(84) bytes of data.
64 bytes from 172.27.0.2: icmp_seq=1 ttl=64 time=0.056 ms
64 bytes from 172.27.0.2: icmp_seq=2 ttl=64 time=0.061 ms
64 bytes from 172.27.0.2: icmp_seq=3 ttl=64 time=0.058 ms
64 bytes from 172.27.0.2: icmp_seq=4 ttl=64 time=0.056 ms

```

```py
import pymongo
from pymongo import MongoClient
client = MongoClient("172.27.0.2", 27017)
print(str(client))

```

Run it, using private ip from container

```bash
python3 run.py
MongoClient(host=['172.27.0.2:27017'], document_class=dict, tz_aware=False, connect=True)

```

https://pymongo.readthedocs.io/en/stable/tutorial.html

```log
MongoClient(host=['172.27.0.2:27017'], document_class=dict, tz_aware=False, connect=True)
Database(MongoClient(host=['172.27.0.2:27017'], document_class=dict, tz_aware=False, connect=True), 'test-database')
Collection(Database(MongoClient(host=['172.27.0.2:27017'], document_class=dict, tz_aware=False, connect=True), 'test-database'), 'test-collection')
{'name': 'tag1', 'date': datetime.datetime(2024, 3, 26, 11, 59, 37, 514865, tzinfo=datetime.timezone.utc), 'value': 78}
{'name': 'tag1', 'date': datetime.datetime(2024, 3, 26, 11, 59, 37, 514904, tzinfo=datetime.timezone.utc), 'value': 78}
Insert
InsertOneResult(ObjectId('6602b8a9d30bebbfeb2c5772'), acknowledged=True)
InsertOneResult(ObjectId('6602b8a9d30bebbfeb2c5773'), acknowledged=True)
```





