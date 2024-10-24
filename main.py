import subprocess
try:
    pg = "python modules.py"
    subprocess.run(pg, shell=True, check=True)
except Exception as e:
    print(f"Error:{e}")
try:
    pg = "python create_data.py"
    subprocess.run(pg, shell=True, check=True)
except Exception as e:
    print(f"Error:{e}")

try:
    pg = "python newloginpage2.py"
    subprocess.run(pg, shell=True, check=True)
except Exception as e:
    print(f"Error:{e}")