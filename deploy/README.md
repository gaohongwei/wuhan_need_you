
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

## Deploy website

