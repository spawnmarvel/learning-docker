# Learn and test Grafana in Docker

Grafana is just a toool for visualize stuff

* Grafana
* MySql backend for settings, config, users, etc

# Plugins

## Zabbix Plugin (Get data from Zabbix)

1. Grafana contacts the Zabbix API (running on your Zabbix server).
2. Zabbix translates the request and fetches the data from its internal database.
3. Grafana displays the result.

Step 1: Install the Plugin in your Dockerfile
You need to add a command to your Dockerfile_grafana to install the plugin during the image build process.

In your Dockerfile_grafana, add this line:

```bash
docker compose down

# Dockerfile_grafana (Add this line before the final commands)
RUN grafana-cli plugins install alexanderzobnin-zabbix-app

docker compose up -d --build

```
Once the build is complete, the Zabbix plugin will be permanently installed in your custom Grafana image, and you can proceed to configure it in the Grafana UI.

Plugins and data

* Plugins, search for zabbix, install and enable.
* Connections, Data sources

URL
* https://192.168.3.5/zabbix/api_jsonrpc.php
* Basic auth, setup login for access to Zabbix API
* grafana1, Echolima12Tango-

Zabbix connection
* grafana1, Echolima12Tango-

![grafana data source](https://github.com/spawnmarvel/learning-docker/blob/main/prod-ish-2/grafana-mysql/images/zabbix_data_source.png)

We can now choose it.

![use zabbix](https://github.com/spawnmarvel/learning-docker/blob/main/prod-ish-2/grafana-mysql/images/use_zabbix.png)

And view data on the fly and save dasboards.

![use zabbix](https://github.com/spawnmarvel/learning-docker/blob/main/prod-ish-2/grafana-mysql/images/use_zabbix.png)


https://grafana.com/docs/plugins/alexanderzobnin-zabbix-app/latest/configuration/



## 

# Inputs

## 