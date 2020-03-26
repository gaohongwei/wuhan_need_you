#!/bin/bash

NAME=wuhan_need_you
ROOT=/usr/local/$NAME
mkdir -p $ROOT
find $ROOT \( -name upload -prune -o -name logs -prune \) -o -type f -exec rm {} + >/dev/null 2>&1
SRC_DIR=`dirname $(readlink -f $0)`/..
cd $SRC_DIR

# Configure nginx
apt-get update
apt install -y nginx python3 python3-pip postgresql postgresql-client
if ! [ -f /etc/nginx/nginx.conf.bak ]; then
	cp /etc/nginx/nginx.conf /etc/nginx/nginx.conf.bak
fi
cp deploy/nginx.conf /etc/nginx/
systemctl restart nginx
systemctl enable nginx
nginx -s reload
systemctl restart postgresql
systemctl enable postgresql

# Install server
cp -r * $ROOT/
pip3 install -r requirements.txt

# Install service
cp deploy/$NAME.service /etc/systemd/system/
systemctl daemon-reload
systemctl restart $NAME
systemctl enable $NAME
systemctl status --no-pager $NAME

