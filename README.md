# Machine Learning As A Service

## Background and Objective

One of the greatest challenges faced by a Data Scientist is getting their <b>sophisticated ML Model running successfully in their laptops</b> to the end user. So many tools are available and yet everything requires the Data Scientist to learn additional toolkits to proceed. <b> Not to mention the complexities involved in provisioning resources both hardware / software and all the other additional costs involved </b>

Some of the key critical challenges involved in deploying a model to production excluding the TCO ( total cost of ownership ) are 

<list>
  <li>a. Repeatability - <b>works in my machine i don't know about yours.</b></li>
  <li>b. Scalability - <b>takes a long time to do predictions in a large number.</b></li>
  <li>c. Accessibility - <b>unable to access the model due to network issues</b></li>
  <li>d. Usability - <b>user doesn't know how to interact with the model.</b></li>
  <li>e. Security - <b>how to secure the model consumption?</b></li>
  <li>f. CI-CD - <b>fail fast , build great.</b></li>
  <li>g. Knowledge - <b>I'm a data scientist. I don't know what is CICD.</b></li>
 </list></br>

 
## High Level Flow
![Alt text](https://github.com/rajeshr6r/ml_as_a_service/blob/main/assets/highlevelflow.png "High Level Flow")

## OUT OF SCOPE
<b>This repo will use boilerplate model training / deployment scripts and will not demonstrate how a model is being trained or can be fine-tuned. We assume that the models are pre-built and ready to deploy.</b>

## Our Toolkit
1. Python - REST API with FastAPI to wrap complexities involved in docker image generation
2. Docker - Generate docker container images to enable rapid prototyping and fast iterations from development to production  
3. Terraform - IAC component to deploy assets to relevant cloud
4. Ready-made container images with commonly used ML packages to reduce image build duration. 

## Commonly used python packages in Machine Learning 
<i>sk-learn,pandas,matplotlib,numpy,nltk</i>

## Key Benefits :<br>
a. Isolate the complexities involved in docker tasks<br>
b. Centralized controls for building high quality , secure images for consumption<br>
c. Automated Versioning , logging .<br>

## TODO
### Docker
:heavy_check_mark:a. Basic Image recognition IRIS Model in a container <br>
:heavy_check_mark:b. endpoint definition <br>
:heavy_check_mark:c. Deployment to Dockerhub as a public image <br>


### Python
:heavy_check_mark:a.Flask API to build docker images dynamically based on parameters sent <br>
:heavy_check_mark:b.Endpoint / route definition <br>
:heavy_check_mark:c.Testing endpoints to verify if docker images are being built<br>
:heavy_check_mark:d.Testing endpoints to push ML payloads such as model files , package requirements and server.py file<br>

### Anatomy of a container image serving an ML Model

<img src="https://imgur.com/4UF2spb.png" />

### Structure of the server.py used for inference

<img src="https://imgur.com/wWsujw3.png" />

### Cloud Resources to be deployed 

1. Central Docker Server - Typically an <b>EC2 / Azure VM / GCP Compute engine</b> that  hosts the REST API and docker setup for facilitating docker build tasks , repo connectivity
2. Github Repo - hosts the dockerfile templates and python scripts 
3. Object Storage - <b> S3 / Azure Blob Storage / Google Storage bucket</b> for backup of incoming assets / docker images . 
4. Persistent Storage - <b> EBS / Managed Disk / Persistent Disk </b> for installing necessary software in the hosting server

### Terraform
a. Terraform script to deploy resources to relevant Cloud provider

#### Product Enhancement Scope

<list>
<li>1. Integrate <a href=https://mlflow.org/>MLFlow</a>    and provide centralized model tracking , observability features</li>
<li>2. Integrate Feature store capability for reducing Pre-processing turnaround.</li>
<li>3. ML Product monetization capabilities</li>
</list>





