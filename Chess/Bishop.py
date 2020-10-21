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
        self.moves = [Move(self.DIRECTIONS['NW'], self.MAX_LENGTH), Move(self.DIRECTIONS['N'], 0),
                      Move(self.DIRECTIONS['NE'], self.MAX_LENGTH), Move(self.DIRECTIONS['E'], 0),
                      Move(self.DIRECTIONS['SE'], self.MAX_LENGTH), Move(self.DIRECTIONS['S'], 0),
                      Move(self.DIRECTIONS['SW'], self.MAX_LENGTH), Move(self.DIRECTIONS['W'], 0)]

