# autodeploy
Python auto deploy for servicesapi
## Pre-installation
```bash
sudo pacman -S caddy
sudo caddy reverse-proxy --from example.org --to localhost:8000
```

## Installation
```bash
git clone https://github.com/holovin777/autodeploy.git
cd autodeploy
python -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```
## Create service unit
```bash
sudo systemctl --force --full edit autodeploy.service
```
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
