# Azure and Docker

That is a clear scope! You want to focus purely on the Docker application lifecycle and deployment to Azure using native Azure tools (Azure CLI, Azure Pipelines YAML), deliberately excluding IaC tools like Bicep and Terraform.
This approach simulates a scenario where an application team is given an existing Azure environment and is responsible only for the CI/CD pipeline and application hosting.

## Project 1 Docker on Azure without IaC
Here is Project 1 re-scoped for Docker on Azure without IaC:
🎯 Project 1: Docker on Azure (Pure CI/CD Focus)

The goal is to master two key deployment targets for containers on Azure: Azure Container Registry (ACR) and Azure App Service for Containers.
Prerequisites

We will assume the following resources are pre-existing (your \text{AZ-104} knowledge covers how to create these manually):
 * Resource Group
 * Azure Container Registry (ACR) (A private place to store your images).
 * Azure App Service Plan (The hosting environment).
 * Azure App Service for Containers (The running web app resource).

### Phase 1: Docker Build & Push Pipeline (The CI)

This stage ensures your application is built and stored in Azure securely.
| Step | Tool/Service | Action to Automate in Azure Pipeline (YAML) | Key Learning |
|---|---|---|---|
| 1. Source Control | Azure Repos or GitHub | Place your app code and Dockerfile in the repository. | Branching, simple .azure-pipelines.yml structure. |
| 2. Build Image | Azure Pipelines & Docker Task | Use the Docker@2 task to execute docker build using your Dockerfile. | Configuring the build context and arguments in the pipeline. |
| 3. Tag Image | Azure Pipelines | Tag the image with the build number or commit hash (e.g., myrepo/myapp:$(Build.BuildId)). | Using pre-defined pipeline variables for unique versioning. |
| 4. Push to ACR | Azure Pipelines & Docker Task | Use the Docker@2 task to securely authenticate and execute docker push to the pre-existing ACR. | Service Connection authentication to ACR for seamless login. |

### Phase 2: Deployment Pipeline (The CD)

This stage takes the newly pushed image and deploys it to a running Azure service using native CLI commands.
| Step | Tool/Service | Action to Automate in Azure Pipeline (YAML) | Key Learning |
|---|---|---|---|
| 1. Service Connection | Azure DevOps | Ensure the pipeline has an Azure Resource Manager (ARM) Service Connection with permissions to update the App Service. | Securely connecting the pipeline to Azure resources using a Service Principal. |
| 2. Deploy to App Service | Azure CLI Task | Use the AzureCLI@2 task to execute the single command that updates the web app: az webapp config container set ... | Crucial Command: Mastering the az webapp config container set command to point the App Service to the newly tagged image in ACR. |
| 3. Swap Deployment Slot | Azure CLI Task (Optional, but advanced) | Implement a deployment to a staging slot first, wait for a health check, then use: az webapp deployment slot swap ... | Zero-Downtime: Implementing a best-practice for zero-downtime rolling updates. |
| 4. Post-Deployment Check | cURL/Bash Task | Execute a simple curl command against the web app URL to verify it's reachable and returns a success code. | Creating simple health checks within the pipeline itself. |

Project Deliverable
The successful completion of this re-scoped project means you can demonstrate:
 * A fully working YAML Azure Pipeline file.
 * A staged, repeatable process that takes source code, turns it into a versioned image in a private registry (\text{ACR}), and deploys it to a serverless platform (\text{App Service}) with a single button click.
This proves your expertise in the core Continuous Delivery aspects of a DevOps role using only native Azure tools.

### Microsoft Learn links in the logical order

Here are the Microsoft Learn links in the logical order of your project flow:

Project 1: Docker on Azure (Pure CI/CD Workflow) Links

### Phase 1: Preparation (Manual Steps using \text{AZ-104} Skills)

While you're not using IaC, you still need to create the targets manually. These links show the key commands needed for the prerequisites.
| Order | Component/Concept | Microsoft Learn Link | Key Takeaway for Project |
|---|---|---|---|---|
| 1. | Container Registry Creation | Quickstart: Create an Azure container registry using the Azure CLI | You must create the ACR instance where your pipeline will push the image. | https://learn.microsoft.com/en-us/azure/container-registry/container-registry-get-started-azure-cli
| 2. | App Service Setup | Quickstart: Run a custom container on App Service | Follow the steps to manually create the App Service Plan and the initial Web App for Containers resource (using a placeholder image like Nginx). | |

### Phase 2: Continuous Integration (CI) Pipeline - Build & Push

This is the first stage of your YAML pipeline, focusing on the Docker@2 task.
| Order | Component/Concept | Microsoft Learn Link | Key Takeaway for Project |
|---|---|---|---|
| 3. | Docker Build & Push YAML | Use Docker YAML to build and push images to Azure Container Registry | Focus on the Docker@2 task. Learn how to define the containerRegistry Service Connection, use the buildAndPush command, and dynamically tag the image with a unique ID. |

### Phase 3: Continuous Delivery (CD) Pipeline - Deployment

This is the second stage of your YAML pipeline, focusing on using the Azure CLI to update the App Service.
| Order | Component/Concept | Microsoft Learn Link | Key Takeaway for Project |
|---|---|---|---|
| 4. | App Service Container Update Command | az webapp config container set documentation | The most critical command for deployment. Learn the exact syntax for using az webapp config container set to change the image in your App Service to the newly pushed, tagged image in your ACR. |
| 5. | App Service Authentication | Configure a custom container in Azure App Service | Pay attention to the section on pulling images from a private registry (like your ACR). The modern, secure approach is using Managed Identity to grant the App Service \text{AcrPull} role, eliminating the need to pass passwords in the CLI. |
| 6. | Deployment Slots (Advanced CD) | Set up staging environments in Azure App Service | (Optional, but highly recommended) If you want your CD pipeline to enable zero-downtime updates, this explains the concept and the az webapp deployment slot swap command. |


