import subprocess
import os

os.chdir("/home/admin/servicesapi")
subprocess.run(["source", "venv/bin/activate"])
subprocess.run(["uvicorn", "main:app"])
