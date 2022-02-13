# autodeploy
Python auto deploy for Fastapi
## Pre-installation
```bash
sudo pacman -S caddy
sudo caddy reverse-proxy --from example.org --to localhost:8000
```
## Installation
```bash
git clone https://github.com/holovin777/autodeploy.git
cd autodeploy
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python autodeploy.py
```
