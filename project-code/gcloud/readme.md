# Google Cloud for Kubernetes

Google Kubernetes Engine[GKE] is a solution provided by Google Inc for seamless management and deployment for containeraized applications.
While leaning about Kubernetes, it was important to explore this google tool for Kubernetes deployment. As both GKE and Kubernetes are developed and maintained by Google, the collaboration is expected to bring is powerful vital usage for the cloud community. 

Here are the steps involved:

1. Google currently provides a free trial of 12 months with $ 300 credit to use the account. An account was created for this puspose.
2. Now lets set up gcloud console locally:
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

