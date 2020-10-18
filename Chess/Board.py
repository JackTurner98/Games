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
    def __init__(self):
        self.size = 8
        self.tiles = [[None for x in range(self.size)] for x in range(self.size)]
        self.createBoard()

    # Fills the tiles array with alternating colors
    def createBoard(self):
        currColor = 1  # 1 == White; 0 == Black
        for i in range(self.size):      # Numbers
            for j in range(self.size):  # Letters
                self.tiles[i][j] = Tile(currColor)
                currColor = int(not currColor)
            currColor = int(not currColor)

    # Prints a pretty version of the game board
    def printBoard(self):
        lineStr = ""
        for i in self.tiles:
            for j in i:
                lineStr += "[{}]".format(j.getColor())
            print(lineStr)
            lineStr = ""

