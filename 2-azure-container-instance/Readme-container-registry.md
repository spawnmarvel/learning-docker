# Azure Container Registry


## Visuals

https://follow-e-lo.com/2024/02/11/azure-aci-docker-registry-102/

## What is Azure Container Registry - How to create Azure Container Registry Tutorial | Whizlabs

https://www.youtube.com/watch?v=_ZzjkglIS0s

## Introduction to Container registries in Azure

Azure Container Registry is a managed registry service based on the open-source Docker Registry 2.0. Create and maintain Azure container registries to store and manage your container images and related artifacts.

Use Azure container registries with your existing container development and deployment pipelines, or use Azure Container Registry Tasks to build container images in Azure. Build on demand, or fully automate builds with triggers such as source code commits and base image updates.

https://learn.microsoft.com/en-us/azure/container-registry/container-registry-intro


## Deploy microservices with Azure Container Apps


![Azure resources](https://github.com/spawnmarvel/learning-docker/blob/main/images/registry.jpg)

https://learn.microsoft.com/en-us/azure/architecture/example-scenario/serverless/microservices-with-container-apps


## Build and store container images with Azure Container Registry

Azure Container Registry is a managed Docker registry service based on the open-source Docker Registry 2.0. Container Registry is private, hosted in Azure, and allows you to build, store, and manage images for all types of container deployments. Learn how to build and store container images with Azure Container Registry.

* Deploy an Azure container registry.
* Build a container image using Azure Container Registry Tasks and deploy it to an Azure container instance.
* Replicate the container image to multiple Azure regions.

### Introduction to Azure Container Registry

* Azure Container Registry is a managed Docker registry service based on the open-source Docker Registry 2.0. Container Registry is private, hosted in Azure, and allows you to build, store, and manage images for container deployments.
* You can push and pull container images with Azure Container Registry using the Docker CLI or the Azure CLI. Azure portal integration allows you to visually inspect the container images in your container registry.
* In distributed environments, you can use the container registry geo-replication feature to distribute container images to multiple Azure data centers for localized distribution.

You can use Azure Container Registry Tasks to store and build container images in Azure. Tasks use a standard Dockerfile to create and store the container images in Azure Container Registry ***without the need for local Docker tooling.***

## Exercise - Deploy an Azure container registry

Create an Azure container registry

1. Sign in and create an rg.
```bash
az login --tenant THE-ID

az group create --name Rg-uks-cr-001 --location uksouth
```

2. Define an environment variable, ACR_NAME, to hold your container registry name using the following command. The name must be unique within Azure and contain 5-50 alphanumeric characters

https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ready/azure-best-practices/naming-and-tagging


```bash
ACR_NAME=your-unique-acr-name

```

3. Create an Azure container registry using the az acr create command.

```bash
# Basic, Standard and Premium
az acr create --resource-group Rg-uks-aci-registry-0001 --name $ACR_NAME --sku Basic

```

Or use the portal.

## Exercise - Build container images using Azure Container Registry Tasks

1. We added the Dockerfile to a storage account and download it

```bash

wget https://staccountmarvel0001.blob.core.windows.net/rabbitmq/Dockerfile

```
2. Build the container image from the Dockerfile using the az acr build command.

```bash
# Make sure you add the period (.) to the end of the command. It represents the source directory containing the Dockerfile. 
# Because we didn't specify the name of the file using the --file parameter, the command looks for a file called Dockerfile in our current directory.
az acr build --registry $ACR_NAME --image rmq:v1 .
```
3. Verify that the image has been created and stored in the registry using the az acr repository list command.

```bash
az acr repository list --name $ACR_NAME --output table
# Result
# --------
# rmq
```
## Exercise - Deploy images from Azure Container Registry

You can pull container images from Azure Container Registry using various container management platforms, such as Azure Container Instances, Azure Kubernetes Service, or Docker for Windows or Mac

In this module, you deploy the image to an Azure Container Instance.

Registry authentication.

Azure Container Registry doesn't support unauthenticated access and requires authentication for all operations. Registries support two types of identities:

* Microsoft Entra identities, including both user and service principals. Access to a registry with a Microsoft Entra identity is role-based and you can assign identities one of three roles: reader (pull access only), contributor (push and pull access), or owner (pull, push, and assign roles to other users).
* The admin account included with each registry. The admin account is disabled by default.

:exclamation: :exclamation:
***The admin account provides a quick option to try a new registry. You can enable the account and use the username and password in workflows and apps that need access.***

***After you've confirmed the registry works as expected, you should disable the admin account and use Microsoft Entra identities to ensure the security of your registry. Do not share the admin account credentials with others.***
:exclamation: :exclamation:

Enable the registry admin account

1. Enable the admin account on your registry using the az acr update command.
```bash
az acr update -n $ACR_NAME --admin-enabled true
```

2. Retrieve the username and password for the admin account using the az acr credential show command.

```bash
az acr credential show --name $ACR_NAME
```

Deploy a container with Azure CLI

1. Deploy a container instance using the az container create command. Make sure you replace <admin-username> and <admin-password> with your admin username and password from the previous command.

```bash
admin_username=
admin_password=
az container create --resource-group Rg-uks-aci-registry-0001 --name rmq01 --image $ACR_NAME.azurecr.io/rmq:v1 --registry-login-server $ACR_NAME.azurecr.io --ip-address Public --location uksouth --registry-username $admin_username --registry-password $admin_password --ports 15672
```
2. Get the IP address of the Azure container instance using the az container show command.

```bash
az container show --resource-group Rg-uks-aci-registry-0001 --name rmq01 --query ipAddress.ip --output table
```

Visit it http://public-ip:15672 success


https://learn.microsoft.com/en-us/training/modules/build-and-store-container-images/

## RabbitMQ ACI 101 Done

## RabbitMQ ACI 102

Update the ACI

* SSL
* RabbitMQ config
* Restart policy
* Mount to storage
* etc