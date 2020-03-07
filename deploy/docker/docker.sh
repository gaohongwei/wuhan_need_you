#!/bin/bash

IMAGE_NAME=ubuntu-18.04-server
CONTAINER_NAME=wuhan_need_you
APP_DIR=/app/wuhan_need_you

is_mac() {
	uname -a | grep Darwin >/dev/null
}

goto_docker_dir() {
	if is_mac; then
		cd `dirname $(greadlink -f $0)`
	else
		cd `dirname $(readlink -f $0)`
	fi
}

build() {
	goto_docker_dir
	docker build -t $IMAGE_NAME .
}

run() {
	docker stop $CONTAINER_NAME >/dev/null 2>&1
	docker rm $CONTAINER_NAME >/dev/null 2>&1
	docker run -d --privileged -p 8122:22 -p 8180:80 -p 8150:5000 --name $CONTAINER_NAME $IMAGE_NAME 
}

deploy() {
	goto_docker_dir
	docker exec -it $CONTAINER_NAME mkdir -p $APP_DIR
	for i in ../../*; do
		docker cp $i $CONTAINER_NAME:$APP_DIR
	done
	docker exec -it $CONTAINER_NAME $APP_DIR/deploy/install.sh
	test
}

test() {
	if wget -t 1 127.0.0.1:8180 >/dev/null 2>&1; then
		echo 'TEST SUCCESS'
	else
		echo 'TEST FAILED'
	fi
}

db() {
	docker exec -it $CONTAINER_NAME $APP_DIR/deploy/database.sh $@
}

help() {
	echo "USAGE: $0 build|run|deploy|test|db"
}

if (( $# == 0 )); then
	help
	exit 1
fi

case $1 in
	build)
		build
		;;
	run)
		run
		;;
	deploy)
		deploy
		;;
	test)
		test
		;;
	db)
		db $@
		;;
	*)
		help
		;;
esac
