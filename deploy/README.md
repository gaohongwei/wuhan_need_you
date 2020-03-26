
# Deploy of the website

## Deploy database

```bash
sudo deploy/database.sh install # install db server and client
sudo deploy/database.sh init    # create db and user if not exist
sudo deploy/database.sh check   # check the databases are created successfully
```

To delete databases (**DANGEROUS!!!**)
```bash
sudo deploy/database.sh delete
```

To backup databases
```bash
sudo deploy/database.sh backup   # the files are save in backup/
```

To restore databases
```bash
sudo deploy/database.sh restore # to restore from the latest file in backup/
```

## Before Deploy website, backup notices images

To backup images 
```bash
sudo deploy/files.sh backup backup_img/
```

## After Deploy website, restore notcies images 
To restore images   
```bash
sudo deploy/files.sh restore backup_img/[xxx..tar.gz]
```

## Deploy website

Assume the database has been setup (`sudo deploy/database.sh check` success).

```bash
sudo deploy/install.sh
```

The `username/password` adopts the default in all the settings, which is safe only if the 5432 port is not exposed.

If the administrator wants to use other username and password,
he/she shoud revise `deploy/database.sh`, and set `DEPLOY_DATABASE_URL` in `wuhan_need_you.service`.

