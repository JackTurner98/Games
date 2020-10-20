from Piece import Piece
from Move import Move

class Knight(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.setMoves()
        self.name = "K" + str(color)

    def setMoves(self):
        # White and Black Pieces
        self.moves = [Move(-2, -1, 1), Move(-1, -2, 1), Move(1, -2, 1), Move(2, -1, 1),
                      Move(2, 1, 1), Move(1, 2, 1), Move(-1, 2, 1), Move(-2, 1, 1)]
