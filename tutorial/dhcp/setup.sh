#!/bin/sh

ip=$1 # should be of format: 192.168.1.100
dns=$2 # should be of format: 192.168.1.1
echo "Installing Dependencies ..."
apt-get update
apt-get install -qy dnsmasq clusterssh iptables-persistent

echo "Setting Up Head Node ..."

# Set the static ip

sudo cat <<EOT >> /etc/dhcpcd.conf
interface eth0
static ip_address=$ip/24
static routers=$dns
static domain_name_servers=$dns

interface wlan0
static ip_address=$ip/24
static routers=$dns
static domain_name_servers=$dns
EOT
