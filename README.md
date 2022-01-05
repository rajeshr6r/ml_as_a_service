# Machine Learning Models as a Service

A Cloud Vendor Agnostic setup for providing deploying Machine Learning Models As a Service.

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

## High Level Flow
![Alt text](https://github.com/rajeshr6r/ml_as_a_service/blob/main/assets/highlevelflow.png "High Level Flow")

## OUT OF SCOPE
<b>This repo will use boilerplate model training / deployment scripts and will not demonstrate how a model is being trained or can be fine-tuned. We assume that the models are pre-built and ready to deploy.</b>


## TODO
### Docker
:heavy_check_mark:a. Basic Image recognition IRIS Model in a container <br>
:heavy_check_mark:b. endpoint definition <br>
:heavy_check_mark:c. Deployment to Dockerhub as a public image <br>

### Cloud Resources to be deployed 

Using generic names for components . Equivalent vendor specific component can be deployed with Terraform

a. Cloud Function for storing requests to do async inference <br>
b. Queue for processing async inference requests <br>
c. Storage for processing results from async inferences <br>
d. Container Registry <br>
e. Container Image hosting the ML Model <br>


### Terraform
a. Terraform script to deploy resources to relevant Cloud provider
