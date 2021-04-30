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
    stdout_fileno.write("id name Flexo Random" + '\n')
    stdout_fileno.write("id author Dennis Cahillane" + '\n')
    stdout_fileno.write('\n')
    stdout_fileno.write("uciok" + '\n')
  elif(command == "isready"):
    stdout_fileno.write("readyok" + '\n')
  elif(command == "ucinewgame"):
    pass
  elif(command.startswith("go")):
    legal_moves = list(board.legal_moves)
    random_move = random.choice(list(legal_moves))
    stdout_fileno.write(f"bestmove {random_move.uci()}" + '\n')
  elif(command.startswith("position")):
    # position startpos
    # position startpos moves g1f3 e7e5 b1a3 d7d5 b2b3 d8h4 h2h3 e5e4 e2e3 e4f3
    board = chess.Board()
    tokens = command.split(' ')
    if len(tokens) > 2:
      uci_moves = tokens[3:]
      for uci_move in uci_moves:
        move = chess.Move.from_uci(uci_move)
        board.push(move)
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

