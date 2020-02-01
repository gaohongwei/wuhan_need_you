#!/bin/bash

ROOT=/usr/local/wuhan_need_you
rm -rf $ROOT
mkdir -p $ROOT
SRC_DIR=`readlink -f $0`/..
cd $SRC_DIR

# Install server
cp -r * $ROOT/
pip3 install -r requirements.txt

# Install service
cp deploy/wuhan_need_you.service /etc/systemd/system/
systemctl start wuhan_need_you
systemctl enable wuhan_need_you

# Configure nginx
apt install nginx
if ! [ -f /etc/nginx/nginx.conf.bak ]; then
	cp /etc/nginx/nginx.conf /etc/nginx/nginx.conf.bak
fi
cp deploy/nginx.conf /etc/nginx/
nginx -s reload
