#!/bin/bash

# A script to manipulate the postgresql database
#
# Envrionment variables
#
#   DB_USER: default wuhan
#   DB_PASSWORD: default 1234567890
#
# If the user want to change the default user and password, set it first, e.g.
#
#   DB_USER=another_user DB_PASSWORD=another_password sudo database.sh init 
#

USER=${DB_USER:-wuhan}
PASSWORD=${DB_PASSWORD:-1234567890}
DATABASE=wuhan_need_you
DATABASE_TEST=wuhan_need_you_test
DB_HOST=${DB_HOST:-127.0.0.1}
ROOT=$(dirname `readlink -f $0`)/..
BACKUP=$ROOT/backup

install() {
	apt-get update
	apt install postgresql postgresql-client
}

# init the database if user/tables do not exist
init() {
    # create a user if not exist
    sudo -u postgres psql -tc "SELECT 1 FROM pg_roles WHERE rolname='$USER'" | grep -q 1 \
    	|| sudo -u postgres psql -c "create role $USER with login password '$PASSWORD';"
    # create a database if not exist
    sudo -u postgres psql -c "SELECT 1" -d $DATABASE &>/dev/null \
    	|| sudo -u postgres createdb --owner $USER $DATABASE
    sudo -u postgres psql -c "SELECT 1" -d $DATABASE_TEST &>/dev/null \
    	|| sudo -u postgres createdb --owner $USER $DATABASE_TEST
    
    echo "Databases are created, connect it with "
    echo -e "\t$USER:$PASSWORD@localhost/$DATABASE"
    echo -e "\t$USER:$PASSWORD@localhost/$DATABASE_TEST"
}

delete() {
    sudo -u postgres psql -c "DROP DATABASE $DATABASE" >/dev/null 2>&1 \
		&& echo "[DONE] Database $DATABASE is deleted" \
		|| echo "[FAIL] Database $DATABASE fail to delete"
    sudo -u postgres psql -c "DROP DATABASE $DATABASE_TEST" >/dev/null 2>&1 \
		&& echo "[DONE] Database $DATABASE_TEST is deleted" \
		|| echo "[FAIL] Database $DATABASE_TEST fail to delete"
    sudo -u postgres psql -c "DROP ROLE $USER" >/dev/null 2>&1 \
		&& echo "[DONE] Role $USER is deleted" \
		|| echo "[FAIL] Role $USER fail to delete"
}

# backup [backup.dump]
backup() {
	FILE=${1:-$BACKUP/$DATABASE-`date +%Y%m%d-%H%M%S`.dump}
	if ! [ -d `dirname $FILE` ]; then
		mkdir -p `dirname $FILE`
	fi
	sudo -u postgres pg_dump -Fc -d $DATABASE >$FILE \
		&& echo "[DONE] Database $DATABASE is saved to $FILE" \
		|| echo "[FAIL] Database $DATABASE fail to save to $FILE"
}

# count_table dbname tbname
count_table() {
	count=`PGPASSWORD=$PASSWORD psql -h $DB_HOST -U $USER -t -c "SELECT count(*) FROM $2;" $1 2>/dev/null`
	count=${count#"${count%%[![:space:]]*}"}
	count=${count%"${count##[![:space:]]*}"}
	echo $count
}

# restore [restore.dump]
restore() {
	default_latest=`ls -1 -rt $BACKUP/*.dump 2>/dev/null | tail -1`
	latest=${1:-$default_latest}
	if [ -z "$latest" ]; then
		echo "ERROR: no backup exists"
		exit 1
	fi
	sudo -u postgres pg_restore -Fc --role=$USER -d $DATABASE $latest >/dev/null 2>&1

	echo "Delete the database and init it before restore"
	echo -e "\t sudo ./database.sh delete"
	echo -e "\t sudo ./database.sh init"
	echo "There may be some errors when restoring, but it may be harmless. Just check the tables"

	count=`count_table $DATABASE tags` \
		&& echo "[DONE] Table $DATABASE.tags has rows=$count" \
		|| echo "[FAIL] Count table $DATABASE.tags failed"
	count=`count_table $DATABASE users` \
		&& echo "[DONE] Table $DATABASE.users has rows=$count" \
		|| echo "[FAIL] Count table $DATABASE.users failed"
	count=`count_table $DATABASE notices` \
		&& echo "[DONE] Table $DATABASE.notices has rows=$count" \
		|| echo "[FAIL] Count table $DATABASE.notices failed"
	count=`count_table $DATABASE caches` \
		&& echo "[DONE] Table $DATABASE.caches has rows=$count" \
		|| echo "[FAIL] Count table $DATABASE.caches failed"
}

# check_table dbname tbname
check_table() {
	count=`count_table` 2>/dev/null \
		&& echo "[DONE] Table $2 is ready, nrows=${count}" \
		|| echo "[FAIL] Table $1.$2 is NOT ready" 
}

check() {
	PGPASSWORD=$PASSWORD psql -h $DB_HOST -U $USER -c "SELECT * FROM pg_catalog.pg_tables;" $DATABASE >/dev/null 2>&1 \
		&& echo "[DONE] Database $DATABASE is ready" \
		|| echo "[FAIL] Database $DATABASE is NOT ready" 
	PGPASSWORD=$PASSWORD psql -h $DB_HOST -U $USER -c "SELECT * FROM pg_catalog.pg_tables;" $DATABASE_TEST >/dev/null 2>&1 \
		&& echo "[DONE] Database $DATABASE_TEST is ready" \
		|| echo "[FAIL] Database $DATABASE_TEST is NOT ready" 
	check_table $DATABASE caches
	check_table $DATABASE tags
}

help() {
	echo "USAGE: $0 install|init|delete|backup|restore|check"
}

if (( $# == 0 )); then
	help
	exit 1
fi

CMD=$1
shift
case $CMD in
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
		backup $@
		;;
	restore)
		restore $@
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
