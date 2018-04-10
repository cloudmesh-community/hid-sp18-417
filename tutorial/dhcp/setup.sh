sudo apt-get update
sudo apt-get install git
mkdir /~/cloudmesh
git clone https://github.com/cloudmesh-community/hid-sp18-417.git
cd *417/tutotial
sh dhcp_setup.sh raspi01 10.0.1.100 10.0.1.1 208.67.222.222
