# Portainer-ce

https://docs.portainer.io/start/install-ce/server/docker/linux

## Set up

You can deploy portainer as its on container or with other containers in the compose.yml.

## portainer-ce as one contaier.

```bash
mkdir mkdir docker-portainer
cd mkdir docker-portainer

# copy compose_https.yml to that folder and rename to compose.yml

docker compose up -d

```