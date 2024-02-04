# Azure


## Visuals

https://follow-e-lo.com/2024/01/29/azure-aci-docker/

## Azure Container Instances documentation

https://learn.microsoft.com/en-us/azure/container-instances/

## Azure Container Registry service tiers

| Tier | Description
| ---  | -----
| Basic | Basic	A cost-optimized entry point for developers learning about Azure Container Registry. <br>Basic registries have the same programmatic capabilities as Standard and Premium (such as Microsoft Entra authentication integration, image deletion, and webhooks). <br>However, the included storage and image throughput are most appropriate for lower usage scenarios.
| Standard |
| Premium  |

https://learn.microsoft.com/en-us/azure/container-registry/container-registry-skus


## Best practices and considerations for Azure Container Instances

https://learn.microsoft.com/en-us/azure/container-instances/container-instances-best-practices-and-considerations

## Security considerations for Azure Container Instances

https://learn.microsoft.com/en-us/azure/container-instances/container-instances-image-security


## How to use managed identities with Azure Container Instances

* Enable a user-assigned or system-assigned identity in a container group
* Grant the identity access to an Azure key vault
* Use the managed identity to access a key vault from a running container

https://learn.microsoft.com/en-us/azure/container-instances/container-instances-managed-identity


## Enable a TLS endpoint in a sidecar container

This article shows how to create a container group with an application container and a sidecar container running a TLS/SSL provider. 

By setting up a container group with a separate TLS endpoint, you enable TLS connections for your application without changing your application code.

https://learn.microsoft.com/en-us/azure/container-instances/container-instances-container-group-ssl

## Run Docker containers with Azure Container Instances

* Run containers in Azure Container Instances
* Control what happens when your container exits
* Use environment variables to configure your container when it starts
* Attach a data volume to persist data when your container exits
* Learn some basic ways to troubleshoot issues on your Azure containers

### Introduction to Azure Container Instances

* Fast startup: Launch containers in seconds.
* Per second billing: Incur costs only while the container is running.
* Hypervisor-level security: Isolate your application as completely as it would be in a VM.
* Custom sizes: Specify exact values for CPU cores and memory.
* Persistent storage: Mount Azure Files shares directly to a container to retrieve and persist state.
* Linux and Windows: Schedule both Windows and Linux containers using the same API.

**A container is a process.**

### Exercise - Run Azure Container Instances

### Exercise - Control restart behavior

### Exercise - Set environment variables

### Exercise - Use data volumes

### Exercise - Troubleshoot Azure Container Instances

### Knowledge check

https://learn.microsoft.com/en-us/training/modules/run-docker-with-azure-container-instances/

## Quickstart: Deploy a container instance in Azure using the Azure CLI


```bash
TBD

```

https://learn.microsoft.com/en-us/azure/container-instances/container-instances-quickstart

## Tutorial: Create a container image for deployment to Azure Container Instances

https://learn.microsoft.com/en-us/azure/container-instances/container-instances-tutorial-prepare-app


## RabbitMQ ACI

