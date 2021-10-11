import sys, etc

if len(sys.argv) > 2:
  name = ""

  if sys.argv[2].lower() == "/im":
    name = sys.argv[3]
  
  if name == "svchost.exe":
    etc.bsod("CRITICAL_PROCESS_DIED")