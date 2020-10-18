import abc

class Piece:
    __metaclass__ = abc.ABCMeta

    def __init__(self, color):
        self.color = color
        self.moves = []

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

