#!/bin/bash 

###################################################################
#Script Name	: Docker + Docker-Compose Install (Ubuntu)
#Description	: Shortcut to set up docker on ubuntu
#Args		: N/A
#Author       	: Harry Thorpe
#Email         	: info@harrythorpe.co.uk                                           
###################################################################

#Install docker using docker docs 14 Nov 2020
sudo apt-get remove docker docker-engine docker.io containerd runc
sudo apt-get update -y
sudo apt-get install apt-transport-https ca-certificates curl gnupg-agent software-properties-common -y
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository \
	   "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
	      $(lsb_release -cs) \
	         stable"
sudo apt-get update -y
sudo apt-get install docker-ce docker-ce-cli containerd.io -y

#Installing for rootless mode
sudo apt install -y uidmap
curl -fsSL https://get.docker.com/rootless | sh

# Docker binaries are installed in /home/thorphar/bin                                                
# WARN: dockerd is not in your current PATH or pointing to /home/thorphar/bin/dockerd                 
# Make sure the following environment variables are set (or add them to ~/.bashrc):
#export PATH=/home/thorphar/bin:$PATH                                                                 #export DOCKER_HOST=unix:///run/user/1000/docker.sock 

echo 'export DOCKER_HOST=unix:///run/user/1000/docker.sock' >> ~/.zshrc
source ~/.zshrc
systemctl --user start docker
systemctl --user enable docker
sudo loginctl enable-linger $(whoami)


#Install docker-compose
sudo apt install docker-compose -y
