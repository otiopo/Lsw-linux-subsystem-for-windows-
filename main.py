import os, json, platform, GPUtil, psutil, threading, time
from commands import etc

def get_size(bytes, suffix="B"):
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor

dire = ""

with open("metadata.json", "w") as file:
  file.write(json.dumps({"dir": "C:/Windows/System32"}))
  file.close()

print("Lsw 1.0")

print("Running Post Check (press enter to cancel!)")

isCancelled = False

def cancel():
  input()
  isCancelled = True
threading.Thread(target=cancel).start()
count = 6

while isCancelled == False:
  count -= 1
  if count == 0:
    break
  if isCancelled == True:
    break
  os.system("clear")
  print("Lsw 1.0")
  print("Running Post Check (press enter to cancel!)")
  print(str(count) + ".")
  threading.Thread(target=cancel).start()
  time.sleep(1)

print("POST Check...")

print(platform.system() + " (Build " + platform.version() + ")")

gpu = GPUtil.getGPUs()

if len(gpu) > 1:
  print("Multiple GPUs detected!")
elif len(gpu) == 0:
  print("No GPU(s) Found!")

for gp in gpu:
  print(gp.name)

print(get_size(psutil.virtual_memory().total) + " Of Ram")

while True:
  if etc.hasBsoded() == "yes":
    with open("bsod.json", "w") as file:
      file.write(json.dumps({"hasBsodded": "no"}))
      file.close()
    exit()
  else:
    with open("metadata.json", "r") as file:
      jsonData = json.load(file)
      dire = jsonData["dir"]
      file.close()
    command = input(dire + ">")
    os.system("python3 commands/" + command.split(" ")[0] + ".py " + command)