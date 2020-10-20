from Pawn import Pawn
from Rook import Rook
from Knight import Knight
from Bishop import  Bishop
from Queen import Queen
from King import King
from Tile import Tile

# 1  [1] [0] [1] [0] [1] [0] [1] [0]
# 2  [0] [1] [0] [1] [0] [1] [0] [1]
# 3  [1] [0] [1] [0] [1] [0] [1] [0]
# 4  [0] [1] [0] [1] [0] [1] [0] [1]
# 5  [1] [0] [1] [0] [1] [0] [1] [0]
# 6  [0] [1] [0] [1] [0] [1] [0] [1]
# 7  [1] [0] [1] [0] [1] [0] [1] [0]
# 8  [0] [1] [0] [1] [0] [1] [0] [1]
#     A   B   C   D   E   F   G   H

class Board:
    BLACK_KING_ROW = 0
    BLACK_PAWN_ROW = 1
    WHITE_KING_ROW = 7
    WHITE_PAWN_ROW = 6

    PIECES = {Pawn}
    def __init__(self):
        self.size = 8
        self.pieces = []
        self.tiles = [[None for x in range(self.size)] for x in range(self.size)]
        #self.createBoard()
        self.fillPieces()

    # Fills the tiles array with alternating colors
    def createBoard(self):
        currColor = 0  # 1 == White; 0 == Black
        for i in self.tiles:      # Numbers
            for j, tile in enumerate(i):  # Letters
                i[j] = Tile(currColor)
                currColor = int(not currColor)
            currColor = int(not currColor)

    def fillPieces(self):
        # Pawn Row
        for i in range(self.size):
            self.tiles[self.BLACK_PAWN_ROW][i] = Pawn(0)
            self.tiles[self.WHITE_PAWN_ROW][i] = Pawn(1)

        # Rooks
        self.tiles[self.BLACK_KING_ROW][0] = Rook(0)
        self.tiles[self.BLACK_KING_ROW][7] = Rook(0)

        self.tiles[self.WHITE_KING_ROW][0] = Rook(1)
        self.tiles[self.WHITE_KING_ROW][7] = Rook(1)

        # Knights
        self.tiles[self.BLACK_KING_ROW][1] = Knight(0)
        self.tiles[self.BLACK_KING_ROW][6] = Knight(0)

        self.tiles[self.WHITE_KING_ROW][1] = Knight(1)
        self.tiles[self.WHITE_KING_ROW][6] = Knight(1)
        # Bishops
        self.tiles[self.BLACK_KING_ROW][2] = Bishop(0)
        self.tiles[self.BLACK_KING_ROW][5] = Bishop(0)

        self.tiles[self.WHITE_KING_ROW][2] = Bishop(1)
        self.tiles[self.WHITE_KING_ROW][5] = Bishop(1)

        # Queen
        self.tiles[self.BLACK_KING_ROW][3] = Queen(0)
        self.tiles[self.WHITE_KING_ROW][3] = Queen(1)

        # King
        self.tiles[self.BLACK_KING_ROW][4] = King(0)
        self.tiles[self.WHITE_KING_ROW][4] = King(1)

    # Prints a pretty version of the game board
    def printBoard(self):
        # Print x Coords on top of board
        lineStr = "  "
        for i in range(self.size):
            lineStr += " {} ".format(i)
        print(lineStr)

        for i, ytile in enumerate(self.tiles):
            # Start and end with y coord
            lineStr = "{} ".format(i)
            for j in ytile:
                if j is not None:
                    lineStr += "[{}]".format(j.getName())
                else:
                    lineStr += "[ ]"
            print(lineStr + " {}".format(i))

        # Print x Coords on bottom of board
        lineStr = "  "
        for i in range(self.size):
            lineStr += " {} ".format(i)
        print(lineStr)

    def getTiles(self):
        return self.tiles

    def getSize(self):
        return self.size

