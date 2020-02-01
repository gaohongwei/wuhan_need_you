#!/bin/bash

# A script to deploy the website to an aws server

# Setup server in ~/.ssh/config
# For example
# 
# Host wuhan
# 	HostName xxx-x-xxx-xxx-xxx.xx-xxxx-2.compute.amazonaws.com
# 	User ubuntu
# 	IdentityFile ~/.ssh/key.pem

SERVER=wuhan
ssh -t $SERVER "cd tmp && git clone https://github.com/gaohongwei/wuhan_need_you.git && sudo /tmp/wuhan_need_you/deploy/install.sh"

