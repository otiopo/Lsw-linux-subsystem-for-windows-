import sys, etc

if len(sys.argv) > 2:
  if len(sys.argv) > 4:
    if sys.argv[3] == ">":
      with open("Drives/" + etc.getDir() + "/" + sys.argv[4], "w") as file:
        file.write(sys.argv[2])
        file.close()
  else:
    print(sys.argv[2])