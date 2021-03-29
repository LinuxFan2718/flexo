import fileinput
import time
import sys
import chess
import random

timestamp = str(int(time.time()))
logfile = "flexo" + timestamp + ".log"
log = open(logfile, "a", 0)

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
    # extract the FEN from the command
    # create a chess Board with that FEN, or startpos
    board = chess.Board()
    legal_moves = list(board.legal_moves)
    random_move = random.choice(list(legal_moves))
    print(f"bestmove {random_move.uci()}")
    pass
  elif(command.startswith("position")):
    pass
  elif(command == "stop"):
    print("bestmove e2e4")
  elif(command.startswith("setoption")):
    pass
  elif (command in ["quit","exit"]):
    log.close()
    sys.exit(0)
  else:
    sys.exit("unknown: " + command)

