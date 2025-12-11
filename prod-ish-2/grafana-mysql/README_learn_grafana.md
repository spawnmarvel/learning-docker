# Learn and test Grafana in Docker

Grafana is just a toool for visualize stuff

* Grafana
* MySql backend for settings, config, users, etc

## Key Functions of Grafana Beyond Visualization

* Data Integration and Querying: Grafana does not store data itself but acts as a unified interface to query data from a vast range of sources, including Prometheus, InfluxDB, MySQL, PostgreSQL, Elasticsearch, and various cloud services like AWS CloudWatch and Azure Monitor.
* Alerting and Notifications: Users can set up complex alert rules and thresholds based on specific metrics and conditions. When these rules are triggered, Grafana can send notifications through various channels like email, Slack, PagerDuty, and more, allowing teams to quickly detect and address issues.
* Monitoring: Grafana is widely used for real-time monitoring of system and application performance, infrastructure health, logs, business metrics, and more. It allows teams to track performance bottlenecks, error rates, and resource usage to ensure system reliability.
* Analysis and Correlation: It provides advanced features for data transformation, ad-hoc querying, and dynamic drill-downs, enabling users to analyze data and uncover the root causes of issues by switching between metrics, logs, and traces in a single interface.
* Collaboration and Reporting: Grafana allows teams to create, explore, and share dynamic dashboards, fostering a data-driven culture.
* Extensibility: Through a rich plugin ecosystem, users can extend Grafana's capabilities with additional data sources, new visualization types, and custom integrations, including AI-powered features for query assistan

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

![use zabbix data](https://github.com/spawnmarvel/learning-docker/blob/main/prod-ish-2/grafana-mysql/images/zabbix_data_linux.png)

dmzdocker03 dasboard

![dmzdocker dashboard](https://github.com/spawnmarvel/learning-docker/blob/main/prod-ish-2/grafana-mysql/images/dmzdocker03_dash.png)


https://grafana.com/docs/plugins/alexanderzobnin-zabbix-app/latest/configuration/



## Plugin

## Plugin
