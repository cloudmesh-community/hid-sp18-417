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
 - Download the package from :
    https://www.raspberrypi.org/downloads/noobs/
 - Download and unzip the package and copy it to the SD card
 ensure that the SD card is formatted before you copy
 [Copy only the files inside NOOBS_{version}]
 - Connect the power cable, keybboard and mouse to the Pi
 - Insert the SD card and the installed will walk you through the installation process
 - Once the installation is through make sure the time and keyboard setting are updated according to your local settings
  Normally they come in UK settings
 
  

## Setting up Static IP and HostName

HostName:
Hostname can be given by clicking the top right wifi icon> network setting>

or by :

``
sudo nano /etc/hostname
``

static IP similarly can be given by
Hostname can be given by clicking the top right wifi icon> network setting>
make sure you give both etho and wlan0 setting for both LAN and Wifi communication

or by ensuring the following in ``/etc/dhcpcd.conf``

```
interface eth0
static ip_address={desired IP}/24
static routers={router IP}
static domain_name_servers={DNS server IP}
```
Ensure that the desired IP falls with in the assigned IP range of your router.
As we will be automating the process later, its advised to follow a naming sequence for the hostname and IP address
Example: kub00/192.168.56.100, kub01/192.168.56.101, kub02/192.168.56.102...

Its essential to ``reboot`` the system for the changes to take effect.



