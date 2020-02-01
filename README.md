# Wuhan Need You

A website for publishing donation information to WuHan.

## Development

```
pip3 install -r requirements.txt
python3 run.py
```

## Deployment

The website is deployed by flask+uwsgi+nginx.

```bash
sudo deploy/install.sh
sudo systemctl status wuhan_need_you
```

