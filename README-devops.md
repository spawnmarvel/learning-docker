# 2 Azure Devops

You are at devops readme


## Learn manual

That's a smart choice to focus and simplify your learning path! Since you already have the AZ-104 (Azure Administrator) and an introductory certification like LSF 101 (which provides valuable Linux experience for Docker), here is the focused path to master Docker and Azure DevOps for container deployment.
Your Focused Learning Path: Docker and Azure DevOps
Phase 1: Master Docker Fundamentals
Your first step is to gain proficiency with Docker locally. The LSF 101 background will be a significant advantage here.
| Step | Focus Area | Key Concepts to Master | Practical Hands-on |
|---|---|---|---|
| 1. Core Concepts | Docker Engine | Images, Containers, Layers, Volumes, Networks (Bridge, Host). | Install Docker on your local machine (Windows/Linux/Mac). |
| 2. Image Creation | Dockerfiles | Instructions (FROM, RUN, COPY, EXPOSE, CMD), .dockerignore. | Write a Dockerfile for a simple application (e.g., a basic web server in Node.js or Python). Build, run, and troubleshoot the container. |
| 3. Multi-Container | Docker Compose | The docker-compose.yml file, defining services, networks, and volumes for a multi-tier app (e.g., a web app plus a database). | Use Docker Compose to launch a local application stack (e.g., a WordPress site using a web server and a MySQL container). |
| 4. Registry | Azure Container Registry (ACR) | Pushing and pulling images, authentication (your AZ-104 knowledge applies here for setup). | Create an ACR instance in Azure. Tag your local Docker image and push it to your private ACR. |
Phase 2: Azure DevOps for CI/CD
Now, you will integrate your Docker skills into the automated processes of Azure DevOps.
| Step | Focus Area | Key Concepts to Master | Practical Hands-on |
|---|---|---|---|
| 1. Azure DevOps Basics | Pipeline Components | Azure Repos (Git), Azure Pipelines (YAML syntax), Service Connections. | Create an Azure DevOps Project. Commit your application code and Dockerfile to a new Azure Repo. |
| 2. Continuous Integration (CI) | Build Pipeline | YAML stages/jobs/steps, Docker task, variable groups. | Create a YAML CI Pipeline to automatically trigger on a code push: 1. Build the Docker image from your Dockerfile. 2. Push the image to your Azure Container Registry (ACR). |
| 3. Continuous Delivery (CD) | Release Pipeline | Deployment jobs, using Azure CLI/Tasks to deploy containers. | Configure a CD pipeline to take the image from ACR and deploy it to a running Azure service, using the Azure CLI task instead of a dedicated IaC tool. |
Phase 3: Azure Container Deployment
This phase uses your existing AZ-104 knowledge and new Docker skills to deploy to Azure's managed container services.
| Azure Service | How to Deploy (Without IaC) | Why it Matters |
|---|---|---|
| Azure Container Instances (ACI) | Use the Azure CLI task in your Azure Pipeline to run the az container create command, specifying the image from your ACR. | Great for quick deployments, testing, and simple tasks where full orchestration is overkill. |
| Azure App Service (for Containers) | Use the Azure App Service Deploy task in your pipeline, configured for a Docker image source. | A simple, fully managed PaaS offering. You just point it to your image in ACR and it handles the rest. |
| Azure Kubernetes Service (AKS) | While typically used with IaC, you can deploy your application using Kubernetes Manifests (.yaml files) and the Kubernetes task in Azure Pipelines. | The industry standard for complex, scalable, and highly-available container orchestration. |
Recommended Next Certification:
 * Microsoft Certified: DevOps Engineer Expert (AZ-400): This is the official expert-level credential. It validates the end-to-end skills you are acquiring (version control, CI/CD, monitoring, and container deployment). You already have the AZ-104 prerequisite, making this your most direct certification goal.