import time
import sys
import chess
import random

timestamp = str(int(time.time()))
logfile = "/tmp/flexo-chessmaster-" + timestamp + ".log"
log = open(logfile, "x")
stdin_fileno = sys.stdin
stdout_fileno = sys.stdout
human_move_filename = "../chess-video/player-move.txt"
chessmaster_move_filename = "../chess-video/chessmaster-move.txt"
last_chessmaster_move = ""
chessmaster_move = ""

for line in stdin_fileno:
  log.write(line)
  log.flush()
  command = line.rstrip()
  if(command == "uci"):
    stdout_fileno.write("id name Flexo Chessmaster" + '\n')
    stdout_fileno.write("id author Dennis Cahillane" + '\n')
    stdout_fileno.write('\n')
    stdout_fileno.write("uciok" + '\n')
  elif(command == "isready"):
    stdout_fileno.write("readyok" + '\n')
  elif(command == "ucinewgame"):
    pass
  elif(command.startswith("go")):
    # spin until chessmaster makes a move
    while(chessmaster_move == last_chessmaster_move):
      chessmaster_move_file = open(chessmaster_move_filename, 'r')
      chessmaster_move = chessmaster_move_file.read()
      chessmaster_move_file.close()
      time.sleep(0.1)
    last_chessmaster_move = chessmaster_move
    #
    # once move is made, extract it and send it to lichess
    stdout_fileno.write(f"bestmove {chessmaster_move}" + '\n')
  elif(command.startswith("position")):
    # position startpos
    # position startpos moves g1f3 e7e5 b1a3 d7d5 b2b3 d8h4 h2h3 e5e4 e2e3 e4f3
    #
    # extract last move from list, it is the human player move from lichess
    tokens = command.split(' ')
    human_move = tokens[-1]
    # write this move to the text file
    human_move_file = open(human_move_filename, "w")
    human_move_file.write(human_move)
    human_move_file.flush()
    human_move_file.close()
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

