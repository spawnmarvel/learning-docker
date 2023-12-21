# learning-docker
Testing and learning Docker with Azure

## Learning docker

* Python for programming
* Bash and linux
* Azure VM with Docker
* Azure Container with Docker

## Visuals

https://follow-e-lo.com/2023/12/20/docker/

## What ARE Containers? (and Docker ...)

Time 11.51

https://github.com/spawnmarvel/learning-docker/tree/main/1-what-are-containers

## Docker docs

Docker Engine is an open source containerization technology for building and containerizing your applications

https://docs.docker.com/engine/

## Installing Docker on a VM (Azure)

Update vm vmdocker01

```bash
# update vm
sudo apt update -y

sudo apt upgrade -y

```
Create script

```bash

# create script
touch add_repository_to_apt.sh

nano add_repository_to_apt.sh

#!/bin/bash
# Add Docker's official GPG key:
sudo apt update
sudo apt install ca-certificates curl gnupg
sudo install -m 0755 -d /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
sudo chmod a+r /etc/apt/keyrings/docker.gpg

# Add the repository to Apt sources:
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update

```
Run it
```bash
sudo bash add_repository_to_apt.sh

```

Install the Docker packages

```bash
sudo apt install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

Verify Docker Engine
```bash
sudo docker run hello-world

# Unable to find image 'hello-world:latest' locally
# latest: Pulling from library/hello-world
# xxxxxxxxxx: Pull complete
# Digest: sha256:xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
# Status: Downloaded newer image for hello-world:latest

# Hello from Docker!
# This message shows that your installation appears to be working correctly.

# To generate this message, Docker took the following steps:
# 1. The Docker client contacted the Docker daemon.
# 2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
#    (amd64)
# 3. The Docker daemon created a new container from that image which runs the
#    executable that produces the output you are currently reading.
# 4. The Docker daemon streamed that output to the Docker client, which sent it
#    to your terminal.

# To try something more ambitious, you can run an Ubuntu container with:
# $ docker run -it ubuntu bash

# Share images, automate workflows, and more with a free Docker ID:
# https://hub.docker.com/

# For more examples and ideas, visit:
#  https://docs.docker.com/get-started/


docker --version
# Docker version 24.0.7, build afdd53b
```

https://docs.docker.com/engine/install/ubuntu/


## Mount fileshare on VM

Storage account staccvmdocker01

Fileshare dockershare01

Test 445
```bash
# cp each line
RESOURCE_GROUP_NAME="<your-resource-group>"
STORAGE_ACCOUNT_NAME="<your-storage-account>"

# This command assumes you have logged in with az login
HTTP_ENDPOINT=$(az storage account show --resource-group $RESOURCE_GROUP_NAME --name $STORAGE_ACCOUNT_NAME --query "primaryEndpoints.file" --output tsv | tr -d '"')
SMBPATH=$(echo $HTTP_ENDPOINT | cut -c7-${#HTTP_ENDPOINT})
FILE_HOST=$(echo $SMBPATH | tr -d "/")

nc -zvw3 $FILE_HOST 445

# Connection to .file.core.windows.net (xx.xxx.xx.xxx) 445 port [tcp/microsoft-ds] succeeded!

```

Mount it

```bash

# https://learn.microsoft.com/en-us/azure/storage/files/storage-how-to-use-files-linux?tabs=Ubuntu%2Csmb311

# https://follow-e-lo.com/2023/11/09/ubuntu-az-cli-and-mount-fileshare/

curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash

az upgrade
az version
# azure-cli 2.55.0


sudo apt install cifs-utils

sudo apt install -y linux-modules-extra-azure

az login --tenant
# To sign in, use a web browser to open the page https://microsoft.com/devicelogin and enter the code

# cp each line
RESOURCE_GROUP_NAME="<resource-group-name>"
STORAGE_ACCOUNT_NAME="<storage-account-name>"
FILE_SHARE_NAME="<file-share-name>"

MNT_ROOT="/media"
MNT_PATH="$MNT_ROOT/$STORAGE_ACCOUNT_NAME/$FILE_SHARE_NAME"

sudo mkdir -p $MNT_PATH

# cd to /media, then pwd
/media/staccvmdocker01/dockershare01

# This command assumes you have logged in with az login
HTTP_ENDPOINT=$(az storage account show --resource-group $RESOURCE_GROUP_NAME --name $STORAGE_ACCOUNT_NAME --query "primaryEndpoints.file" --output tsv | tr -d '"')
SMB_PATH=$(echo $HTTP_ENDPOINT | cut -c7-${#HTTP_ENDPOINT})$FILE_SHARE_NAME

STORAGE_ACCOUNT_KEY=$(az storage account keys list --resource-group $RESOURCE_GROUP_NAME --account-name $STORAGE_ACCOUNT_NAME --query "[0].value" --output tsv | tr -d '"')

sudo mount -t cifs $SMB_PATH $MNT_PATH -o username=$STORAGE_ACCOUNT_NAME,password=$STORAGE_ACCOUNT_KEY,serverino,nosharesock,actimeo=30,mfsymlinks

# Create a folder on the fileshare on the vm
# cd, sudo mkdir test01, pwd
/media/staccvmdocker01/dockershare01/test01

# Verify the folder on the storage account
# Storage accounts > name > File shares > sharename
test01
# Restart the vm and verify the folder and make a file in the folder
ssh

mount

# and no share args, run this again

# cp each line
RESOURCE_GROUP_NAME="<resource-group-name>"
STORAGE_ACCOUNT_NAME="<storage-account-name>"
FILE_SHARE_NAME="<file-share-name>"

MNT_ROOT="/media"
MNT_PATH="$MNT_ROOT/$STORAGE_ACCOUNT_NAME/$FILE_SHARE_NAME"

sudo mkdir -p $MNT_PATH

az login --tenant

# This command assumes you have logged in with az login
HTTP_ENDPOINT=$(az storage account show --resource-group $RESOURCE_GROUP_NAME --name $STORAGE_ACCOUNT_NAME --query "primaryEndpoints.file" --output tsv | tr -d '"')
SMB_PATH=$(echo $HTTP_ENDPOINT | cut -c7-${#HTTP_ENDPOINT})$FILE_SHARE_NAME

STORAGE_ACCOUNT_KEY=$(az storage account keys list --resource-group $RESOURCE_GROUP_NAME --account-name $STORAGE_ACCOUNT_NAME --query "[0].value" --output tsv | tr -d '"')

sudo mount -t cifs $SMB_PATH $MNT_PATH -o username=$STORAGE_ACCOUNT_NAME,password=$STORAGE_ACCOUNT_KEY,serverino,nosharesock,actimeo=30,mfsymlinks


# cd, pwd and the folder is back
/media/staccvmdocker01/dockershare01/test01

# make a file inside the folder
sudo touch file1

# Restart the vm and verify all, it has to work, djjezes...


```

https://follow-e-lo.com/2023/11/09/ubuntu-az-cli-and-mount-fileshare/


## Overview of get started

https://github.com/spawnmarvel/learning-docker/blob/main/README-1-getstarted.md


## Docker basic commands

```bash
# login
ssh user@IP

```
https://github.com/spawnmarvel/learning-docker/blob/main/README-2-commands.md

## Configure Applications

RabbitMQ:

https://github.com/spawnmarvel/learning-docker/tree/main/rmq

Zabbix:

Wordpress:

Portainer:

## Using docker on Azure Container

