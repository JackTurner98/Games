from Piece import Piece
from Move import Move

class Rook(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.setMoves()
        self.name = "R" + str(color)

    def setMoves(self):
        # White and Black Pieces
        self.moves = [Move(self.DIRECTIONS['NW'], 0), Move(self.DIRECTIONS['N'], self.MAX_LENGTH),
                      Move(self.DIRECTIONS['NE'], 0), Move(self.DIRECTIONS['E'], self.MAX_LENGTH),
                      Move(self.DIRECTIONS['SE'], 0), Move(self.DIRECTIONS['S'], self.MAX_LENGTH),
                      Move(self.DIRECTIONS['SW'], 0), Move(self.DIRECTIONS['W'], self.MAX_LENGTH)]