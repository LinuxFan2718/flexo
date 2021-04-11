import fileinput
import time
import sys
import chess
import random

timestamp = str(int(time.time()))
logfile = "/tmp/flexo-" + timestamp + ".log"
log = open(logfile, "x")

for line in fileinput.input():
  log.write(line)
  log.flush()
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
    # access the chess board and choose a random move
    board = chess.Board()
    legal_moves = list(board.legal_moves)
    random_move = random.choice(list(legal_moves))
    print(f"bestmove {random_move.uci()}")
    pass
  elif(command.startswith("position")):
    # extract the FEN from the command
    # create a chess Board with that FEN, or startpos
    # store the chess board to be ready for when go is called
    pass
  elif(command == "stop"):
    pass
    # maybe call go function instead
  elif(command.startswith("setoption")):
    pass
  elif (command in ["quit","exit"]):
    log.close()
    sys.exit(0)
  else:
    log.close()
    print("unknown: " + command)
    sys.exit("unknown: " + command)

