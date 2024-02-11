# Azure


## Visuals

https://follow-e-lo.com/2024/01/29/azure-aci-docker/

## Azure Container Instances documentation

ACI and ACI Group

![Azure resources](https://github.com/spawnmarvel/learning-docker/blob/main/images/aci2.jpg)


https://learn.microsoft.com/en-us/azure/container-instances/

## Azure Container Registry service tiers

| Tier | Description
| ---  | -----
| Basic | Basic	A cost-optimized entry point for developers learning about Azure Container Registry. <br>Basic registries have the same programmatic capabilities as Standard and Premium (such as Microsoft Entra authentication integration, image deletion, and webhooks). <br>However, the included storage and image throughput are most appropriate for lower usage scenarios.
| Standard |
| Premium  |

https://learn.microsoft.com/en-us/azure/container-registry/container-registry-skus


## Image source

Quickstart

Azure Container Registry

Other registry

![Azure resources](https://github.com/spawnmarvel/learning-docker/blob/main/images/deploy_types.jpg)

Public docker

![Azure resources](https://github.com/spawnmarvel/learning-docker/blob/main/images/deploy_public.jpg)

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

# use git bash or login to a linux vm

az version
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

Secured environment variables prevent sensitive information from displaying in the container's output.

Create an Azure Cosmos DB instance and use environment variables to pass the connection information to an Azure container instance. An application in the container uses the variables to write and read data from Azure Cosmos DB. 

Create both an 
* environment variable and a 
* secured environment variable so that you can see the difference between them.

Deploy Azure Cosmos DB

1. When you deploy Azure Cosmos DB, you provide a unique database name.
```bash

COSMOS_DB_NAME=aci-cosmos-db-$RANDOM
echo $COSMOS_DB_NAME
# aci-cosmos-db-3767



```

2. Run this az cosmosdb create command to create your Azure Cosmos DB instance:
```bash
COSMOS_DB_ENDPOINT=$(az cosmosdb create --resource-group Rg-uk-learn-aci-001 --name $COSMOS_DB_NAME --query documentEndpoint --output tsv)
```

3. Run az cosmosdb keys list to get the Azure Cosmos DB connection key and store it in a Bash variable named COSMOS_DB_MASTERKEY:
```bash
COSMOS_DB_MASTERKEY=$(az cosmosdb keys list \
  --resource-group Rg-uk-learn-aci-001 \
  --name $COSMOS_DB_NAME \
  --query primaryMasterKey \
  --output tsv)

 echo $COSMOS_DB_MASTERKEY

```

Deploy a container that works with your database

Create an Azure container instance that can read from and write records to your Azure Cosmos DB instance.

The two environment variables you created in the last part, 
* COSMOS_DB_ENDPOINT and 
* COSMOS_DB_MASTERKEY, hold the values you need to connect to the Azure Cosmos DB instance.

1. 
```bash
az container create \
  --resource-group Rg-uk-learn-aci-001 \
  --name aci-demo \
  --image mcr.microsoft.com/azuredocs/azure-vote-front:cosmosdb \
  --ip-address Public \
  --location eastus \
  --environment-variables \
    COSMOS_DB_ENDPOINT=$COSMOS_DB_ENDPOINT \
    COSMOS_DB_MASTERKEY=$COSMOS_DB_MASTERKEY
```

2. Run the az container show command to get your container's public IP address:
```bash
az container show \
  --resource-group Rg-uk-learn-aci-001 \
  --name aci-demo \
  --query ipAddress.ip \
  --output tsv
```

3. 
```bash
```

Use secured environment variables to hide connection information

In the previous section, you used two environment variables to create your container. By default, these environment variables are accessible through the Azure portal and command-line tools in plain text.

1.  Let's start by seeing the current behavior in action. Run the following az container show command to display your container's environment variables:

```bash
az container show \
  --resource-group Rg-uk-learn-aci-001 \
  --name aci-demo \
  --query containers[0].environmentVariables
```

You get output with both values in plain text. Here's an example:

```json
[
  {
    "name": "COSMOS_DB_ENDPOINT",
    "secureValue": null,
    "value": "https://aci-cosmos.documents.azure.com:443/"
  },
  {
    "name": "COSMOS_DB_MASTERKEY",
    "secureValue": null,
    "value": "Xm5BwdLlCllBvrR26V00000000S2uOusuglhzwkE7dOPMBQ3oA30n3rKd8PKA13700000000095ynys863Ghgw=="
  }
]

```
Although these values don't appear to your users through the voting application, it's a good security practice to ensure that sensitive information (such as connection keys) isn't stored in plain text.

Secure environment variables prevent clear text output. To use secure environment variables, use the 
* --secure-environment-variables argument instead of the 
* --environment-variables argument.

2. Run the following command to create a second container named aci-demo-secure that makes use of secured environment variables:

```bash
az container create \
  --resource-group Rg-uk-learn-aci-001 \
  --name aci-demo-secure \
  --image mcr.microsoft.com/azuredocs/azure-vote-front:cosmosdb \
  --ip-address Public \
  --location eastus \
  --secure-environment-variables \
    COSMOS_DB_ENDPOINT=$COSMOS_DB_ENDPOINT \
    COSMOS_DB_MASTERKEY=$COSMOS_DB_MASTERKEY
```

3. Run the following az container show command to display your container's environment variables:
```bash
az container show --resource-group Rg-uk-learn-aci-001 --name aci-demo-secure --query containers[0].environmentVariables
```

4. This time, you can see that your environment variables don't appear in plain text:
```json
[
  {
    "name": "COSMOS_DB_ENDPOINT",
    "secureValue": null,
    "value": null
  },
  {
    "name": "COSMOS_DB_MASTERKEY",
    "secureValue": null,
    "value": null
  }
]
```

### Exercise - Use data volumes

By default, Azure Container Instances are stateless. If the container crashes or stops, all of its state is lost. To persist state beyond the lifetime of the container, you must mount a volume from an external store.

Mount an Azure file share to an Azure container instance so that you can store data and access it later.

Create an Azure file share

1. Your storage account requires a unique name
```bash
# Rg-uk-learn-aci-001

STORAGE_ACCOUNT_NAME=mystorageaccount$RANDOM

```

2. Run the following az storage account create command to create your storage account:
```bash
az storage account create --resource-group Rg-uk-learn-aci-001 --name $STORAGE_ACCOUNT_NAME --sku Standard_LRS --location eastus
```

3. Run the following command to place the storage account connection string into an environment variable named AZURE_STORAGE_CONNECTION_STRING:
```bash
export AZURE_STORAGE_CONNECTION_STRING=$(az storage account show-connection-string --resource-group Rg-uk-learn-aci-001 --name $STORAGE_ACCOUNT_NAME --output tsv)
```

4. Run this command to create a file share named aci-share-demo in the storage account:
```bash
az storage share create --name aci-share-demo
```

Get storage credentials

To mount an Azure file share as a volume in Azure Container Instances, you need these three values:

Storage account name
Share name
Storage account access key

You already have the first two values. The storage account name is stored in the STORAGE_ACCOUNT_NAME Bash variable. You specified aci-share-demo as the share name in the previous step. Here, you get the remaining value: the storage account access key.

1. Run the following command to get the storage account key:
```bash
STORAGE_KEY=$(az storage account keys list --resource-group Rg-uk-learn-aci-001 --account-name $STORAGE_ACCOUNT_NAME --query "[0].value" --output tsv)

#
echo $STORAGE_KEY

```

Deploy a container and mount the file share

1. Run this az container create command to create a container that mounts /aci/logs/ to your file share:
```bash

STORAGE_ACCOUNT_NAME=mystorageaccount3078
STORAGE_KEY=$(az storage account keys list --resource-group Rg-uk-learn-aci-001 --account-name $STORAGE_ACCOUNT_NAME --query "[0].value" --output tsv)

az container create --resource-group Rg-uk-learn-aci-001 --name aci-demo-files --image mcr.microsoft.com/azuredocs/aci-hellofiles --location uksouth --ports 80 --ip-address Public --azure-file-volume-account-name $STORAGE_ACCOUNT_NAME --azure-file-volume-account-key $STORAGE_KEY --azure-file-volume-share-name aci-share-demo --azure-file-volume-mount-path /aci/logs/
```
2. Run az container show to get your container's public IP address:
```bash
az container show --resource-group Rg-uk-learn-aci-001 --name aci-demo-files --query ipAddress.ip --output tsv
```

### Exercise - Troubleshoot Azure Container Instances

Get the logs form the prior deployed container
```bash
az container logs --resource-group Rg-uk-learn-aci-001 --name aci-demo-files
```

The tutorial uses the voting app, we have removed that. Not it is the save text app.

```log
listening on port undefined
{ name: 'Data to storage account' }
Wrote to file

```

Get container events

```bash
az container attach --resource-group Rg-uk-learn-aci-001 --name aci-demo-files
```

Execute a command in your container

```bash
az container exec --resource-group Rg-uk-learn-aci-001 --name aci-demo-files --exec-command /bin/sh

pwd
/usr/src/app

```

Monitor CPU and memory usage on your container

1. Run the following az container show command to get the ID of your Azure container instance and store the ID in a Bash variable:
```bash
CONTAINER_ID=$(az container show --resource-group Rg-uk-learn-aci-001 --name aci-demo-files --query id --output tsv)
```

2. Run the az monitor metrics list command to retrieve CPU usage information:

```bash
az monitor metrics list --resource $CONTAINER_ID --metrics CPUUsage --output table
```

3. Run this az monitor metrics list command to retrieve memory usage information:
```bash
az monitor metrics list --resource $CONTAINER_ID --metrics MemoryUsage --output table
```

### Knowledge check

https://learn.microsoft.com/en-us/training/modules/run-docker-with-azure-container-instances/

## Introduction to Container registries in Azure

Azure Container Registry is a managed registry service based on the open-source Docker Registry 2.0. Create and maintain Azure container registries to store and manage your container images and related artifacts.

Use Azure container registries with your existing container development and deployment pipelines, or use Azure Container Registry Tasks to build container images in Azure. Build on demand, or fully automate builds with triggers such as source code commits and base image updates.

https://learn.microsoft.com/en-us/azure/container-registry/container-registry-intro


## Deploy microservices with Azure Container Apps


![Azure resources](https://github.com/spawnmarvel/learning-docker/blob/main/images/registry.jpg)

https://learn.microsoft.com/en-us/azure/architecture/example-scenario/serverless/microservices-with-container-apps

## Tutorial: Create a container image for deployment to Azure Container Instances

https://learn.microsoft.com/en-us/azure/container-instances/container-instances-tutorial-prepare-app


## RabbitMQ ACI

