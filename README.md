# autodeploy
Python auto deploy for Fastapi
## Pre-installation
```bash
sudo pacman -S caddy
sudo caddy reverse-proxy --from example.org --to localhost:8000
sudo systemctl --force --full edit autodeploy.service
```

## Create service unit
```python
[Unit]
Description=Autodeploy

[Service]
ExecStart=/home/admin/servicesapi/venv/bin/python /home/admin/Repositories/autodeploy/autodeploy.py
User=admin

[Install]
WantedBy=multi-user.target
```
```bash
sudo systemctl daemon-reload
sudo systemctl start autodeploy.service
sudo systemctl status autodeploy.service
sudo systemctl enable autodeploy.service
```
## Installation
```bash
git clone https://github.com/holovin777/autodeploy.git
cd autodeploy
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python autodeploy.py
```
