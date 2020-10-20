from Piece import Piece
from Move import Move

class Queen(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.setMoves()
        self.name = "Q" + str(color)

    def setMoves(self):
        # White and Black Pieces
        self.moves = [Move(-1, -1, self.MAX_LENGTH), Move(0, -1, self.MAX_LENGTH),
                      Move(1, -1, self.MAX_LENGTH), Move(1, 0, self.MAX_LENGTH),
                      Move(1, 1, self.MAX_LENGTH), Move(0, 1, self.MAX_LENGTH),
                      Move(-1, 1, self.MAX_LENGTH), Move(-1, 0, self.MAX_LENGTH)]
