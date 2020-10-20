class Move():
    DIRECTIONS = {  'NW': (-1, -1),
                    'N':  (0, -1),
                    'NE': (1, -1),
                    'E':  (1, 0),
                    'SE': (1, 1),
                    'S':  (0, 1),
                    'SW': (-1, 1),
                    'W':  (-1, 0)}

    def __init__(self, dir, length):
        self.length = length
        self.x, self.y = DIRECTION[dir]

    def getLength(self):
        return self.length

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def setLength(self, l):
        self.length = l

    def setX(self, x):
        self.x = x

    def setY(self, y):
        self.y = y

    def __str__(self):
        return "x: {x} - y: {y} - length: {l}".format(x=self.x, y=self.y, l=self.length)
