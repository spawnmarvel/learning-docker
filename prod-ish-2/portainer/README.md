# Portainer-ce

https://docs.portainer.io/start/install-ce/server/docker/linux

## Set up

You can deploy portainer as its on container or with other containers in the compose.yml.

View frontpage or main readme section

https://github.com/spawnmarvel/learning-docker/blob/main/README.md#set-up-portainer-https-done-2

## portainer-ce as one contaier https


Generate ssl certificate

```bash
mkdir mkdir docker-portainer
cd mkdir docker-portainer
mkdir certs
cd certs

# Ensure you are in the directory containing the 'certs' folder
openssl req -x509 -nodes -days 730 -newkey rsa:2048 -keyout portainer.key -out portainer.crt -subj "/C=US/ST=State/L=City/O=PortainerTest/CN=portainer.local"

# Why 644? The COPY command needs to read the file, and 644 grants read permissions to everyone, ensuring the Docker builder can access it.

sudo chmod 644 portainer.crt
sudo chmod 644 portainer.key

```

Run portainer

```bash
cd mkdir docker-portainer
ls
Dockerfile_portainer  certs  compose.yml

# copy compose.yml and Dockerfile_portainer , here we specify version and move the certs to the container

docker compose up -d --build

```

![compose portainer https](https://github.com/spawnmarvel/learning-docker/blob/main/prod-ish-2/portainer/images/compose_portainer_https.png)