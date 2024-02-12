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
az acr create --resource-group Rg-uks-cr-001 --name $ACR_NAME --sku Basic

```

Or use the portal.

## Exercise - Build container images using Azure Container Registry Tasks

1. We added the Dockerfile to a storage account and download it

```bash
ACR_NAME=marvel0001

wget https://staccountmarvel0001.blob.core.windows.net/rabbitmq/Dockerfile

az acr build --registry $ACR_NAME --image rmq:v1 .

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
https://learn.microsoft.com/en-us/training/modules/build-and-store-container-images/

## az acr build

```bash
az acr build --registry
             [--agent-pool]
             [--auth-mode {Default, None}]
             [--build-arg]
             [--file]
             [--image]
             [--log-template]
             [--no-format]
             [--no-logs]
             [--no-push]
             [--no-wait]
             [--platform]
             [--resource-group]
             [--secret-build-arg]
             [--target]
             [--timeout]
             [<SOURCE_LOCATION>]
```

https://learn.microsoft.com/en-us/cli/azure/acr?view=azure-cli-latest#az-acr-build

## RabbitMQ ACI