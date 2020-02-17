#!/bin/bash

USER=wuhan
DATABASE=wuhan_need_you
DATABASE_TEST=wuhan_need_you_test
PASSWORD=1234567890
ROOT=$(dirname `readlink -f $0`)/..
BACKUP=$ROOT/backup

install() {
	apt-get update
	apt install postgresql postgresql-client
}

init() {
	su -u postgres
    # create a user if not exist
    psql -tc "SELECT 1 FROM pg_roles WHERE username='$USER'" | grep -q 1 \
    	|| psql -c "create role $USER with login password '$PASSWORD';"
    # create a database if not exist
    psql -c "SELECT 1" -d $DATABASE &>/dev/null \
    	|| createdb --owner $USER $DATABASE
    psql -c "SELECT 1" -d $DATABASE_TEST &>/dev/null \
    	|| createdb --owner $USER $DATABASE_TEST
    
    echo "Databases are created, connect it with "
    echo "\t$USER:$PASSWORD@localhost/$DATABASE"
    echo "\t$USER:$PASSWORD@localhost/$DATABASE_TEST"
}

delete() {
	su -u postgres
    psql -c "DROP ROLE $USER"
	echo "User $USER is deleted"
    psql -c "DROP DATABASE $DATABASE"
	echo "Database $DATABASE is deleted"
    psql -c "DROP DATABASE $DATABASE_TEST"
	echo "Database $DATABASE_TEST is deleted"
}

backup() {
	if ! [ -d $BACKUP ]; then
		mkdir $BACKUP
	fi
	FILE=$BACKUP/$DATABASE-`date +%Y%m%d-%H%M%S`.dump
	pg_dump -U $USER -Fc $DATABASE >$BACKUP/$DATABASE-`date +%Y%m%d-%H%M%S`.dump
	echo "Database is backuped to $FILE"
}

restore() {
	su -u postgres
	latest=`ls -1 -rt $BACKUP/*.dump 2>/dev/null | tail -1`
	if [ -z "$latest" ]; then
		echo "ERROR: no backup exists"
		exit 1
	fi
	pg_restore -Fc --role=$USER $BACKUP/$latest \
		&& echo "Database is restored from $BACKUP/$latest"
}

check() {
	PGPASSWORD=$PASSWORD psql -U $USER -c "SELECT * FROM pg_catalog.pg_tables;" $DATABASE >/dev/null 2>&1 \
		|| echo "Database $DATABASE is ready"
	PGPASSWORD=$PASSWORD psql -U $USER -c "SELECT * FROM pg_catalog.pg_tables;" $DATABASE_TEST >/dev/null 2>&1 \
		|| echo "Database $DATABASE_TEST is ready"
}

help() {
	echo "USAGE: $0 install|init|delete|backup|restore|check"
}

if (( $# == 0 )); then
	help
	exit 1
fi

case $1 in
	install)
		install
		;;
	init)
		init
		;;
	delete)
		delete
		;;
	backup)
		backup
		;;
	restore)
		restore
		;;
	check)
		check
		;;
	*)
		echo "Unknown command $1"
		help
		echo 1
		;;
esac
