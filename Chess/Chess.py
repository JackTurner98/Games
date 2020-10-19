from Board import Board
from Pawn import Pawn


b = Board()
b.printBoard()
p = Pawn(1)
p.setMoves()
for move in p.getMoves():
    if move is not None:
        print(move)

