# The first tutorial 1 is docker run, the second 2 is docker compose

# 1 how to run zabbix, zabbix agent, mysql and apache in docker make it as a tutorial, step by step, not using compose but only docker run

## Running Zabbix, Zabbix Agent, MySQL, and Apache in Docker using `docker run`

This tutorial guides you through setting up a Zabbix monitoring environment with its agent, database (MySQL), and web server (Apache) using individual `docker run` commands instead of Docker Compose. This approach gives you more control over individual container configurations but requires more manual setup.

**Prerequisites:**

* Docker installed on your system.

**Step 1: Create a Docker Network**

This network will allow your containers to communicate with each other by name.

```bash
docker network create zabbix-net

# me, list networks

docker network ls
NETWORK ID     NAME                          DRIVER    SCOPE
8e6e8e33bdba   bridge                        bridge    local
16e4c0c05bc5   host                          host      local
ca34d5e024b2   imsdal_default                bridge    local
0d5aff734251   none                          null      local
3e7a07ccf429   portainer-app_net_portainer   bridge    local
286d4fe9a2f6   zabbix-net                    bridge    loca
```

**Step 2: Run the MySQL Container**

```bash
docker run -d --name zabbix-mysql \
  --network zabbix-net \
  -e MYSQL_ROOT_PASSWORD=your_password \
  -e MYSQL_DATABASE=zabbix \
  -v mysql-data:/var/lib/mysql \
  mysql:8.0

# me, paste it in. It will pull what it needs
docker image ls
REPOSITORY               TAG       IMAGE ID       CREATED         SIZE
mysql                    8.0       9f4b39935f20   3 weeks ago     590MB

docker container ps
CONTAINER ID   IMAGE                           COMMAND                  CREATED              STATUS              PORTS                                                                                            NAMES
6687d08f355f   mysql:8.0                       "docker-entrypoint.s…"   About a minute ago   Up About a minute   3306/tcp, 33060/tcp                                                                              zabbix-mysql

```

**Important:** Replace `your_password` with a strong password.

**Step 3: Run the Zabbix Server Container**

```bash
docker run -d --name zabbix-server \
  --network zabbix-net \
  -p 10051:10051 \
  -e DB_SERVER_HOST=zabbix-mysql \
  -e MYSQL_USER=root \
  -e MYSQL_PASSWORD=your_password \
  -e MYSQL_DATABASE=zabbix \
  -v /etc/localtime:/etc/localtime:ro \
  zabbix/zabbix-server-mysql:latest

# me, paste it in. It will pull what it needs
 docker image ls
REPOSITORY                   TAG       IMAGE ID       CREATED         SIZE
zabbix/zabbix-server-mysql   latest    1b3dce144ce3   2 weeks ago     138MB
mysql                        8.0       9f4b39935f20   3 weeks ago     590MB

 docker ps
CONTAINER ID   IMAGE                               COMMAND                  CREATED          STATUS          PORTS                                                                                            NAMES
d9534aba6745   zabbix/zabbix-server-mysql:latest   "/usr/bin/docker-ent…"   33 seconds ago   Up 33 seconds   0.0.0.0:10051->10051/tcp, :::10051->10051/tcp                                                    zabbix-server
6687d08f355f   mysql:8.0                           "docker-entrypoint.s…"   2 minutes ago    Up 2 minutes    3306/tcp, 33060/tcp                                                                              zabbix-mysql

```

**Step 4: Run the Zabbix Web (Apache) Container**

```bash
docker run -d --name zabbix-web \
  --network zabbix-net \
  -p 80:80 \
  -e ZBX_SERVER_HOST=zabbix-server \
  -e DB_SERVER_HOST=zabbix-mysql \
  zabbix/zabbix-web-apache-mysql:latest
```

**Step 5: Run the Zabbix Agent Container**

```bash
docker run -d --name zabbix-agent \
  --network zabbix-net \
  -p 10050:10050 \
  -e ZBX_SERVER_HOST=zabbix-server \
  zabbix/zabbix-agent2:latest
```

**Step 6: Complete the Zabbix Setup**

Now, open a web browser and navigate to `http://localhost` (or the IP address of your Docker host). You'll be greeted by the Zabbix setup wizard. Follow the on-screen instructions, using the following details for the database connection:

* **Database type:** MySQL
* **Database host:** zabbix-mysql (container name, thanks to the network)
* **Database port:** 3306
* **Database name:** zabbix
* **User:** root
* **Password:** `your_password`

For the Zabbix server details, use:

* **Host:** zabbix-server (container name)
* **Port:** 10051

Complete the remaining steps of the wizard and login to Zabbix with the default credentials (Admin/zabbix).

**Step 7: Verify Agent Connectivity**

In the Zabbix web interface:

* Go to **Configuration** > **Hosts**.
* You should see the `zabbix-server` host.
* Check its status. The Availability icon (ZBX) should be green, indicating the agent is connected.

**Key Considerations:**

* **Data Persistence:** The `-v mysql-data:/var/lib/mysql` in the MySQL command ensures data persists even if the container is removed. You can use named volumes for other containers as well.
* **Manual Management:** You need to manually manage each container (start, stop, etc.).
* **Networking:** The `zabbix-net` network allows containers to resolve each other by name, simplifying communication.
* **Security:**  Consider using stronger passwords and limiting exposed ports for a production environment.

**Using `docker run` commands offers flexibility but demands careful management. If you plan on running a more complex or production-ready setup, using Docker Compose is highly recommended as it simplifies the process of managing dependencies and configuration.**


# 2 How to run zabbix, zabbix agent, mysql and apache in docker make it as a tutorial, step by step

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

