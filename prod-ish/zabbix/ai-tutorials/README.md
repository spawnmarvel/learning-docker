# How to run zabbix, zabbix agent, mysql and apache in docker make it as a tutorial, step by step

## ## Running Zabbix, Zabbix Agent, MySQL, and Apache in Docker: A Step-by-Step Tutorial

This tutorial will guide you through setting up a Zabbix monitoring system with its agent, database (MySQL), and web server (Apache) using Docker Compose.

**Prerequisites:**

* Docker and Docker Compose installed on your system.

**Step 1: Create the Docker Compose File**

Create a file named `docker-compose.yml` in a directory of your choice. Add the following content:

```yaml
version: "3.8"

services:
  mysql:
    image: mysql:8.0
    container_name: zabbix-mysql
    environment:
      MYSQL_ROOT_PASSWORD: your_password  # Replace with a strong password
      MYSQL_DATABASE: zabbix
    volumes:
      - mysql-data:/var/lib/mysql
    restart: always

  zabbix-server:
    image: zabbix/zabbix-server-mysql:latest
    container_name: zabbix-server
    ports:
      - "10051:10051"
    environment:
      DB_SERVER_HOST: mysql
      MYSQL_USER: root
      MYSQL_PASSWORD: your_password  # Same password as above
      MYSQL_DATABASE: zabbix
    volumes:
      - /etc/localtime:/etc/localtime:ro
    depends_on:
      - mysql
    restart: always

  zabbix-web-apache:
    image: zabbix/zabbix-web-apache-mysql:latest
    container_name: zabbix-web
    ports:
      - "80:80"
    environment:
      ZBX_SERVER_HOST: zabbix-server
      DB_SERVER_HOST: mysql
    depends_on:
      - zabbix-server
    restart: always

  zabbix-agent:
    image: zabbix/zabbix-agent2:latest
    container_name: zabbix-agent
    environment:
      ZBX_SERVER_HOST: zabbix-server
    ports:
      - "10050:10050"
    depends_on:
      - zabbix-server
    restart: always

volumes:
  mysql-data:
```

**Important:** Replace `your_password` with a strong password for your MySQL database.

**Step 2: Start the Services**

Open a terminal in the directory where you saved `docker-compose.yml` and run:

```bash
docker-compose up -d
```

This command downloads the necessary images and starts all the services in the background.

**Step 3: Access the Zabbix Web Interface**

Open a web browser and navigate to `http://localhost` (or the IP address of your Docker host). You should see the Zabbix setup wizard.

**Step 4: Complete the Zabbix Setup**

Follow the wizard instructions to complete the Zabbix installation:

* **Check Prerequisites:** Ensure all requirements are met.
* **Configure Database Connection:**
    * Database type: MySQL
    * Database host: mysql
    * Database port: 3306
    * Database name: zabbix
    * User: root
    * Password: `your_password` (the one you set in the compose file)
* **Zabbix Server Details:**
    * Host: zabbix-server
    * Port: 10051
* **Name and Timezone:** Provide a name for your installation and select your timezone.
* **Finish:** Review the summary and complete the installation.

**Step 5: Login to Zabbix**

After setup, you'll be redirected to the login page. The default username is `Admin` and the password is `zabbix`.

**Step 6: Verify Agent Connectivity**

In the Zabbix web interface:

* Go to **Configuration** > **Hosts**.
* You should see the `zabbix-server` host already added.
* Click on its name to check its status.
* The Availability icon (ZBX) should be green, indicating the agent is connected.

**Explanation of the Docker Compose File:**

* **Services:** Defines the containers to be run (MySQL, Zabbix Server, Web, Agent).
* **Image:** Specifies the Docker image to use for each service.
* **Container Name:** Sets a custom name for each container.
* **Ports:** Maps ports from the container to the host system.
* **Environment:** Sets environment variables for the containers (database credentials, server hostnames).
* **Volumes:** Persists data from the MySQL container (using `mysql-data`).
* **Depends_on:** Ensures containers start in the correct order (e.g., Zabbix Server starts after MySQL).
* **Restart:**  Automatically restarts containers if they fail.

**Further Steps:**

* **Change default password:**  Change the default Zabbix password after login.
* **Add more hosts:** Configure the Zabbix Agent on other servers to monitor them.
* **Customize configuration:**  Explore the Zabbix documentation for advanced configuration options.

This tutorial provides a foundation for running a basic Zabbix setup with Docker Compose. You can customize it further to meet your specific monitoring needs. Remember to secure your setup by using strong passwords and limiting access as needed.

