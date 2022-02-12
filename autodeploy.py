import subprocess
import os

os.chdir("/home/admin/servicesapi")
subprocess.run(["python", "-m", "uvicorn", "main:app"])
subprocess.run(["caddy", "reverse-proxy", "--from", "api.dottore.link", "--to", "localhost:8000"])
