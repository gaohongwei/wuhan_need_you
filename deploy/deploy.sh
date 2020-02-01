#!/bin/bash

# Setup server in ~/.ssh/config
# For example
# 
# Host wuhan
# 	HostName xxx-x-xxx-xxx-xxx.xx-xxxx-2.compute.amazonaws.com
# 	User ubuntu
# 	IdentityFile ~/.ssh/key.pem

SERVER=wuhan
SRC_DIR=`dirname $(readlink -f $0)`/..
cd $SRC_DIR
scp -r ../wuhan_need_you $SERVER:/usr/local/
ssh -t $SERVER "sudo /usr/local/wuhan_need_you/deploy/install.sh"

