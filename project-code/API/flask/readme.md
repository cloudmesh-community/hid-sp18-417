# Python-Flask App for Stocks Analysis
This a python application that uses:

      - Flask server as rest service
      - qyandl module for fetching real-time stocks data
      - pygal to render graph data
      - boorstrap for modularization of web application
      - docker-compose for managing the container
      - yml for kubernetes configuration deployment
      - html for web development
 
 ## API
 The entrypoint for the python api is ```/app/main.py```
 The versions are : Python 2.7, flask: 0.10.1.
The app fetches realitime WIKI stocks data using python quandl module and renders pygal graph for visual appeal. 

Please note that the quandl code in `main.py` needs to be restored for the API to work.

## docker-compose
Deploying the service to kubectl cluster will need docker-compose.
Here is the installation instruction for docker-compose:
```
sudo curl -L https://github.com/docker/compose/releases/download/1.18.0/docker-compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
```
 ## Kubernetes Deployment
Once the kubectl cluster is up and running. Us the following command to deploy the service to the cluster:
```
docker-compose up -d
kubectl apply -f kubernetes/flask-web-ui.yml
```
