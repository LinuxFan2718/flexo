import time
import sys
import chess
import random

timestamp = str(int(time.time()))
logfile = "/tmp/flexo-" + timestamp + ".log"
log = open(logfile, "x")
stdin_fileno = sys.stdin
stdout_fileno = sys.stdout
 
for line in stdin_fileno:
  log.write(line)
  log.flush()
  command = line.rstrip()
  if(command == "uci"):
    stdout_fileno.write("id name Flexo Alpha" + '\n')
    stdout_fileno.write("id author Dennis Cahillane" + '\n')
    stdout_fileno.write('\n')
    stdout_fileno.write("uciok" + '\n')
  elif(command == "isready"):
    stdout_fileno.write("readyok" + '\n')
  elif(command == "ucinewgame"):
    pass
  elif(command.startswith("go")):
    # access the chess board and choose a random move
    board = chess.Board()
    legal_moves = list(board.legal_moves)
    random_move = random.choice(list(legal_moves))
    stdout_fileno.write(f"bestmove {random_move.uci()}" + '\n')
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
    stdout_fileno.write("unknown: " + command + '\n')
    sys.exit("unknown: " + command)

  stdout_fileno.flush()

