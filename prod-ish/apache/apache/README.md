# docker run apache

To run an Apache web server in a Docker container using the `docker run` command, you can use the official Apache HTTP Server image from Docker Hub. Here's the basic command and a breakdown of its parts:

**Basic Command:**

```bash
docker run -d -p 80:80 --name my-apache httpd:latest
```

**Explanation:**

* **`docker run`**: This is the main command to start a new container from an image.
* **`-d` (Detached Mode)**: This flag tells Docker to run the container in the background. Your terminal will return immediately after the container starts.
* **`-p 80:80` (Port Mapping)**: This maps port 80 on your host machine to port 80 inside the container. This allows you to access the Apache web server by visiting `http://localhost` (or your host machine's IP address) in your browser.
* **`--name my-apache` (Container Name)**:  This assigns a name to the container, making it easier to manage. You can choose any name you like.
* **`httpd:latest` (Image Name and Tag)**: This specifies the Docker image to use. `httpd` is the name of the official Apache image, and `latest` refers to the latest available version.

**How to Use It:**

1. **Run the command:** Execute the `docker run` command in your terminal.
2. **Access the server:** Open a web browser and navigate to `http://localhost` (or your host machine's IP address). You should see the default Apache "It Works!" page.

```bash
# msd
docker ps
CONTAINER ID   IMAGE                           COMMAND              CREATED         STATUS             PORTS                                                                                            NAMES
f61087976986   httpd:latest                    "httpd-foreground"   7 seconds ago   Up 6 seconds       0.0.0.0:80->80/tcp, :::80->80/tcp                                                                my-apache
```


![It works apache ](https://github.com/spawnmarvel/learning-docker/blob/main/prod-ish/apache/apache/z_img_apache_works.jpg)

```bash

# enter apache
docker exec -it my-apache sh

```

**Customization:**

* **Serving Custom Content:** By default, the container serves files from the `/usr/local/apache2/htdocs/` directory within the container. To serve your own content, you can mount a local directory as a volume:

   ```bash
   docker run -d -p 80:80 --name my-apache -v /path/to/your/files:/usr/local/apache2/htdocs/ httpd:latest
   ```

   Replace `/path/to/your/files` with the actual path to the directory containing your website files.

* **Specific Apache Version:** To use a specific version of Apache, replace `latest` with the desired tag. For example, to use Apache 2.4:

   ```bash
   docker run -d -p 80:80 --name my-apache httpd:2.4
   ```

* **Custom Configuration:** You can create a custom Apache configuration file and mount it into the container. See the Docker Hub documentation for the `httpd` image for more details on how to do this.

**Managing the Container:**

* **Stop the container:** `docker stop my-apache`
* **Start the container (if stopped):** `docker start my-apache`
* **Remove the container:** `docker rm my-apache` (This will delete the container. Make sure you don't need any data inside it before removing.)

This provides a basic way to run an Apache web server in a Docker container. You can adapt the command and explore further options based on your specific requirements. Remember to check the official Docker Hub documentation for the `httpd` image for more detailed instructions and configuration options.

## Apache 2.4

Specific Apache Version: To use a specific version of Apache, replace latest with the desired tag. For example, to use Apache 2.4:

```bash
docker run -d -p 80:80 --name my-apache httpd:2.4
```


## How to Use the Apache httpd Docker Official Image

https://www.docker.com/blog/how-to-use-the-apache-httpd-docker-official-image/


## 1,2,3 Dockerfile, compose.yaml, run docker-compose up -d


```bash
# 1 Define your app's environment with a Dockerfile so it can be reproduced anywhere.
# 2 Define the services that make up your app in compose.yaml so they can be run together in an isolated environment.
# 3 Lastly, run docker compose up and Compose will start and run your entire app.

```

Dockerfile

```bash
# Use the official Apache HTTP Server as the base image
FROM httpd:2.4

# Copy the custom Apache configuration file to the proper location in the container
COPY httpd.conf /usr/local/apache2/conf/httpd.conf

# Copy the website files for the virtual hosts into the web root inside the container
COPY www/example /usr/local/apache2/htdocs/example
```

Files:

```log
my-apache-project/
│
├── Dockerfile
├── docker-compose.yml
├── httpd.conf
└── www/
    ├── example/
    │   └── index.html
```
.html

```html
<html>
  <head><title>Example Website</title></head>
  <body><h1>Welcome to Example Website</h1></body>
</html>
```

compose.yml

```yaml

services:
  apache:
    build: .  # Build the Docker image using the Dockerfile in the current directory
    container_name: my-apache
    ports:
      - "80:80"

```

If you are using virtual hosts (ServerName directives), you need to add the following entries to your /etc/hosts file (on Linux or macOS) or C:\Windows\System32\drivers\etc\hosts file (on Windows) to resolve the domain names locally.

Add the lines to your hosts file:

```log
127.0.0.1 www.example.com
```

else commecnt out in httpd.conf


```log
# ServerName www.example.com
```



Run it, ,Run the following command in the project directory (my-apache-project/)

```bash

# --build: Forces Docker Compose to build the image using the Dockerfile.
docker compose up --build -d

docker compose down

# images
docker images

# force remove
docker rmi -f  d7e7351f5e15

```