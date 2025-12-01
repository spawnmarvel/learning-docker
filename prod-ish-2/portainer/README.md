# Portainer-ce

https://docs.portainer.io/start/install-ce/server/docker/linux

## Set up

You can deploy portainer as its on container or with other containers in the compose.yml.

View frontpage or main readme section

https://github.com/spawnmarvel/learning-docker/blob/main/README.md#set-up-portainer-https-done-2

## portainer-ce as one contaier.


Generate ssl certificate

```bash
cd /etc/docker/
cd ssl/

sudo openssl req -x509 -newkey rsa:4096 -keyout portainer.key -out portainer.crt -days 730 -nodes

sudo chmod 600 portainer.key
```

Run portainer

```bash
mkdir mkdir docker-portainer
cd mkdir docker-portainer

# copy compose_https.yml to that folder and rename to compose.yml

docker compose up -d

```