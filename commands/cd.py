import etc, sys, json, os

if len(sys.argv) > 2:
  di = etc.getDir() + "/" + sys.argv[2]
  if sys.argv[2] == "..":
    d = etc.getDir().split("/")
    f = ""
    
    num = 0

    for thing in d:
      num += 1
      if num != len(d):
        if num != len(d) - 1:
          f += thing + "/"
        else:
          f += thing
    
    di = f
  elif sys.argv[2] == "C:" or sys.argv[2] == "C:/":
    di = "C:"
  if os.path.isdir("Drives/" + di):
    with open("metadata.json", "w") as file:
      file.write(json.dumps({"dir": di}))
      file.close()
  else:
    print(di + " No Such File Or Directory")