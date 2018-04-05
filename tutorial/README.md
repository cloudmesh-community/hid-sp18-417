# Setting up Raspberry Pi Kubernetes Cluster

This tutorial will guide the steps towards setting up a Kubernetes Pi cluster.
The steps are:
a. Setting up static IP
b. Secure ssh key setup for communication
c. Kubenetes cluster setup
d. Aumating the process

Cluster needs:
1. One head/master Pi
2. number of follower nodes Pi
3. router [optional]

Pis can be connected directly to the home's Internet router.
Please note that a router is needed when portability is a criteria. 
## Initial Setup
Some Pi kids come with pre installed SD card if not then:
 - download the package from :
    https://www.raspberrypi.org/downloads/noobs/
 - download and unzip the package and copy it to the SD card
 ensure that the SD card is formatted before you copy
 [Copy only the files inside NOOBS_<version>]
 - connect the power cable, keybboard and mouse to the Pi
 - insert the SD card and the installed will walk you through the installation process
 - Once the installation is through make sure the time and keyboard setting are updated according to your local settings
  Normally they come in UK settings
 
  

## Setting up static IP and HostName

The s

