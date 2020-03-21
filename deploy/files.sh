#!/bin/bash

#
# A script to back static/upload
#

is_mac() {
	uname -a | grep Darwin >/dev/null
}
get_root_dir() {
	if is_mac; then
		# `brew install greadlink` beforehand
		echo `dirname $(greadlink -f $0)`/..
	else
		echo `dirname $(readlink -f $0)`/..
	fi
}
get_absolute_path() {
	if is_mac; then
		# `brew install greadlink` beforehand
		echo `greadlink -f $1`
	else
		echo `readlink -f $1`
	fi
}
make_dir_for_file() {
	path=`dirname $1`
	mkdir -p $path >/dev/null 2>&1
}

APP_ROOT=/usr/local/wuhan_need_you
UPLOAD=$APP_ROOT/app/static/upload
ROOT=`get_root_dir`
BACKUP=$ROOT/backup

# backup [backup_dir]
backup() {
	if ! [ -d $UPLOAD ]; then
		echo "ERROR: $UPLOAD not exist, maybe it is not installed"
		exit 1
	fi
	DIR=${1:-$BACKUP}
	if ! [ -d $DIR ]; then
		mkdir -p $DIR
	fi
	FILE=`get_absolute_path $DIR`/upload-`date +%Y%m%d-%H%M%S`.tar.gz
	echo "Backup to $FILE..."
	make_dir_for_file $FILE
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
