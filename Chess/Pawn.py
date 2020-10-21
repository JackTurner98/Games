from Piece import Piece
from Move import Move

class Pawn(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.setMoves()
        self.name = "P" + str(color)

    def setMoves(self):
        tempMoves = []
        # White Pieces
        if self.color == 1:
            self.moves = [Move(self.DIRECTIONS['NW'], 1), Move(self.DIRECTIONS['N'], 1),
                          Move(self.DIRECTIONS['NE'], 1), Move(self.DIRECTIONS['E'], 0),
                          Move(self.DIRECTIONS['SE'], 0), Move(self.DIRECTIONS['S'], 0),
                          Move(self.DIRECTIONS['SW'], 0), Move(self.DIRECTIONS['W'], 0)]
        # Black Pieces
        else:
            self.moves = [Move(self.DIRECTIONS['NW'], 0), Move(self.DIRECTIONS['N'], 0),
                          Move(self.DIRECTIONS['NE'], 0), Move(self.DIRECTIONS['E'], 0),
                          Move(self.DIRECTIONS['SE'], 1), Move(self.DIRECTIONS['S'], 1),
                          Move(self.DIRECTIONS['SW'], 1), Move(self.DIRECTIONS['W'], 0)]
