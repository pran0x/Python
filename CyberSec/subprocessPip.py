import subprocess
result = subprocess.run(["ipconfig/all"], capture_output=True, text=True, shell=True)

with open("ipconfig.txt", "w") as ipAdress:
  ipAdress.write(result.stdout)

