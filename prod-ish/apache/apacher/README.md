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