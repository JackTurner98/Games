from Piece import Piece
from Move import Move

class Pawn(Piece):
    DIRECTIONS = 8
    def __init__(self, color):
        super().__init__(color)
        self.setMoves()

    def setMoves(self):
        tempMoves = []
        # White Pieces
        if self.color == 1:
            self.moves = [Move(-1, -1, 1), Move(0, -1, -1), Move(1, -1, 1), None, None, None, None, None]
        # Black Pieces
        else:
            self.moves = [Move(-1, 1, 1), Move(0, 1, -1), Move(1, 1, 1), None, None, None, None, None]
