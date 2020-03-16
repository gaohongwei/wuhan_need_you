#!/bin/bash

#
# A script to back static/upload
#

APP_ROOT=/usr/local/wuhan_need_you
UPLOAD=$APP_ROOT/app/static/upload
ROOT=$(dirname `greadlink -f $0`)/..
BACKUP=$ROOT/backup

# backup [backup_dir]
backup() {
	if ! [ -d $UPLOAD ]; then
		echo "ERROR: $UPLOAD not exist, maybe it is not installed"
		exit 1
	fi
	DIR=${1:-$BACKUP}
	FILE=$DIR/upload-`date +%Y%m%d-%H%M%S`.tar.gz
	if ! [ -d $DIR ]; then
		mkdir -p $DIR
	fi
	cd $UPLOAD
	tar czvf $FILE * >/dev/null 2>&1 \
		&& echo "Backup to $FILE success" \
		|| echo "Backup failed"
}

# restore [restore-xx-xx-xx.tar.gz]
restore() {
	default_latest=`ls -1 -rt $BACKUP/*.tar.gz 2>/dev/null | tail -1`
	latest=${1:-$default_latest}
	if [ -z "$latest" ]; then
		echo "ERROR: no backup exists"
		exit 1
	fi
	cd $UPLOAD
	tar xzvf $latest >/dev/null 2>&1 \
		&& echo "Restore from $latest successfully" \
		|| echo "Restore from $latest failed"
}

help() {
	echo "USAGE: $0 backup [backup_dir] | restore [backup_file.tar.gz]"
}

if (( $# == 0 )); then
	help
	exit 0
fi

CMD=$1
shift
case $CMD in
	backup)
		backup $@	
		;;
	restore)
		restore $@
		;;
	*)
		echo "Unknown command $1"
		help
		echo 1
		;;
esac
