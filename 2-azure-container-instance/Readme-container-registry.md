# Azure Container Registry


## Visuals

https://follow-e-lo.com/2024/02/11/azure-aci-docker-registry-102/

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

https://learn.microsoft.com/en-us/training/modules/build-and-store-container-images/

## RabbitMQ ACI