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
            self.moves = [Move('NW', 1), Move('N', 1), Move('NE', 1), Move('E', 0),
                          Move('SE', 0), Move('S', 0), Move('SW', 0), Move('W', 0)]
        # Black Pieces
        else:
            self.moves = [Move('NW', 0), Move('N', 0), Move('NE', 0), Move('E', 0),
                          Move('SE', 1), Move('S', 1), Move('SW', 1), Move('W', 0)]
