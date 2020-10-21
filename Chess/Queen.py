from Piece import Piece
from Move import Move

class Queen(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.setMoves()
        self.name = "Q" + str(color)

    def setMoves(self):
        # White and Black Pieces
        self.moves = [Move(self.DIRECTIONS['NW'], self.MAX_LENGTH), Move(self.DIRECTIONS['N'], self.MAX_LENGTH),
                      Move(self.DIRECTIONS['NE'], self.MAX_LENGTH), Move(self.DIRECTIONS['E'], self.MAX_LENGTH),
                      Move(self.DIRECTIONS['SE'], self.MAX_LENGTH), Move(self.DIRECTIONS['S'], self.MAX_LENGTH),
                      Move(self.DIRECTIONS['SW'], self.MAX_LENGTH), Move(self.DIRECTIONS['W'], self.MAX_LENGTH)]
