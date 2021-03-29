import fileinput
import time
import sys

timestamp = str(int(time.time()))
logfile = timestamp + "flexo.log"
log = open(logfile, "x")

for line in fileinput.input():
  log.write(line)
  command = line.rstrip()
  if(command == "uci"):
    print("id name Flexo Alpha")
    print("id author Dennis Cahillane")
    print()
    print("uciok")
  elif(command == "isready"):
    print("readyok")
  elif(command == "ucinewgame"):
    pass
  elif(command.startswith("go")):
    pass
  elif(command.startswith("position")):
    pass
  elif(command == "stop"):
    print("bestmove e2e4")
  elif (command in ["quit","exit"]):
    log.close()
    sys.exit(0)
  else:
    sys.exit("unknown: " + command)

