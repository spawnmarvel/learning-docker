# Zabbix

Could you make a compose.yml for zabbix with local agent, but no proxy and mysql?

Could you make a compose.yml for zabbix version 6 with local agent, but no proxy and mysql?

## Vicuna


### compose1

Could you make a compose.yml for zabbix version 6 with local agent, but no proxy and mysql?

Here is a docker compose file for Zabbix version 6 with a local Zabbix agent, MySQL database, and no proxy:

Compose1.yml


The key differences from Zabbix 5.x:

Use Zabbix 6.0 images
MySQL 8.0 instead of 5.7
No Zabbix proxy service
Otherwise it follows the same pattern of Zabbix server, MySQL database, and local Zabbix agent.


### compose2

Sure, here is a simple example of docker-compose.yml file that starts Zabbix server with MySQL database and Zabbix agent:

compose2.yml

This docker-compose.yml file creates three services: zabbix-server, mysql-server, and zabbix-agent.

The Zabbix server and agent services are using the latest Zabbix 6.0 images. The MySQL service is using a MySQL 8.0 image. The Zabbix server and agent services depend on the MySQL service.

The Zabbix server and agent services are configured using environment variables. The MySQL service is also configured using environment variables, and its data is stored in a Docker volume.

Please adjust the MySQL root password and other environment variables as per your needs.