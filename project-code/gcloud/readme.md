# Google Cloud for Kubernetes

Google Kubernetes Engine[GKE] is a solution provided by Google Inc for seamless management and deployment for containerized applications.
While leaning about Kubernetes, it was important to explore this google tool for Kubernetes deployment. As both GKE and Kubernetes are developed and maintained by Google, the collaboration is expected to bring is powerful vital usage for the cloud community. 

# Installation:
Here are the steps involved:
1. Google currently provides a free trial of 12 months with $ 300 credit to use the account. An account was created for this purpose.
2. Set up gcloud console locally:
```
# Create environment variable for correct distribution
 export CLOUD_SDK_REPO="cloud-sdk-$(lsb_release -c -s)"

# Add the Cloud SDK distribution URI as a package source
echo "deb http://packages.cloud.google.com/apt $CLOUD_SDK_REPO main" | sudo tee -a /etc/apt/sources.list.d/google-cloud-sdk.list

# Import the Google Cloud Platform public key
curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add -

# Update the package list and install the Cloud SDK
sudo apt-get update && sudo apt-get install google-cloud-sdk
```

Alternatively, the cloud shell from the website can be used as well.

3. Now install kubectl:
```
sudo apt-get install kubectl
```
or 
```
gcloud components install kubectl
```

# gcloud Initiation & Configuration:

Now we are ready to initiate the cloud:
```
gcloud init
```
while initiating gcloud you will go setup the following::
1. Project ID setup: You may setup a new project or use existing projects. The options will be prompted. For changing the project this can be used later as well:
```
gcloud config set project [PROJECT_ID]
```
2. Compute Zone setup: 
```
gcloud config set compute/zone [COMPUTE_ZONE]
```
Here is a list of available compute zones for gcloud. Depending of the compute zone selected the instances will use default processor in that zone. Here is a list of compute zones for GKE:
https://cloud.google.com/compute/docs/regions-zones/#available

## Creating Cluster:
A cluster consists of one master multiple worker machines. gcloud creates a cluster of three nodes by default.
```
gcloud container clusters create [CLUSTER_NAME]

## get authentication to interact with the clusters
gcloud container clusters get-credentials [CLUSTER_NAME]
```

## Deployment:
A containerized docker image can be deployed to the cluster using the following:
```
kubectl run [SERVICE_NAME] --image [IMAGE_NAME] --port [posrt number]
```
Exposing a service to a port will enable external access:
```
kubectl expose deployment [SERVICE_NAME] --type "LoadBalancer"
```
## Access:
After exposing the service the following command will provide the external IP for the service
```
kubectl get service [SERVICE_NAME]
```
Now access the app:
```
http://[EXTERNAL_IP]:[EXPORTED_PORT]
```

## Cleanup :
A resource can be deleted using:
``
kubectl delete pod [POD_NAME]
kubectl delete service [SEVICE_NAME]
kubectl delete deployment [DEPLOYMENT_NAME]
gcloud container clusters delete [CLUSTER_NAME]
``

Its worth noting that if a webservice replicas are defined during depoyment then deleting a pod will automatically generate a new one.
