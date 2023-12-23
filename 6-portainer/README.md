# Portainer

Portainer consists of two elements, the Portainer Server, and the Portainer Agent. Both elements run as lightweight Docker containers on a Docker engine.

* By default, Portainer Server will expose the UI over port 9443 and expose a TCP tunnel server over port 8000

https://docs.portainer.io/start/install-ce/server/docker/linux

## Install Portainer CE with Docker on Linux

```bash
# First, create the volume that Portainer Server will use to store its database:
docker volume create portainer_data

# Then, download and install the Portainer Server container:
docker run -d -p 8000:8000 -p 9443:9443 --name portainer --restart=always -v /var/run/docker.sock:/var/run/docker.sock -v portainer_data:/data portainer/portainer-ce:latest

docker ps
CONTAINER ID   IMAGE                           COMMAND        CREATED         STATUS         PORTS                                                                                            NAMES
635d80e430a3   portainer/portainer-ce:latest   "/portainer"   8 seconds ago   Up 7 seconds   0.0.0.0:8000->8000/tcp, :::8000->8000/tcp, 0.0.0.0:9443->9443/tcp, :::9443->9443/tcp, 9000/tcp   portainer
```
Open inbound NSG 9443

https://localhost:9443 Replace localhost with the relevant IP address or FQDN if needed, and adjust the port if you changed it earlier.


![Portainer](https://github.com/spawnmarvel/learning-docker/blob/main/images/portainer.jpg)

## Initial setup

Your first user will be an administrator.


Once the admin user has been created, the Environment Wizard will automatically launch. The wizard will help get you started with Portainer.

The installation process automatically detects your local environment and sets it up for you. If you want to add additional environments to manage with this Portainer instance, click Add Environments. Otherwise, click Get Started to start using Portainer!

Right now we have none.

![Portainer_env](https://github.com/spawnmarvel/learning-docker/blob/main/images/portainer_env.jpg)


https://docs.portainer.io/start/install-ce/server/setup


