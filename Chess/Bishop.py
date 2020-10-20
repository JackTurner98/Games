from Piece import Piece
from Move import Move

class Bishop(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.setMoves()
        self.name = "B" + str(color)

    def setMoves(self):
        tempMoves = []
        # White and Black Pieces
        self.moves = [Move(-1, -1, self.MAX_LENGTH), None, Move(1, -1, self.MAX_LENGTH), None,
                      Move(1, 1, self.MAX_LENGTH), None, Move(-1, 1, self.MAX_LENGTH), None]

