import os, sys, etc

if len(sys.argv) > 2:
  os.remove("Drives/" + etc.getDir() + "/" + sys.argv[2])