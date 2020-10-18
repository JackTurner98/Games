import abc

class Piece:
    __metaclass__ = abc.ABCMeta

    def __init__(self, color, location, board):
        self.color = color
        self.location = location
        self.moves = []
        self.board = board

    def getBoard(self):
        return self.board

    def setBoard(self, board):
        self.board = board

    def getColor(self):
        return self.color

    def setColor(self, color):
        self.color = color

    def getLocation(self):
        return self.location

    def setLocation(self, location):
        self.location = location

    def getMoves(self):
        return self.moves

    @abc.abstractmethod
    def setMoves(self):
        """Calculates all possible moves of a piece, stores them in moves array"""

