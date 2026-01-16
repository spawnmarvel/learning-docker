# Zabbix Docker / Nemesis

## docker compose

1. Launch the stack:

```bash
docker-compose up -d
```

2. Access the Dashboard: Go to http://your-ip-address.

3. Default Credentials: * User: Admin

* Password: zabbix

4. Enable Docker Monitoring:

* In the Zabbix UI, go to Data collection > Hosts.

* Find the "Zabbix Docker Host" (or create it if it doesn't appear).

* Add the template: "Docker by Zabbix agent 2".

* Because you mapped /var/run/docker.sock, Zabbix will now automatically discover and monitor all other containers in this stack.

Key Improvements in this Setup
* MySQL 8.4 Compatibility: Included --log-bin-trust-function-creators=1 which is mandatory for Zabbix to create its database schema on first run.

* Apache vs Nginx: Switched to the apache-mysql image as requested.

* Agent 2: By using Agent 2 instead of the classic Agent, you get native support for the Docker monitoring plugin without needing external scripts.