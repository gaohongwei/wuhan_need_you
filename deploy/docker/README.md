
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

### Init database

```
sudo ./docker.sh db init
```

### Deploy the website

Deploy the website on the container, with exposed port `8180`:

```
sudo ./docker.sh deploy
```

### Test the website

Test the website is normal

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

