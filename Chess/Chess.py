from Board import Board
from Pawn import Pawn
import re


playing = input("Would you like to play Chess?\n>>>")
while playing:
    b = Board()
    b.printBoard()
    whiteTurn = 1
    move = []
    while len(move) < 2:
        toMove = input("Pick a piece to move, eg '64' is row 6 column 4...\n>>>")
        move = re.findall("\d", toMove)

