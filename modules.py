import subprocess

modules = ["mysql.connector","pillow","tkcalendar"]

for i in modules:
    try:
        subprocess.run(["pip","install",i])
    except:
        print(f"Cannot install module {i}")