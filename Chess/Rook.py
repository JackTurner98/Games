from Piece import Piece
from Move import Move

class Rook(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.setMoves()
        self.name = "R" + str(color)

    def setMoves(self):
        # White and Black Pieces
        self.moves = [None, Move(0, -1, self.MAX_LENGTH), None, Move(1, 0, self.MAX_LENGTH), None, Move(0, 1, self.MAX_LENGTH), None, Move(-1, 0, self.MAX_LENGTH)]
