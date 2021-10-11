import json, colorama, random, time, os, sys

def getDir():
  with open("metadata.json", "r") as file:
    return json.load(file)["dir"]
    file.close()

def bsod(errorcode):
  percent = 0
  
  os.system("clear")

  while percent <= 100:
    if percent != 100:
      percent += 10
    else:
      dumpname = str(random.randint(1243478950324789625, 6587345695636489536479364869))
      if not os.path.isdir("Drives/C:/Windows/minidump"):
        os.mkdir("Drives/C:/Windows/minidump")
      print("Dump Created At C:/Windows/minidump/" + dumpname + "!")
      with open("bsod.json", "w") as file:
        file.write(json.dumps({"hasBsodded": "yes"}))
        file.close()
      break
    print(":(" + colorama.Fore.CYAN + "⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜" + colorama.Style.RESET_ALL + "\nYour Computer Ran Into a Problem And Needs To Restart\n" + str(percent) + "\nERROR CODE: " + errorcode, end="\r")
    time.sleep(random.uniform(0.5, 0.8))
    os.system("clear")

def hasBsoded():
  with open("bsod.json", "r") as file:
    return json.load(file)["hasBsodded"]
    file.close()