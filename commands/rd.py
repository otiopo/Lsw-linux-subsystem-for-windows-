import os, sys, etc

if len(sys.argv) > 2:
  os.rmdir("Drives/" + etc.getDir() + "/" + sys.argv[2])