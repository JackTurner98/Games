from Piece import Piece
from Move import Move

class King(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.setMoves()
        self.name = "*" + str(color)

    def setMoves(self):
        # White and Black Pieces
        self.moves = [Move(self.DIRECTIONS['NW'], 1), Move(self.DIRECTIONS['N'], 1),
                      Move(self.DIRECTIONS['NE'], 1), Move(self.DIRECTIONS['E'], 1),
                      Move(self.DIRECTIONS['SE'], 1), Move(self.DIRECTIONS['S'], 1),
                      Move(self.DIRECTIONS['SW'], 1), Move(self.DIRECTIONS['W'], 1)]