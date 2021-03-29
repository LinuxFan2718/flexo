import chess
import random

# initialize a chessboard, , 
board = chess.Board()
# generate legal moves
legal_moves = list(board.legal_moves)
# select one at random
random_move = random.choice(list(legal_moves))
print(random_move.uci()) # sample output: g2g4
# make that move
board.push(random_move)
legal_moves2 = list(board.legal_moves)
random_move2 = random.choice(list(legal_moves2))
print(random_move2.uci())
board.push(random_move2)
print(board)
pass