#!/bin/bash

IMAGE_NAME=ubuntu-18.04-server
CONTAINER_NAME=wuhan_need_you
APP_DIR=/app/wuhan_need_you
APP_SERVICE=wuhan_need_you

is_mac() {
	uname -a | grep Darwin >/dev/null
}

goto_docker_dir() {
	if is_mac; then
		# `brew install greadlink` beforehand
		cd `dirname $(greadlink -f $0)`
	else
		cd `dirname $(readlink -f $0)`
	fi
}

# build the image of ubuntu server 18.04
build() {
	goto_docker_dir
	docker build -t $IMAGE_NAME .
}

# run/restart the image as container
restart() {
	docker stop $CONTAINER_NAME >/dev/null 2>&1
	docker rm $CONTAINER_NAME >/dev/null 2>&1
	docker run -d --privileged -p 8122:22 -p 8180:80 -p 8150:5000 --name $CONTAINER_NAME $IMAGE_NAME 
}

# deploy the webiste to the container
deploy() {
	goto_docker_dir
	docker exec -it $CONTAINER_NAME mkdir -p $APP_DIR
	for i in ../../*; do
		docker cp $i $CONTAINER_NAME:$APP_DIR
	done
	docker exec -it $CONTAINER_NAME $APP_DIR/deploy/docker/init_tz.sh
	db install
	db init
	docker exec -it $CONTAINER_NAME $APP_DIR/deploy/install.sh
	echo 'Wait 5 seconds to test the website'
    sleep 5
    test
	echo 'If not success, try "sudo ./docker.sh test" a few times again'
}

# start the website
start_website() {
    docker exec -it $CONTAINER_NAME systemctl restart $APP_SERVICE
}
# stop the website
stop_website() {
    docker exec -it $CONTAINER_NAME systemctl stop $APP_SERVICE
}

test() {
	BASE=127.0.0.1:8180
	for url in / /api/reports/overall /api/reports/world /api/reports/provinces; do
		if wget -t 1 $BASE/$url -O - >/dev/null 2>&1; then
			echo "[DONE] $BASE/$url"
		else
			echo "[FAIL] $BASE/$url"
		fi
	done
}

# db operation
db() {
	docker exec -it $CONTAINER_NAME $APP_DIR/deploy/database.sh $@
}

help() {
	echo "USAGE: $0 build|restart|deploy|stop_website|start_website|test|db"
}

if (( $# == 0 )); then
	help
	exit 1
fi

cmd=$1
shift
case $cmd in
	build)
		build
		;;
	restart)
		restart
		;;
	deploy)
		deploy
		;;
    stop_website)
        stop_website
        ;;
    start_website)
        start_website
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
