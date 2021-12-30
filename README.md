# ml_as_a_service
A setup for providing ML As a Service with any Cloud Provider

## Background and Objective

One of the greatest challenges faced by a Data Scientist is getting their <b>sophisticated ML Model running successfully in their laptops</b> to the end user. So many tools are available and yet everything requires the Data Scientist to learn additional toolkits to proceed. <b> Not to mention the complexities involved in provisioning resources both hardware / software and all the other additional costs involved </b>

Some of the key critical challenges involved in deploying a model to production excluding the TCO ( total cost of ownership ) are 

<list>
  <li>a. Scalability </li>
  <li>b. Accessibility </li>
  <li>c. Usability</li>
  <li>d. Security</li>
 </list></br>
  
Our purpose to is to address the above problems with a one-stop solution on cloud

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
