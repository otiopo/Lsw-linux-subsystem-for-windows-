import os, sys

if len(sys.argv) > 2:
  if os.path.isdir("Drives/C:/Windows/minidump"):
    if os.path.isfile("Drives/C:/Windows/minidump/" + sys.argv[2]):
      print("Found Dump File!")
    else:
      print("Failed To Find Dmp File!")
  else:
    print("minidump directory wasn't found!")