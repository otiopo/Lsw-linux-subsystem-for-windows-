import os, json
from commands import etc

dire = ""

with open("metadata.json", "w") as file:
  file.write(json.dumps({"dir": "C:/Windows/System32"}))
  file.close()

print("Lsw 1.0")

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