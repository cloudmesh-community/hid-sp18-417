#!/bin/sh

ip=$1 # should be of format: 192.168.1.100
dns=$2 # should be of format: 192.168.1.1

# Set the static ip

sudo cat <<EOT >> /etc/dhcpcd.conf
interface eth0
static ip_address=$ip/24
static routers=$dns
static domain_name_servers=$dns
EOT
