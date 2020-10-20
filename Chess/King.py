from Piece import Piece
from Move import Move

class King(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.setMoves()
        self.name = "*" + str(color)

    def setMoves(self):
        # White and Black Pieces
        self.moves = [Move(-1, -1, 1), Move(0, -1, 1),
                      Move(1, -1, 1), Move(1, 0, 1),
                      Move(1, 1, 1), Move(0, 1, 1),
                      Move(-1, 1, 1), Move(-1, 0, 1)]