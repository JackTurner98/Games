from Piece import  Piece

class Pawn(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.setMoves()

    def setMoves(self):
        tempMoves = []
        # White Pieces
        if self.color == 1:
            tempMoves.append([-1, 1])
            tempMoves.append([0, 1])
            tempMoves.append([1, 1])
            print(tempMoves)
        # Black Pieces
        else:
            pass
