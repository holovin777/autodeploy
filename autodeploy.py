import subprocess
import os

os.chdir("/home/admin/servicesapi")
subprocess.run(["source", "venv/bin/activate"])
subprocess.run(["uvicorn", "main:app"])
subprocess.run(["caddy", "reverse-proxy", "--from", "api.dottore.link", "--to", "localhost:8000"])
