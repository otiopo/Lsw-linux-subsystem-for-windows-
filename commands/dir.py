import os, json

with open("metadata.json", "r") as file:
  jsonData = json.load(file)
  dire = jsonData["dir"]
  print("Directory of " + dire + "\n")

  di = os.listdir("Drives/" + dire)
  if di:
    for fil in di:
      print(fil)
  else:
    print("Directory is empty!")
  file.close()