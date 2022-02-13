import subprocess
import os

os.chdir("/home/admin/servicesapi")
subprocess.run(["python", "-m", "uvicorn", "main:app"])
