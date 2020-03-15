
# Docker environment for testing deployment

These scripts are used to mimick a similar environment of Ubuntu 18.04 host to deploy the website.

## Usage

### Build an image

Create an image named as `Ubuntu-18.04-server`:

```
sudo ./docker.sh build
```

### Run the image as container

Restart/start a container named `wuhan_need_you`:

```
sudo ./docker.sh restart
```

### Deploy the website

Deploy the website on the container, with exposed port `8180`:

```
sudo ./docker.sh deploy
```

### Test the website

Test the website is normal (The first few tries may fail)

```
sudo ./docker.sh test
```

### Stop/restart the website

Before we delete the database, we should stop the website first.

```
sudo ./docker.sh stop_website
```

And restart it with

```
sudo ./docker.sh start_website
```

### Operate the database

```
sudo ./docker.sh db install
sudo ./docker.sh db init 
sudo ./docker.sh db check
sudo ./docker.sh db backup
sudo ./docker.sh db restore
```
