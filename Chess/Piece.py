import abc

class Piece:
    __metaclass__ = abc.ABCMeta
    DIRECTIONS = {  'NW': (-1, -1),
                    'N':  (0, -1),
                    'NE': (1, -1),
                    'E':  (1, 0),
                    'SE': (1, 1),
                    'S':  (0, 1),
                    'SW': (-1, 1),
                    'W':  (-1, 0)}
    MAX_LENGTH = 8
    def __init__(self, color):
        self.color = color

    def getBoard(self):
        return self.board

    def setBoard(self, board):
        self.board = board

    def getColor(self):
        return self.color

    def setColor(self, color):
        self.color = color

    def getName(self):
        return self.name

    def getMoves(self):
        return self.moves

    @abc.abstractmethod
    def setMoves(self):
        """Calculates all possible moves of a piece, stores them in moves array"""

