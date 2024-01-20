# Image-building best practices

https://docs.docker.com/get-started/09_image_best/

## Containerize an application

```bash
```


## Update the application

```bash
```


## Share the application

```bash
```



## Persist db

```bash
```

## Use bind mounts

```bash
```

## Multi container apps

```bash
```

## Use docker compose

```bash
# oh great I stopped here, nice.

pwd
# /home/imsdal/getting-started-app

ls
# Dockerfile  README.md  compose.yml  node_modules  package.json  spec  src  yarn.lock

docker compose up -d

# Network getting-started-app_default           Created                                                          
# Volume "getting-started-app_todo-mysql-data"  Created                                                          
# Container getting-started-app-mysql-1         Started                                                         
# Container getting-started-app-app-1           Started

# Open NSG 3000 again, it was rm'ed since I though I was done
# visit http://public-ip:3000

```

## and finally: Image-building best practice

```bash
```


