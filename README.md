# ml_as_a_service
A setup for providing ML As a Service with any Cloud Provider

## Background and Objective

One of the greatest challenges faced by a Data Scientist is getting their <b>sophisticated ML Model running successfully in their laptops<b> to the end user. So many tools are available and yet everything requires the Data Scientist to learn the toolkit to proceed . 

Some of the challenges involved in deploying a model to production include 
  a. Scalability 
  b. Accessibility 
  c. Usability
  
Our purpose to is to address the above problems with a one-stop solution .

## OUT OF SCOPE
This repo will use boilerplate model training / deployment scripts and will not demonstrate how a model is being trained or can be fine-tuned. We assume that the models are pre-built and ready to deploy.


## TODO
### Docker
1. Basic Image recognition IRIS Model in a container 
2. endpoint definition
3. Deployment to Dockerhub as a public image 

### Azure
4. Add ARM Template for deploying the following assets to Azure
5. Container Instance with ML Model
6. Linux App Service
7. Storage Account 
8. Azure function with Blob Trigger to process batch images and send response 

[![Deploy to Azure](https://aka.ms/deploytoazurebutton)](https://portal.azure.com/#create/Microsoft.Template/uri/https://raw.githubusercontent.com/rajeshr6r/ml_as_a_service/main/azure/azuredeploy.json)


### AWS

### GCP
