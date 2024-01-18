# Zabbix

Could you make a compose.yml for zabbix with local agent, but no proxy and mysql?

## Vicuna

Here is a docker compose YAML file to deploy Zabbix with a local Zabbix agent, MySQL database, but no Zabbix proxy:

Compose1.yml


This defines 3 services:

zabbix-server - The Zabbix server with MySQL database
zabbix-database - MySQL database for Zabbix
zabbix-agent - Zabbix agent for local monitoring
No Zabbix proxy service is included. The Zabbix server connects directly to the Zabbix agent for monitoring.


Sure, here is a simple example of docker-compose.yml file that starts Zabbix server with MySQL database and Zabbix agent:

compose2.yml

This docker-compose.yml file creates three services: zabbix-server, mysql-server, and zabbix-agent.

The Zabbix server and agent services are using the latest Zabbix 4.2 images. The MySQL service is using a MySQL 5.7 image. The Zabbix server and agent services depend on the MySQL service.

The Zabbix server and agent services are configured using environment variables. The MySQL service is also configured using environment variables, and its data is stored in a Docker volume.

Please adjust the MySQL root password and other environment variables as per your needs.