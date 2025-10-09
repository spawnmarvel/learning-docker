# 2 Azure

You are at devops readme


## Learn manual

The most complete and logical order for a beginner learning to deploy a Docker container to Azure Container Instances (ACI) is:

1.  **When to use Docker containers**
    * (Foundational knowledge on Docker concepts)
    * `https://learn.microsoft.com/en-us/training/modules/intro-to-docker-containers/`

2.  **Tutorial: Create a container image for deployment to Azure Container Instances**
    * (Local preparation and image creation)
    * `https://learn.microsoft.com/en-us/azure/container-instances/container-instances-tutorial-prepare-app`

3.  **Run Docker containers with Azure Container Instances**
    * (Introduction to the Azure Container Instances service)
    * `https://learn.microsoft.com/en-us/training/modules/run-docker-with-azure-container-instances/`

4.  **Quickstart: Push and pull a container image using Docker**
    * (**The Missing Step:** Using Azure Container Registry to store the image for ACI to access)
    * `https://learn.microsoft.com/en-us/azure/container-registry/container-registry-get-started-docker-cli`

5.  **Quickstart: Deploy a container instance in Azure using the Azure CLI**
    * (Final execution of the deployment using the image pushed in step 4)
    * `https://learn.microsoft.com/en-us/azure/container-instances/container-instances-quickstart`

## Learn devops

The full conceptual flow would be:

1. Intro to Docker
2. Create the Image (Local)
3. Learn the Service (ACI)

(Insert Pipeline Learning Here)

4. Push to Registry (Automated by Pipeline)
5. Deploy to ACI (Automated by Pipeline)

The CI/CD pipeline step is the automation layer built on top of the manual steps. The most common tool for this in the Azure ecosystem is **Azure DevOps Pipelines** (or GitHub Actions).

Here are key links for learning and implementing the pipeline step, which conceptually fits between Step 3 (Learning ACI) and the rest of the manual process (Steps 4 & 5).

## Pipeline Step: CI/CD for Docker to ACI

This automation replaces the manual steps of building, tagging, pushing the image to Azure Container Registry (ACR), and finally deploying to Azure Container Instances (ACI).

| Action | Resource Title | URL |
| :--- | :--- | :--- |
| **Implement CI/CD** | **Azure Pipelines and Docker** (Covers Build & Push to Registry) | `https://docs.docker.com/guides/azure-pipelines/` |
| **Deployment to ACI** | **Managing Containers with Azure DevOps** (Includes YAML for Build, Push, and ACI Deployment) | `https://www.devopswithritesh.in/managing-containers-with-azure-devops` |
| **Service Connection** | **Create a service connection and build and publish Docker images to Azure Container Registry** | `https://learn.microsoft.com/en-us/azure/devops/pipelines/ecosystems/containers/publish-to-acr?view=azure-devops` |

---

The below video provides a hands-on walk-through of the entire end-to-end process: from containerization to deploying to ACI using an Azure DevOps CI/CD pipeline.

[Day-10/16 Getting Started With Docker Container | Azure DevOps CICD for Azure Container Instances](https://www.youtube.com/watch?v=6DJfhwG3DGQ) is a relevant video that shows a step-by-step walkthrough of setting up an Azure DevOps CI/CD pipeline to deploy a containerized application to Azure Container Instances.
http://googleusercontent.com/youtube_content/0