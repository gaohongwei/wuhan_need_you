#!/bin/bash

NAME=wuhan_need_you_stage
ROOT=/usr/local/$NAME
rm -rf $ROOT
mkdir -p $ROOT
SRC_DIR=`dirname $(readlink -f $0)`/..
cd $SRC_DIR

# Configure nginx
apt-get update
apt install -y nginx python3 python3-pip postgresql postgresql-client
if ! [ -f /etc/nginx/nginx.conf.bak ]; then
	cp /etc/nginx/nginx.conf /etc/nginx/nginx.conf.bak
fi
cp deploy/nginx.conf /etc/nginx/
nginx -s reload

# Install server
cp -r * $ROOT/
pip3 install -r requirements.txt

# Install service
cp deploy/$NAME.service /etc/systemd/system/
systemctl daemon-reload
systemctl restart $NAME
systemctl enable $NAME
systemctl status --no-pager $NAME

