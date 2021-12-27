# Azure App Service Web App Demo Project
 
This tutorial azure cloud project demonstrates how to create and deploy a basic web app using azure. We will use our azure account to creature a resource group, app service plan, and a web app. Then we will configure a CI/CD pipeline (continuous integration/continuous deployment) that integregates with our GitHub code repository. Our demo web app is a flask template and python web application.
 
Watch the video tutorials and follow step-by-step instructions to learn how to create your own starter web app running on azure cloud. A bonus video and instructions are shown that demonstrate quick start creation of a web-app using the CLI (command line interface).  

## Create Azure Resource Group

Login into your Azure account and create a resource group for this project. In this tutorial we will be using the resource group name `resource-group-web-app-demo` .

## Create Web App Resource

Navigate to the resource group that was just created and add a new resource.
Search for "web app" in the azure marketplace and select the web app template.

A wizard process will guide you through the next steps

Create an App Service Web App with the following configuration:

Resource-Group: resource-group-web-app-demo
Web App Name: unique name (example: my-web-app-demo)
Publish: Code
Runtime stack: Python 3.7 or Latest
Operating System: Linux
Region: Closest region to you
App Service Plan: Default name or Create new with a name of your choice
SKU and size: F1 (Free)
Note: Azure free account only allows one Linux App Service of size F1. You may need to delete the App Service along with the App Service Plan after this demo if you will create other Linux App Services.


Voila! You have successfully created a Flask web application running on an azure web app. 

Congratulations!

## Cleanup

Don't forget to stop your azure web app after you are done playing with your project and to delete your resource group. 
