# Wuhan Need You

A [website](http://wuhanuniversity.org/) for publishing donation information to the people fighting Coronavirus.

## Development

```
pip3 install -r requirements.txt
python3 run.py
```

## Deployment

The website is deployed by flask+uwsgi+nginx.

```bash
git clone https://github.com/gaohongwei/wuhan_need_you.git
cd wuhan_need_you
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

**NOTE**: The deploy scripts are only tested on Ubuntu18.04.

