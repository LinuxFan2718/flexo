import fileinput
import time
import sys

timestamp = str(int(time.time()))
logfile = timestamp + "flexo.log"
log = open(logfile, "x")

for line in fileinput.input():
  log.write(line)
  sline = line.rstrip()
  if(sline == "uci"):
    print("id name Flexo Alpha")
    print("id author Dennis Cahillane")
    print()
    print("uciok")
  elif(sline == "isready"):
    print("readyok")
  elif(sline == "ucinewgame"):
    pass
  elif(sline == "stop"):
    print("bestmove e2e4")
  elif (sline in ["quit","exit"]):
    log.close()
    sys.exit(0)
  else:
    sys.exit("unknown: " + sline)

