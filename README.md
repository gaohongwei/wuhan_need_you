# Wuhan Need You

A [website](http://wuhanuniversity.org/) for publishing donation information to the people fighting Coronavirus.

## Development

First time
```
mkdir -p ~/works
cd ~/works
git clone https://github.com/gaohongwei/wuhan_need_you.git
cd wuhan_need_you
git checkout feature/web_beauty
pip3 install virtualenv
virtualenv venv
source ~/works/wuhan_need_you/venv/bin/activate
pip3 install -r requirements.txt
python3 run.py
```

Not first time
```
cd ~/works/wuhan_need_you
source ~/works/wuhan_need_you/venv/bin/activate
python3 run.py
```

Open in chrome to access the pages: http://0.0.0.0:5000/

To exit development environment
```
ctrl+c
deactivate
```

## Internationalization

The multiple languages support follows this [instructions](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xiii-i18n-and-l10n)

The command will be used as:

```bash
(venv) $ flask translate --help
Usage: flask translate [OPTIONS] COMMAND [ARGS]...

  Translation and localization commands.

Options:
  --help  Show this message and exit.

Commands:
  compile  Compile all languages.
  init     Initialize a new language.
  update   Update all languages.
```

## Deployment

The website is powered by flask+uwsgi+nginx.

```bash
git clone https://github.com/gaohongwei/wuhan_need_you.git
cd wuhan_need_you
git checkout dev
sudo deploy/install.sh
```

If everything is OK, `http://127.0.0.1` is available, e.g. `wget http://127.0.0.1`.

For external access, make sure the server has port `80` open.

To check the status of the server
```bash
sudo systemctl status wuhan_need_you
```

To restart the server
```bash
sudo systemctl restart wuhan_need_you
```

To update, just update the repository and re-install.
```bash
git pull
git checkout dev
sudo deploy/install.sh
```

**NOTE**: The deploy scripts are only tested on Ubuntu18.04.

