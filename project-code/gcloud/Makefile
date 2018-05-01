gcloud-install:
	# Create environment variable for correct distribution
	export CLOUD_SDK_REPO='cloud-sdk-$(lsb_release -c -s)'

	# Add the Cloud SDK distribution URI as a package source
	echo 'deb http://packages.cloud.google.com/apt $CLOUD_SDK_REPO main' | sudo tee -a /etc/apt/sources.list.d/google-cloud-sdk.list

	# Import the Google Cloud Platform public key
	curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add -

	# Update the package list and install the Cloud SDK
	sudo apt-get update && sudo apt-get install google-cloud-sdk

	# Install kubectl
	sudo apt-get update
	sudo apt-get install kubectl

gcloud-init:
	gcloud init
	
cluster-create:
	 gcloud container clusters create cluster01
	
kubectl-deploy:
	kubectl run [SERVICE_NAME] --image [IMAGE_NAME] --port [port number]
	kubectl expose deployment [SERVICE_NAME] --type 'LoadBalancer'

gcloud-remove-cluster:
  	kubectl delete service [SEVICE_NAME]
  	kubectl delete deployment [DEPLOYMENT_NAME]
  	gcloud container clusters delete [CLUSTER_NAME]
