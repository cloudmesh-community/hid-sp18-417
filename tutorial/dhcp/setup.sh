sudo apt-get update
sudo apt-get install git
mkdir /~/cloudmesh
echo installing git
git clone https://github.com/cloudmesh-community/hid-sp18-417.git
cd *417/tutotial/dhcp
echo running initial dhcp setup
sh dhcp_setup.sh raspi01 10.0.1.100 10.0.1.1 208.67.222.222
#!/bin/sh

hostname=$1
ip=$2 # should be of format: 192.168.1.100
router=$3 # should be of format: 192.168.1.1
dns=$4 # should be of format: 192.168.1.1

# Change the hostname
touch hostname
sudo cat <<end>> hostname
hostname
end
sudo cp hostname /etc/hostname
head -n -1 /etc/hosts > temp ; mv temp /etc/hosts
sudo cat <<end11>> /etc/hosts
127.0.0.1     $1
end11

# Set the static ip
echo setting static ip and rebooting...
sudo cat <<EOT >> /etc/dhcpcd.conf
interface eth0
static ip_address=$ip/24
static routers=$router
static domain_name_servers=$dns
interface wlan0
static ip_address=$ip/24
static routers=$router
static domain_name_servers=$dns
EOT
echo rebooting...
reboot
