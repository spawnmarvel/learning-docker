# Wordpress

# How to Quickstart: Compose and WordPress

https://github.com/docker/awesome-compose/tree/master/official-documentation-samples/wordpress/

```bash
mkdir my_wordpress
cd my_wordpress

docker compose up -d

```
wordpress

http://public-ip:80

After making a user

* wordpress
* wordpresstest789-


![Multi container ](https://github.com/spawnmarvel/learning-docker/blob/main/images/wordpress.jpg)

phpmyadmin

http://public-ip:8080

```bash

- WORDPRESS_DB_USER=wordpress
- WORDPRESS_DB_PASSWORD=wordpress

```

![phpmyadmin ](https://github.com/spawnmarvel/learning-docker/blob/main/images/phpmyadmin.jpg)

portainer

https://public-ip:9443

* admin
* wordpresstest789-

![Portainer ](https://github.com/spawnmarvel/learning-docker/blob/main/images/wordpress_portainer.jpg)

Test stop it
```bash

cd my_wordpress

docker compose down

docker rmi -f $(docker images -aq)

# keep the volume

docker compose up -d

# all good

```