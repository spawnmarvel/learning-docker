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

| Restart policy | Description
| -------------  | -----
| Always         | Containers in the container group are always restarted. This policy makes sense for long-running tasks like a web server. This setting is the default applied when no restart policy is specified at container creation.
| Never          | Containers in the container group are never restarted. The containers run one time only.
| OnFailure      | Containers in the container group are restarted only when the process executed in the container fails (when it terminates with a nonzero exit code). The containers are run at least once. This policy works well for containers that run short-lived tasks.


Resource group and login

```bash
# rg
Rg-uk-learn-aci-001

# localhost, check that you have az cli, else install it
# open powershell

PowerShell 7.3.9
az version
# PS C:\Users\username> az version
{
  "azure-cli": "2.50.0",
  "azure-cli-core": "2.50.0",
  "azure-cli-telemetry": "1.0.8",
  "extensions": {
    "ssh": "2.0.0"
  }
}

# good
# now login to azure
az login --tenant TENANT-ID

```
Run a container to completion

1. Run this az container create command to start the container:
```bash
az container create --resource-group Rg-uk-learn-aci-001 --name mycontainer-restart-demo --image mcr.microsoft.com/azuredocs/aci-wordcount:latest --restart-policy OnFailure --location uksouth

```
Azure Container Instances starts the container and then stops it when its process (a script, in this case) exits. When Azure Container Instances stops a container whose restart policy is Never or OnFailure, the container's status is set to Terminated.

2. Run az container show to check your container's status:
```bash
az container show --resource-group Rg-uk-learn-aci-001 --name mycontainer-restart-demo --query "containers[0].instanceView.currentState.state"
# "Terminated"
```

3. Run az container logs to view the container's logs to examine the output:
```bash
az container logs --resource-group Rg-uk-learn-aci-001 --name mycontainer-restart-demo
```

3. Output
```log
[('the', 990),
 ('and', 702),
 ('of', 628),
 ('to', 610),
 ('I', 544),
 ('you', 495),
 ('a', 453),
 ('my', 441),
 ('in', 399),
 ('HAMLET', 386)]
```
### Exercise - Set environment variables

### Exercise - Use data volumes

### Exercise - Troubleshoot Azure Container Instances

### Knowledge check

https://learn.microsoft.com/en-us/training/modules/run-docker-with-azure-container-instances/

## Quickstart: Deploy a container instance in Azure using the Azure CLI


https://learn.microsoft.com/en-us/azure/container-instances/container-instances-quickstart

## Tutorial: Create a container image for deployment to Azure Container Instances

https://learn.microsoft.com/en-us/azure/container-instances/container-instances-tutorial-prepare-app


## RabbitMQ ACI

