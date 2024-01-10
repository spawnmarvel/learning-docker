# Wordpress

# How to Quickstart: Compose and WordPress

https://github.com/docker/awesome-compose/tree/master/official-documentation-samples/wordpress/

```bash
mkdir my_wordpress
cd my_wordpress

docker compose up -d

```
http://public-ip:80

After making a user

* wordpress
* wordpresstest789-


![Multi container ](https://github.com/spawnmarvel/learning-docker/blob/main/images/wordpress.jpg)

Test stop it
```bash

cdm my_wordpress

docker compose down

docker rmi -f $(docker images -aq)

# keep the volume

docker compose up -d

# all good

```