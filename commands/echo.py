import sys, json

if len(sys.argv) > 2:
  if len(sys.argv) > 4:
    if sys.argv[3] == ">":
      with open("metadata.json", "r") as jso:
        with open("Drives/" + json.load(jso)["dir"] + "/" + sys.argv[4], "w+") as file:
          file.write(sys.argv[2])
          file.close()
        jso.close()
  else:
    print(sys.argv[2])