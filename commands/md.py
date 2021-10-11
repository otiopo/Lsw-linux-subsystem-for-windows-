import sys, etc, os

if len(sys.argv) > 2:
  os.mkdir("Drives/" + etc.getDir() + "/" + sys.argv[2])