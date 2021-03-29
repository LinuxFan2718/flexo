import chess
import random

# initialize a chessboard, , 
board = chess.Board()
# generate legal moves
legal_moves = list(board.legal_moves)
# select one at random
random_move = random.choice(list(legal_moves))
print(random_move.uci())
# sample output: g2g4
