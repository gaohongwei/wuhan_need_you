#!/bin/bash

#
# Avoid interactive interface of tzdata configuration when installing in docker
#

export DEBIAN_FRONTEND=noninteractive
apt-get update
apt install -y tzdata
ln -fs /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
dpkg-reconfigure -f noninteractive tzdata

